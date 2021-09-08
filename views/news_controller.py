from flask import render_template
from config import app

class NewsController(object):

    @staticmethod
    @app.route('/news/create')
    def create():
        """ Метод для загрузки шаблона главной страницы """
        return render_template('/news/create.html')

    @staticmethod
    @app.route('/news/delete')
    def delete():
        """ Метод для загрузки шаблона страницы Про сайт """
        return render_template('news/delete.html')

    @staticmethod
    @app.route('/news/details')
    def details():
        """ Метод для загрузки шаблона страницы контактов"""
        return render_template('news/details.html')

    @staticmethod
    @app.route('/news/list')
    def list():
        """ Метод для загрузки шаблона страницы контактов"""
        return render_template('news/list.html')

    @staticmethod
    @app.route('/news/update')
    def update():
        """ Метод для загрузки шаблона страницы контактов"""
        return render_template('news/update.html')