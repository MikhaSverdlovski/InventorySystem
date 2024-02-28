import hashlib
import os
from flask import Flask, request, redirect, url_for, render_template
from Config import db_connect
from Service.SqlConnectorService import SqlConnectorService

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login_or_register():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Войти':
            # Обработка события для кнопки "Войти"
            # Здесь можно добавить вашу логику для входа пользователя
            return redirect(url_for('login'))
        elif request.form['submit_button'] == 'Зарегистрироваться':
            # Обработка события для кнопки "Зарегистрироваться"
            # Здесь можно добавить вашу логику для перехода на страницу регистрации
            return redirect(url_for('register'))
    return render_template('login.html')


@app.route('/login')
# Скорее всего не понадобиться. Редиректить будем вовнутрь проекта
def login():
    # Здесь можно добавить вашу логику для страницы входа
    return "Страница входа"


@app.route('/register')
def register():
    return render_template("registration.html")


@app.route('/register_confirm', methods=['POST'])
def register_confirm():
    # TODO: не работает подключение к БД в докере, поправить
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
                _SQL = """INSERT INTO users (login, passw_hash, salt) VALUES (%s, %s, %s)"""
                cursor.execute(_SQL, (username, password_hash, salt))

            return "Success"
    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
