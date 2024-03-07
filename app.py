from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from Config import secret_key
from Service.DbActions import DbActions
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
    items = DbActions.get_items()  # Получаем данные из БД
    return render_template('main.html', items=items)


@app.route('/statistics')
@Security.check_logged_in
def another_page():
    return render_template('statictics.html')


@app.route('/articles')
@Security.check_logged_in
def articles():
    articles = DbActions.get_articles()
    return render_template('articles.html', articles=articles)


@app.route('/get_item', methods=['GET'])
def get_item():
    item_id = int(request.args.get('id'))
    weapon = DbActions.get_item(item_id)

    if weapon:
        return jsonify(weapon)
    return jsonify({'error': 'Элемент с указанным id не найден'})


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


@app.route('/add_item', methods=['POST'])
@Security.check_logged_in
def add_item():
    item_name = request.form['name_gun']
    item_descr = request.form['descr_gun']
    type_item = request.form['gun_type']
    manufacturer = request.form['manufacturer']
    year = request.form['year']
    country = request.form['country']
    price = request.form['price']
    quantity = request.form['quantity']
    image = request.form['image']
    DbActions.add_item(item_name, item_descr, type_item, manufacturer, year, country, price, quantity)
    return render_template('main.html')


@app.route('/edit_item', methods=['POST'])
def edit_item():
    item_id = request.form.get('item_id')
    name = request.form.get('name_gun')
    descr = request.form.get('descr_gun')
    type_item = request.form.get('gun_type')
    manufacturer = request.form.get('manufacturer')
    year = request.form.get('year')
    country = request.form.get('country')
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    success = DbActions.edit_item(item_id, name, descr, type_item, manufacturer, year, country, price, quantity)

    if success:
        return redirect(url_for('main_page'))
    else:
        return jsonify({'error': 'Произошла ошибка при обновлении элемента'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
