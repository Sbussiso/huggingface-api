from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from transformers import pipeline
from tensorflow.keras import layers


load_dotenv()

app = Flask(__name__)
app.secret_key = 'secret_key'

# Sentiment analysis pipeline
def sentiment_analysis(text: str) -> str:
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    classifier = pipeline("sentiment-analysis", model=model_name)
    result = classifier(text)
    return result[0]

# Sentiment analysis route
@app.route('/sentiment-pipe', methods=['POST'])
def sentiment_pipe():
    data = request.json
    user_message = data.get('user_message')

    if not user_message:
        return jsonify({"error": "No user_message provided"}), 400

    result = sentiment_analysis(user_message)
    return jsonify({"message": result})

# Sentiment analysis route
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Binding to port {port}")
    app.run(host='0.0.0.0', port=port)
