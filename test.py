import requests

session = requests.Session()

base_url = 'http://127.0.0.1:5000'

sentiment_pipe_url = f'{base_url}/sentiment-pipe'
data = {'user_message': 'I love this product!'}
response = session.post(sentiment_pipe_url, json=data)
print("Sentiment analysis response:", response.json())