from flask import Flask, request, jsonify, session
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')  # Replace with a real secret key


#sentiment analysis pipeline
def sentiment_analysis(text: str) -> str:
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = pipeline("sentiment-analysis", model=model_name)
    result = classifier(text)
    return result[0]

#!sentiment analysis route
@app.route('/sentiment-pipe', methods=['POST'])
def sentiment_pipe():
    data = request.json
    user_message = data.get('user_message')

    result = sentiment_analysis(user_message)
    return jsonify({"message": result})


if __name__ == '__main__':
    app.run(debug=True)
