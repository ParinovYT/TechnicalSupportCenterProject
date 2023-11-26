from flask import Flask, render_template, request

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
        # ОНА УЖЕ ЕСТЬ, ОВЕТ BAD_REQUEST ЭТО И ЕСТЬ НЕПРАВИЛЬНЫЕ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ :D
             
        if request.form['submit_button'] == 'login':
            return f'Добро пожаловать, {username}!'
        
        if request.form['submit_button'] == 'register':
            return f'Создана учетная запись с именем, {username}!'
        
        return f'Неверные параметры POST'
    
    return render_template('login.html')