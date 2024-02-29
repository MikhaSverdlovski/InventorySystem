from flask import Flask, request, redirect, url_for, render_template, session
from Config import secret_key
from security.Security import registration, check_password, check_logged_in

app = Flask(__name__)
app.secret_key = secret_key


@app.route('/', methods=['GET', 'POST'])
def login_or_register():
    if session.get('logged_in'):
        return redirect(url_for('main_page'))
    if request.method == 'POST':
        if request.form['submit_button'] == 'Войти':
            if check_password(request.form['username'], request.form['password']):
                return redirect(url_for('main_page'))
            return render_template("registration.html")
        elif request.form['submit_button'] == 'Зарегистрироваться':
            return render_template("registration.html")
    return render_template('login.html')


@app.route('/login')
@check_logged_in
def main_page():
    # Здесь можно добавить вашу логику для страницы входа
    return "Страница входа"


@app.route('/another')
@check_logged_in
def another():
    """Просто для демонстрации вторая страница для залогированных"""
    return 'another page'


@app.route('/logout')
@check_logged_in
def logout():
    """Разлогиниться.
    TODO Добавить потом сюда переброс на страницу входа"""
    session.pop('logged_in')
    return "You are now logged_out"


@app.route('/register_confirm', methods=['POST'])
def register_confirm():
    """Метод для регистрации нового пользователя (Сохранение в базу)"""
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    registration(username, email, password)
    return redirect(url_for('login_or_register'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
