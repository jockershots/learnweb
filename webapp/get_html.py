import requests
from bs4 import BeautifulSoup

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
            result.append({
                'title': title,
                'link': link,
                'time': time
            })
        return result
    return "Ошибка"
