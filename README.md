# Dr.Py - Stress relief chatbot

A Flask-based web application that uses a generative AI model to provide a chatbot interface for stress relief and mood analysis. It also performs sentiment analysis using the NLTK library and stores chat history in Firebase Firestore.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Screenshots](#screenshots)

## Features

- **Chatbot Interaction:** Chat with the AI-powered bot for stress relief.
- **Principle:** The design leverages the "Dopamine Design" principle, which suggests that a visually appealing and user-friendly interface can enhance dopamine levels in the brain, creating a sense of pleasure and well-being.
- **Mood Analysis:** Sentiment analysis of the user's messages using NLTK's VADER sentiment analyzer.
- **Chat History:** Stores chat history and mood data in Firebase Firestore.
- **Interactive Graph:** Displays mood analysis using matplotlib.
- **Login and Logout:** Simple login with email and secure session management.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abbilaash/Techathon-24.git
    cd Techathon-24
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Start the Flask application:**

    ```bash
    python run.py
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.
   The default email is 'abbilaashat@gmail.com' and password is 'abbi123'

## Screenshots
![image](https://github.com/user-attachments/assets/d705e094-53fe-475c-9409-fe9bfedaa93f)
![image](https://github.com/user-attachments/assets/222a37c3-6098-4982-853a-bb74cddea7fa)
![image](https://github.com/user-attachments/assets/4c1ab372-f05a-4be6-ab87-90ca312a8907)
![image](https://github.com/user-attachments/assets/e36df796-403e-4d3d-bb5b-1555afb157d5)




