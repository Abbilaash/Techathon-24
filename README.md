# Dr.Py - Stress relief chatbot

A Flask-based web application that uses a generative AI model to provide a chatbot interface for stress relief and mood analysis. It also performs sentiment analysis using the NLTK library and stores chat history in Firebase Firestore.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)

## Features

- **Chatbot Interaction:** Chat with the AI-powered bot for stress relief.
- **Mood Analysis:** Sentiment analysis of the user's messages using NLTK's VADER sentiment analyzer.
- **Chat History:** Stores chat history and mood data in Firebase Firestore.
- **Interactive Graph:** Displays mood analysis using matplotlib.
- **Login and Logout:** Simple login with email and secure session management.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- pip (Python package manager)
- Firebase account with Firestore enabled
- Google Cloud API Key for Generative AI model (Gemini API)

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
