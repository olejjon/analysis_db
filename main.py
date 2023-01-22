from flask import Flask, request, render_template, jsonify
from utils import receive_film, receive_date_film, receive_rate_film, receive_genre_film

app = Flask(__name__)


@app.route('/movie/<title>')
def page_form(title):
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_film(title)
    return jsonify(db_film)


@app.route('/movie/year/to/<int:year>')
def page_date(year):
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_date_film(year)
    return jsonify(db_film)


@app.route('/rating/children')
def page_children():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_rate_film('g')
    return jsonify(db_film)


@app.route('/rating/family')
def page_family():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_rate_film('f')
    return jsonify(db_film)


@app.route('/rating/adult')
def page_adult():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_rate_film('a')
    return jsonify(db_film)


@app.route('/genre/<genre>')
def page_genre(genre):
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    db_film = receive_genre_film(genre)
    return jsonify(db_film)


app.run()


