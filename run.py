from flask import render_template, request, redirect, url_for, Flask, flash, session
from app import bot
from app import auth

app = Flask(__name__)
app.secret_key = 'kjhgdfkldhsafksdhfkl'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))
    

@app.route('/about')
def about():
    return render_template('about.html')





# making the login and signup routes
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        auth_ = auth.login(email, password)      # [1, "Abbilaash"]
        if auth_[0] == 1:
            session['name'] = auth_[1]
            session['email'] = email
            flash("You have successfully logged in.", "success")
            return redirect(url_for('home'))
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
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
