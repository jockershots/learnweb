from datetime import datetime
from re import S
import requests
from bs4 import BeautifulSoup
from webapp.model import db, News

def get_html(link):
    try:
        result = requests.get(link)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        return False

def get_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts menu').findAll('li')
        result = []
        for news in all_news:
            title = news.find('a').text
            link = news.find('a')['href']
            time = news.find('time').text
            try:
                time = datetime.strptime(time, '%Y-%m_%d')
            except ValueError:
                time = datetime.now()
            save_news(title, link, time)

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()