from flask import Flask, render_template, request
import config as config #src.config to config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Здесь может быть проверка данных пользователя

        return f'Добро пожаловать, {username}!'
    
    return render_template('login.html')

if __name__ == '__main__':
    config.load_configurate('config.json')
    app.run(port=int(config.data['server_port']), host=str(config.data['server_host']), debug=bool(config.data['server_debug']))