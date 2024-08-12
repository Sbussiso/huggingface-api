import requests

session = requests.Session()

# Local base URL
base_url = 'http://127.0.0.1:8000'

sentiment_pipe_url = f'{base_url}/sentiment-pipe'
data = {'user_message': 'I love this product!'}

response = session.post(sentiment_pipe_url, json=data)

try:
    response.raise_for_status()  # Check for HTTP errors
    print("Sentiment analysis response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Failed to parse JSON. Response content:", response.text)
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred: {err}")
