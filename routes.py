from flask import Blueprint, redirect, render_template, request
from src.core.classes.user import User
from src.tools import generate_password

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return redirect('/home')

@routes.route('/home', methods=['GET', 'POST'])
def home_general():
    return render_template('example/home.html')


@routes.route('/login/<password>')
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.args.get('passwordGenerate'):
        return render_template('login.html', password=generate_password())

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if request.form['submit_button'] == 'login':
            user_obj = User().sign_in()
            user_obj.execute(username, password, 60)

            statuscode = user_obj.status_code
            token = user_obj.get_token
            print(statuscode)
            if statuscode == 401:
                return 'Пользователь не найден'
            elif statuscode == 400:
                return 'Неверный логин или пароль!'
            elif statuscode == 200:
                return f'Добро пожаловать, {username}, статус {user_obj.status_code}, токен {user_obj.get_token}!'

        if request.form['submit_button'] == 'register':
            user_obj = User().sign_up()
            user_obj.execute(username, password)

            if (user_obj.status_code == 200):
                return f'Учетная запись с именем, {username}, создана!'

        return f'Неверные параметры POST'

    return render_template('login.html')