from flask import Flask, request, redirect, url_for, render_template, session
from Config import secret_key
from security.Security import Security

app = Flask(__name__)
app.secret_key = secret_key


@app.route('/', methods=['GET', 'POST'])
def login_or_register():
    if session.get('logged_in'):
        return redirect(url_for('main_page'))
    if request.method == 'POST':
        if request.form['submit_button'] == 'Войти':
            if Security.check_password(request.form['username'], request.form['password']):
                return redirect(url_for('main_page'))
            return render_template("registration.html")
        elif request.form['submit_button'] == 'Зарегистрироваться':
            return render_template("registration.html")
    return render_template('login.html')


@app.route('/login')
@Security.check_logged_in
def main_page():
    return render_template('main.html')


@app.route('/statistics')
@Security.check_logged_in
def another_page():
    return render_template('statictics.html')


@app.route('/logout')
@Security.check_logged_in
def logout():
    session.pop('logged_in')
    return redirect(url_for('main_page'))


@app.route('/register_confirm', methods=['POST'])
def register_confirm():
    """Метод для регистрации нового пользователя (Сохранение в базу)"""
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    Security.registration(username, email, password)
    return redirect(url_for('login_or_register'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
