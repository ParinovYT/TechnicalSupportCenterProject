import calendar
from datetime import datetime
import time 

from imports import Blueprint, redirect, render_template, request, User, Report, MySqlBase, session, getConfigurate, url_for, is_valid_password, is_valid_username

routes = Blueprint('routes', __name__)

cfg = getConfigurate()

if cfg['server_debug'] == False:
    @routes.errorhandler(Exception)
    def handle_error(e):
        return render_template('errors/500.html', error=e)

def checkLogin():
    result = False
    if 'login' in session and 'time' in session and 'token' in session and 'type' in session:  
        print(f"login: {session.get('login')} | time: {session.get('time')} | token: {session.get('token')} | type: {session.get('type')}")    
        result = True
        timestamp = calendar.timegm(time.gmtime())
        if timestamp > session.get('time'):
            print('pop time/login/token')
            session.pop('time', None) 
            session.pop('login', None) 
            session.pop('token', None) 
            session.pop('type', None) 
            print('redirect to login page | EXPIRED sessions')
            result = False
    else:
            result = False
            print('redirect to login page | none sessions')
    return result


def get_rule_by_login(value: str):
    from src.core.classes.mysql import MySqlBase
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute("SELECT rule FROM users WHERE username=%s", (value,))
        row = cursor.fetchone()
        if row:
            rule_id = int(row[0])
            return rule_id
        else:
            return 0
    finally:
        db_connection.close()

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if checkLogin() == True:
        return redirect(url_for('.home_general')) 
    
    _status = 0
    _token = 0
    _rule_selected = 0
    _rule_selected_index = 0
    
    if request.method == 'POST':
        user_obj = User().sign_in()
        user_obj.execute(request.form['username'], request.form['password'], int(cfg['login_timeout']))  
        _status = user_obj.status_code
        _token = user_obj.get_token 

        _rule_selected = request.form['rule'] 
        if _rule_selected == 'Пользователь':
            _rule_selected_index = 4
        
        if get_rule_by_login(request.form['username']) != _rule_selected_index:
            return render_template('login.html', status=999, token='', rule=_rule_selected)
        
        if _status == 200:
            session['login'] = request.form['username']
            session['time'] = calendar.timegm(time.gmtime()) + int(cfg['login_timeout'])
            session['token'] = _token
            session['type'] = _rule_selected
            return render_template('login.html', status=_status, token=_token)
        
    return render_template('login.html', status=_status, token=_token)


@routes.route('/register', methods=['GET', 'POST'])
def register():
    username = None
    password = None
    user_agreement_checked = None
        
        
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_agreement_checked = request.form['user_agreement']
        
        validate_username = is_valid_username(username)
        
        if validate_username != '':
            return render_template('register.html', status=400, _error=validate_username)
        
        validate_pwd = is_valid_password(password)
        
        if validate_pwd != '':
            return render_template('register.html', status=400, _error=validate_pwd)
        
        if username != None and password != None and user_agreement_checked == 'on':
            print('reg!!')
            user_obj = User().sign_up()
            user_obj.execute(username, password)   
            _status = user_obj.status_code
            if _status == 200:
                return render_template('register.html', status=_status)
  
    return render_template('register.html')


@routes.route('/')
def home():
    return redirect('/home')

@routes.route('/home', methods=['GET', 'POST'])
def home_general():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule == 'Пользователь':
        return render_template('userarea.html', login=session.get('login'), rule=rule)
    else:
        return render_template('example/home.html')

@routes.route('/logout', methods=['GET', 'POST'])
def logout():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    user_obj = User().sign_out()
    user_obj.execute(session.get('token'))
    
    session.pop('time', None) 
    session.pop('login', None) 
    session.pop('token', None) 
    session.pop('type', None) 
    
    return redirect(url_for('.login'))

def get_rule_by_value(value: str):
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()

        # Используем параметризованный запрос
        cursor.execute("SELECT id FROM rules WHERE name=%s", (value,))

        row = cursor.fetchone()

        # Проверяем, есть ли результат
        if row:
            rule_id = int(row[0])
            return rule_id
        else:
            # Если не найдено, можно вернуть, например, None
            return 1
    finally:
        db_connection.close()

def get_id_by_login():
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute("SELECT id FROM users WHERE username=%s", (session.get('login'),))
        row = cursor.fetchone()
        if row:
            rule_id = int(row[0])
            return rule_id
        else:
            return -1
    finally:
        db_connection.close()



@routes.route('/my_tickets')
def my_tickets():
    issues = []
    
    
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule == 'Пользователь':
        user_id = get_id_by_login()
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM issues WHERE user_id = %s', (user_id,))
            row = cursor.fetchall()      
        finally:
            db_connection.close()
        
        for rows in row:
            issue_status = 'В работе'
            issue_color = 'danger'
            if rows[8] == 0:
                issue_color = 'danger'
                issue_status = 'В работе'
            elif rows[8] == 1:
                issue_color = 'success'
                issue_status = 'Решено'
            
            issue_date = datetime.fromtimestamp(int(rows[5])).strftime('%Y-%m-%d %H:%M:%S')
            issue_date_update = datetime.fromtimestamp(int(rows[6])).strftime('%Y-%m-%d %H:%M:%S')
            
            issue = [str(rows[0]), issue_date, issue_date_update, str(rows[2]), issue_status, issue_color]
            issues.append(issue)


        return render_template('mytickets.html', login=session.get('login'), rule=rule, tickets=issues)

@routes.route('/add_ticket', methods=['GET', 'POST'])
def addticket():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule == 'Пользователь':
        if request.method == 'POST':
            login = session.get('login')
            time_created = calendar.timegm(time.gmtime())
            desc = request.form['desc_ticket']
            text = request.form['text_ticket']
            
            user_obj = Report().create()
            user_obj.execute(session.get('token'), desc, text, 'null')

            
            
            print(f'Попытка создания заявки:\nLogin:{login}\nTime:{time_created}\nDescription:{desc}\nText:{text}\nStatus: {user_obj.status_code}')
            
        return render_template('addticket.html', login=session.get('login'), rule=rule)