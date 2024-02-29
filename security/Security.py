import functools
import hashlib
import os
from typing import Callable

from flask import request, session

from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService


def registration() -> str:
    try:
        if request.form['submit_button'] == 'Зарегистрироваться':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            # Генерация соли
            salt = os.urandom(32).hex()

            # Хеширование пароля с солью
            password_hash = hashlib.sha256((password + salt).encode()).hexdigest()

            # Создание нового пользователя
            with SqlConnectorService(db_connect) as cursor:
                _SQL = """INSERT INTO users (login, passw_hash, salt, email) VALUES (%s, %s, %s, %s)"""
                cursor.execute(_SQL, (username, password_hash, salt, email))

            return "Success"
    except Exception as e:
        return f"Error: {e}"


def check_password(password: str, user: str) -> bool:
    with SqlConnectorService(db_connect) as cursor:
        _SQL = """SELECT salt, passw_hash FROM users WHERE login = %s"""
        cursor.execute(_SQL, (user,))
        result = cursor.fetchone()
    hashed_password = hashlib.sha256((password + str(result[0])).encode()).hexdigest()
    session['logged_in'] = True
    return hashed_password == result[1]


def check_logged_in(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return "You are not logged in"

    return wrapper
