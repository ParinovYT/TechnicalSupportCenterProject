from flask import Flask, render_template, request, redirect, url_for
from src.core.classes.user import User
from src.config import load_configurate

cfg = load_configurate('src/config.json')

app = Flask(__name__, root_path='src/')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pass
    return f''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if request.form['submit_button'] == 'login':   
            user_obj = User().sign_in()
            user_obj.execute(username, password, 60)
            return f'Добро пожаловать, {username}, статус {user_obj.status_code}, токен { user_obj.get_token }!'

        if request.form['submit_button'] == 'register':
            user_obj = User().sign_up()
            user_obj.execute(username, password)         
            
            if(user_obj.status_code == 200):
                return redirect(url_for("username", name=username))
            return f'При создании учетной записи с именем, { username }, возникла ошибка. Status: { user_obj.status_code }!'
        
        return f'Неверные параметры POST'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))