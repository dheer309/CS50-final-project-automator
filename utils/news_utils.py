import feedparser
import requests


def get_top_stories():
    url = 'https://news.google.com/rss'
    response = requests.get(url)
    feed = feedparser.parse(response.text)
    top_stories = [entry.title for entry in feed.entries]
    return top_stories


def present_in_bulleted_list(stories):
    for story in stories:
        print(f'• {story}')
