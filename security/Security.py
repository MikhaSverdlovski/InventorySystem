import functools
import hashlib
import os
from typing import Callable
from flask import session, redirect, url_for
from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService


class Security:
    @staticmethod
    def registration(username, email, password) -> str:
        try:
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

    @staticmethod
    def check_password(password: str, user: str) -> bool:
        with SqlConnectorService(db_connect) as cursor:
            _SQL = """SELECT salt, passw_hash FROM users WHERE login = %s"""
            cursor.execute(_SQL, (user,))
            result = cursor.fetchone()
        hashed_password = hashlib.sha256((password + str(result[0])).encode()).hexdigest()
        session['logged_in'] = True
        return hashed_password == result[1]

    @staticmethod
    def check_logged_in(func):
        @functools.wraps(func)
        def check_logged_in_wrapper(*args, **kwargs):
            if 'logged_in' in session:
                return func(*args, **kwargs)
            else:
                return redirect(url_for('login_or_register'))
        return check_logged_in_wrapper



