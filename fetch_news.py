import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_news(topic):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("articles", [])

    news_list = []

    for article in articles:
        title = article.get("title", "")
        description = article.get("description", "")
        content = article.get("content", "")

        combined_text = f"Title: {title}\nDescription: {description}\nContent: {content}"

        news_list.append(combined_text)

    return news_list