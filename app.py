from flask import Flask, render_template, request
from src.core.classes.user import User
from src.config import load_configurate

cfg = load_configurate('src/config.json')

app = Flask(__name__, root_path='src/')

@app.route('/')
def index():
    return f"{cfg}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if request.form['submit_button'] == 'login':
            return f'Добро пожаловать, {username}!'

        if request.form['submit_button'] == 'register':
            user_obj = User().sign_up()
            user_obj.execute(username, password)         
            return f'Создана учетная запись с именем, { username }, статус { user_obj.status_code }!'
        
        return f'Неверные параметры POST'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))