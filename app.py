import random

from flask import Flask, render_template, request, redirect, url_for
from src.core.classes.user import User
from src.config import load_configurate

import re
import secrets
import string

cfg = load_configurate('src/config.json')

app = Flask(__name__, root_path='src/')


def generate_password():
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W]).{8,64}$'

    while True:
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random.randint(8, 64)))
        if re.match(pattern, password):
            return password

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
    return f''

@app.route('/login/<password>')
@app.route('/login', methods=['GET', 'POST'])
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
                return f'Добро пожаловать, {username}, статус {user_obj.status_code}, токен { user_obj.get_token }!'


        if request.form['submit_button'] == 'register':
            user_obj = User().sign_up()
            user_obj.execute(username, password)         
            
            if(user_obj.status_code == 200):
                return f'Учетная запись с именем, { username }, создана!'
        
        return f'Неверные параметры POST'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))