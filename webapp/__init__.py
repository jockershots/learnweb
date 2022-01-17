from flask import Flask, render_template

from webapp.model import db, News
from webapp.get_html import get_news

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        news_list = News.query.order_by(News.time.desc()).all()
        return render_template('index.html', page_title=title, news_list=news_list)

    return app
    # set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run