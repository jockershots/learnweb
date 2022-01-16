from flask import Flask, render_template

from webapp.model import db
from webapp.get_html import get_news

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        news_list = get_news()
        return render_template('index.html', page_title=title, news_list=news_list)

    return app