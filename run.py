from flask import render_template, request, redirect, url_for, Flask, flash, session, jsonify

from app import auth
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import google.generativeai as genai
from dotenv import load_dotenv
import os
import datetime
from matplotlib import pyplot as plt
import base64
import io
from scipy.interpolate import make_interp_spline
import numpy

app = Flask(__name__)
app.secret_key = 'kjhgdfkldhsafksdhfkl'
app.config['SESSION_TYPE'] = 'filesystem'

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('techathon24-106b3-firebase-adminsdk-ecjpy-5aa2cc6fa2.json')
    firebase_admin.initialize_app(cred)
else:
    print("[!] Firebase SDK is already initialized")
db = firestore.client()

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

def sentiment_analysis(text, email):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        sentiment = "positive"
    elif sentiment_score['compound'] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    try:
        new_city_ref = db.collection("sentiment_his").document()
        new_city_ref.set({
            "email": email,
            "score": sentiment_score['compound'],
            "sentiment": sentiment,
            "date": datetime.datetime.now().timestamp(),
            "message": text
        })
    except Exception as e:
        print(f"[-] Error in saving sentiment to database: {e}")

def start_chat_session():
    chat = model.start_chat(
        # setting the memory with custom chat history
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Hi there! How can I assist you with stress relief today?"},
            {"role": "user", "parts": "You have to assist me with my stress and mental health and always make me feel comfortable."},
            {"role": "model", "parts": "ok"},
            {"role": "user", "parts": "your name is Dr.Py"},
            {"role": "model", "parts": "ok"},
        ]
    )
    return chat

def get_gemini_response(user_input, chat):
    response = chat.send_message(user_input)
    return response.text


@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'chat_history' not in session:
        session['chat_history'] = []

    if request.method == 'POST':
        user_message = request.form['message']
        email = session.get('email', session['email'])

        if "mood analysis" in user_message.lower():
            return redirect(url_for('mood_analytics'))

        chat = start_chat_session()
        sentiment_analysis(user_message, email)

        bot_response = get_gemini_response(user_message, chat)

        session['chat_history'].append({"role": "user", "text": user_message})
        session['chat_history'].append({"role": "bot", "text": bot_response})

    return render_template('index.html', username = session['name'],messages=session.get('chat_history', []))




@app.route('/mood_analytics')
def mood_analytics():
    email = session['email']
    mood_data = []

    try:
        # Fetching documents from Firestore
        docs = db.collection("sentiment_his").where("email", "==", email).stream()
        for doc in docs:
            mood_data.append(doc.to_dict())
    except Exception as e:
        print(f"[-] Error fetching mood data: {e}")

    if not mood_data:
        return render_template('index.html', user_name=session['name'], messages=session.get('chat_history', []), error="No mood data available.")

    # Plotting the graph
    dates = []
    scores = []

    for doc in mood_data:
        try:
            timestamp = doc['date']
            dates.append(timestamp)
            scores.append(doc['score'])
        except Exception as e:
            print(f"[-] Error parsing date: {e}")
    combined = list(zip(dates, scores))
    combined.sort(key=lambda x: x[0])
    dates, scores = zip(*combined) if combined else ([], [])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, scores, marker='o', linestyle='-', color='b')
    plt.xlabel('Timestamp')
    plt.ylabel('Mood Score')
    plt.title('Mood Score Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()

    # Add a bot message to session chat history
    session['chat_history'].append({"role": "bot", "text": "Here is your mood analysis graph."})

    return render_template('index.html', user_name=session['name'], messages=session.get('chat_history', []), graph_url=graph_url)







# making the login and signup routes
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        auth_ = auth.login(email, password)      # [1, "Abbilaash"]
        print(auth_)
        if auth_[0] == 1:
            session['name'] = auth_[1]
            session['email'] = email
            flash("You have successfully logged in.", "success")
            return redirect(url_for('chat'))
        else:
            flash("Invalid credentials, please try again.", "danger")
            return redirect(url_for('login'))
    else:
        if 'email' in session:
            return redirect(url_for('home'))
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        auth.signup(name, email, password)
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('name', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
