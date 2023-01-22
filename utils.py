import sqlite3

from flask import jsonify


def receive_film(name):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT title, country, release_year, listed_in, description FROM netflix WHERE title = '{name}'"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'title': row[0],
                'country': row[1],
                'release_year': row[2],
                'listed_in': row[3],
                'description': row[4]
            }
            return json_row


def receive_date_film(year):
    year1 = year // 10000
    year2 = year % 10000

    with sqlite3.connect("netflix.db") as connection:
        list_film = []
        cursor = connection.cursor()
        query = f"SELECT title, release_year FROM netflix WHERE release_year BETWEEN {year1} and {year2} LIMIT 100"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'title': row[0],
                'release_year': row[1]
            }
            list_film.append(json_row)

        return list_film


def receive_rate_film(rate):
    # (G, PG, PG-13)
    # (R, NC-17)

    with sqlite3.connect("netflix.db") as connection:
        list_film = []
        cursor = connection.cursor()
        if rate == 'f':
            query = f"SELECT title, rating, description " \
                    f"FROM netflix " \
                    f"rating LIKE 'G' or " \
                    f"rating LIKE 'PG-13' or" \
                    f"rating LIKE 'PG'"
        elif rate == 'g':
            query = f"SELECT title, rating, description " \
                    f"FROM netflix " \
                    f"WHERE rating LIKE 'G'"
        elif rate == 'a':
            query = f"SELECT title, rating, description " \
                    f"FROM netflix " \
                    f"WHERE rating LIKE 'R' or " \
                    f"rating LIKE 'NC-17'"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'title': row[0],
                'rating': row[1],
                'description': row[2]
            }
            list_film.append(json_row)

        return list_film


def receive_genre_film(genre):
    with sqlite3.connect("netflix.db") as connection:
        list_film = []
        cursor = connection.cursor()
        query = f"SELECT title, description " \
                f"FROM netflix " \
                f"WHERE listed_in LIKE '%{genre}%'" \
                f"ORDER BY 'release_year' DESC " \
                f"LIMIT 10"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'title': row[0],
                'description': row[1]
            }
            list_film.append(json_row)

        return list_film


def actor_db(text):
    index_actor1 = text.find('и')
    actor1 = text[:index_actor1 - 1]
    actor2 = text[index_actor1 + 1:]
    with sqlite3.connect("netflix.db") as connection:
        list_film = []
        cursor = connection.cursor()
        query = f"SELECT netflix.cast " \
                f"FROM netflix " \
                f"WHERE netflix.cast LIKE '%{actor1}%' or " \
                f"netflix.cast LIKE '%{actor2}%'"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'cast': row[0]
            }
            list_film.append(json_row)

        return list_film


def actor_db(type, year, genre):
    # тип, год, жанр
    with sqlite3.connect("netflix.db") as connection:
        list_film = []
        cursor = connection.cursor()
        query = f"SELECT title, description " \
                f"FROM netflix " \
                f"WHERE type = '{type}' AND " \
                f"year = '{year}' AND " \
                f"listed_in LIKE '{genre}'"
        cursor.execute(query)
        for row in cursor.fetchall():
            # А нормальная какая-нибудь функция или метод есть чтобы вот такое не писать????
            json_row = {
                'cast': row[0]
            }
            list_film.append(json_row)

        return list_film
