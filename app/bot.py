import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to start a chat session and manage conversation history
def start_chat_session():
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Hi there! How can I assist you with stress relief today?"},
            {"role": "user", "parts": "Here after your name is CalmAI."},
            {"role": "model", "parts": "ok"}
        ]
    )
    return chat

# Function to send a message and get a response
def get_gemini_response(user_input, chat):
    response = chat.send_message(user_input)
    return response.text

# Main function to simulate a chatbot conversation
def chatbot():
    print("Chatbot: Hi! I'm here to help you with stress relief. How are you feeling today?")
    
    # Start the chat session
    chat = start_chat_session()
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit"]:
            print("CalmAI: Goodbye! Take care.")
            break
        
        response = get_gemini_response(user_input, chat)
        print(f"CalmAI: {response}")
        print(chat.history) # Print the conversation history

# Run the chatbot
#chatbot()
