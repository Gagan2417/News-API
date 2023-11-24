from flask import Flask, render_template, request
import requests

app=Flask(__name__)

NEWS_API_KEY = 'AgZaN18JE4QP7XEjTcXYHvfI5O2e6Hilc5RpnZwc'

@app.route('/')
def index():
    # Example: fetching top headlines
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()

    headlines = news_data['articles']

    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)