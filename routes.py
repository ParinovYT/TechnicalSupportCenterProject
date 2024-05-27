import calendar
from datetime import datetime
import json
import time
from src.config import Config
from imports import Blueprint, redirect, render_template, request, User, Report, MySqlBase, TemplateIssue, session, url_for, is_valid_password, is_valid_username

routes = Blueprint('routes', __name__)

def get_users():
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute("SELECT username FROM users")
        row = cursor.fetchall()
        return row
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

def get_login_by_id(id):
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute("SELECT username FROM users WHERE id=%s", (id,))
        row = cursor.fetchone()
        if row:
            rule_id = str(row[0])
            return rule_id
        else:
            return ''
    finally:
        db_connection.close()


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

def get_stats():
    stats = []
    
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM issues")
        tickets_all = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM users")
        users_all = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM issues WHERE status = 0")
        tickets_work = cursor.fetchone()[0]
        
        tickets_closed = tickets_all - tickets_work
        stats = [tickets_closed, tickets_work, users_all]
        return stats
    finally:
        db_connection.close()


def get_all_tickets():
    issues = [] 
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute('SELECT * FROM issues')
        row = cursor.fetchall()      
    finally:
        db_connection.close()    
        for rows in row:
            issue_status = 'В работе'
            issue_color = 'danger'
            
            if rows[8] == 0:
                issue_color = 'info'
                issue_status = 'Открыто'
            elif rows[8] == 1:
                issue_color = 'success'
                issue_status = 'Решено'
            elif rows[8] == 2:
                issue_color = 'danger'
                issue_status = 'В работе'
            elif rows[8] == 3:
                issue_color = 'warning'
                issue_status = 'Закрыт'
                
            issue_date = datetime.fromtimestamp(int(rows[5])).strftime('%Y-%m-%d %H:%M:%S')
            issue_date_update = datetime.fromtimestamp(int(rows[6])).strftime('%Y-%m-%d %H:%M:%S')  
            issue = [str(rows[0]), issue_date, issue_date_update, str(rows[2]), issue_status, issue_color, get_login_by_id(rows[1])]
            issues.append(issue)


    return issues

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if checkLogin() == True:
        return redirect(url_for('.home_general')) 
    
    _status = 0
    _token = 0
    _rule_selected = 0
    _rule_selected_index = 0
    block_login = 0
    
    
    if request.method == 'POST':
        block_login = 0
        user_obj = User().sign_in()
        user_obj.execute(request.form['username'], request.form['password'], int(Config.get('login_timeout')))  
        _status = user_obj.status_code
        _token = user_obj.get_token 

        _rule_selected = request.form['rule'] 
        if _rule_selected == 'Пользователь':
            _rule_selected_index = 4
        if _rule_selected == 'Сотрудник':
            _rule_selected_index = 3
        if _rule_selected == 'Администратор':
            _rule_selected_index = 2   
             
        if get_rule_by_login(request.form['username']) != _rule_selected_index:
            if get_rule_by_login(request.form['username']) != 2 or get_rule_by_login(request.form['username']) != 3 and _rule_selected_index != 4:      
                block_login = 1
        
        
        
        if _status == 200:
            if block_login == 1:
                return render_template('login.html', status=999, token='', rule=_rule_selected)
            
            session['login'] = request.form['username']
            session['time'] = calendar.timegm(time.gmtime()) + int(Config.get('login_timeout'))
            session['token'] = _token
            session['type'] = _rule_selected
            return redirect(url_for('.home_general')) 
            #return render_template('login.html', status=_status, token=_token)
        
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
            user_obj = User().sign_up()
            user_obj.execute(username, password)   
            _status = user_obj.status_code
            if _status == 200:
                return render_template('register.html', status=_status)
            elif _status == 409:
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
        __obj = TemplateIssue()
        obj = __obj.get()
        obj.execute()
        obj.status_code   
        
        respone=obj.response
        print(respone)
        
        text = json.loads(respone)      
        print(f"Грузим-грузим  - {text}")
        
        return render_template('userarea.html', login=session.get('login'), rule=rule, template_issueses=text)
    elif rule == 'Администратор':
        stats = get_stats()
        issues = get_all_tickets()
        return render_template('admin/adminarea.html', login=session.get('login'), rule=rule, tickets_work=stats[1], tickets_done=stats[0], all_useers=stats[2], tickets=issues)

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

@routes.route('/users')
def users():
    array = []
    
    
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule != 'Пользователь':
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM users')
            row = cursor.fetchall()      
        finally:
            db_connection.close()
        
        for rows in row:
            registration_date = datetime.fromtimestamp(int(rows[3])).strftime('%Y-%m-%d %H:%M:%S')
            _rule = None
            __rule = rows[4]
            
            if __rule == 4:
                _rule = 'Пользователь'
            elif __rule == 3:
                _rule = 'Сотрудник'
            elif __rule == 2:
                _rule = 'Администратор' 
            elif __rule == 1:
                _rule = 'Заблокирован'  
                            
            _str = [str(rows[0]), str(rows[1]), registration_date, _rule]
            array.append(_str)    
            
        return render_template('admin/users.html', login=session.get('login'), rule=rule, users=array)

@routes.route('/my_tickets')
def my_tickets():
    issues = []
    
    
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule != 'Пользователь':
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM issues')
            row = cursor.fetchall()      
        finally:
            db_connection.close()
        
        for rows in row:
            issue_status = 'В работе'
            issue_color = 'danger'
            if rows[8] == 0:
                issue_color = 'info'
                issue_status = 'Открыто'
            elif rows[8] == 1:
                issue_color = 'success'
                issue_status = 'Решено'
            elif rows[8] == 2:
                issue_color = 'danger'
                issue_status = 'Есть ответ'
            elif rows[8] == 3:
                issue_color = 'warning'
                issue_status = 'Закрыта'
            elif rows[8] == 4:
                issue_color = 'dark'
                issue_status = 'Ждем ответа'        
                
            issue_date = datetime.fromtimestamp(int(rows[5])).strftime('%Y-%m-%d %H:%M:%S')
            issue_date_update = datetime.fromtimestamp(int(rows[6])).strftime('%Y-%m-%d %H:%M:%S')
            
            issue = [str(rows[0]), issue_date, issue_date_update, str(rows[2]), issue_status, issue_color, get_login_by_id(rows[1]), str(rows[9])]
            issues.append(issue)    
            
        return render_template('mytickets.html', login=session.get('login'), drawing_creator_ticket=True,rule=rule, tickets=issues)
    
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
                issue_color = 'info'
                issue_status = 'Открыто'
            elif rows[8] == 1:
                issue_color = 'success'
                issue_status = 'Решено'
            elif rows[8] == 2:
                issue_color = 'danger'
                issue_status = 'В работе'
            elif rows[8] == 3:
                issue_color = 'warning'
                issue_status = 'Закрыта'
            elif rows[8] == 4:
                issue_color = 'dark'
                issue_status = 'Есть ответ'    
            issue_date = datetime.fromtimestamp(int(rows[5])).strftime('%Y-%m-%d %H:%M:%S')
            issue_date_update = datetime.fromtimestamp(int(rows[6])).strftime('%Y-%m-%d %H:%M:%S')
            
            issue = [str(rows[0]), issue_date, issue_date_update, str(rows[2]), issue_status, issue_color]
            issues.append(issue)


        return render_template('mytickets.html', drawing_creator_ticket=False, login=session.get('login'), rule=rule, tickets=issues)

@routes.route('/add_ticket', methods=['GET', 'POST'])
def addticket():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    devices_ = []
    
    db_connection = MySqlBase().connection()
    db_connection.open()
    if request.method == 'GET':
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM devices')
            devices__ = cursor.fetchall()
            for devices___ in devices__:  
                if devices___[1] == 'null':
                    continue
                devices_.append(devices___)    
        finally:
            db_connection.close()    
    
    if rule == 'Пользователь':
        if request.method == 'POST':
            _create = request.form['create'] 
            login = session.get('login')
            time_created = calendar.timegm(time.gmtime())
            desc = request.form['desc_ticket']
            text = request.form['text_ticket']
            
            floor = request.form['floor']  
            office = request.form['office']  
            info_device = request.form['device_name']  
            info_device_id = 'null'
        
            
            print(f'once add info {_create}')           
            
            if _create == "true":
                if floor:
                    floor_text = str(floor)
                else:
                    floor_text = 'Не указан'

                if office:
                    office_text = str(office)
                else:
                    office_text = 'Не указан'

                if info_device == 'none':
                    info_device_text = 'нет'
                else:
                    info_device_text = f'<br>{info_device}'
                    devID = info_device.split("-")[-1].strip()
                    devID = devID.split("|")[0].replace(" ", "")
                    info_device_id = devID
                    
                comment_info = {'sender': 'system', 'text': f'<br>Дополнительная информация о заявке:<br>Этаж: {floor_text}<br>Кабинет: {office_text}<br>Проблемное устройство: {info_device_text}'}

            if _create == "true":        
                once_comment = [comment_info, {"sender": "user", "text": text}]
            else:
                once_comment = [{"sender": "user", "text": text}]
            
                
            text = json.dumps(once_comment)
            
            user_obj = Report().create()
            user_obj.execute(session.get('token'), desc, text, info_device_id)

            
            
            print(f'Попытка создания заявки:\nLogin:{login}\nTime:{time_created}\nDescription:{desc}\nText:{text}\nStatus: {user_obj.status_code}')
      
        return render_template('addticket.html', login=session.get('login'), rule=rule, devices=devices_)

@routes.route('/add_comment', methods=['POST'])
def add_comment():
    if checkLogin() == False:
        return redirect(url_for('.login'))    
    comments_data = []
    ticket_id = request.form['ticket_id']  # Получаем ticket_id
    sender = request.form['sender']  # Получаем отправителя
    text = request.form['text']  # Получаем текст комментария
    worker = request.form['operator']  # Получаем оператора
    
    if worker == 'Не назначен':
        operator = f"Вам назначен оператор: {session.get('login')}"
        new_comment_worker = {'sender': 'system', 'text': operator}
    
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute('SELECT comments FROM issues WHERE id = %s', (ticket_id,))
        row = cursor.fetchone()
        comments_data = json.loads(row[0]) if row else [] 
        if worker == 'Не назначен':
            comments_data.append(new_comment_worker)
            cursor.execute("UPDATE issues SET worker = %s WHERE id = %s", (session.get('login'), ticket_id))         
            db_connection.connection.commit()
        new_comment = {'sender': sender, 'text': text}
        comments_data.append(new_comment)
        cursor.execute("UPDATE issues SET comments = %s, updated_at = %s WHERE id = %s", (json.dumps(comments_data), calendar.timegm(time.gmtime()), ticket_id))       
        if sender == 'system': 
             cursor.execute("UPDATE issues SET status = %s WHERE id = %s", ('3', ticket_id))       
        db_connection.connection.commit()
        if sender == 'user':
            cursor.execute("UPDATE issues SET status = %s WHERE id = %s", ('2', ticket_id))      
            db_connection.connection.commit()       
        if sender == 'support':
            cursor.execute("UPDATE issues SET status = %s WHERE id = %s", ('4', ticket_id))    
            db_connection.connection.commit()       
    finally:
        cursor.close()
        db_connection.close()
        
        
        
    return f'200'

@routes.route('/view_ticket', methods=['GET', 'POST'])
def viewticket():
    history_chat_ = []
    if checkLogin() == False:
        return redirect(url_for('.login'))
    rule = session.get('type')
    if rule == 'Администратор':
        if request.method == 'GET':
            ticket_id = request.args.get('ticket_id')
            db_connection = MySqlBase().connection()
            db_connection.open()
            try:
                cursor = db_connection.connection.cursor()
                cursor.execute('SELECT * FROM issues WHERE id = %s', (ticket_id,))
                row = cursor.fetchall()      
            finally:
                db_connection.close()
                
            for rows in row:        
                ticket_id = rows[0]
                comments = json.loads(rows[3])
                history_chat_.append({'comments': comments})
                _status_ticket = rows[8]
                _operator = rows[9]
                if _operator == '':
                    _operator = 'Не назначен'
                
        return render_template('viewticket.html', login=session.get('login'), rule=rule, id=ticket_id, history_chat=history_chat_, status_ticket=_status_ticket, operator=_operator)
    
    
    if rule == 'Пользователь':
        if request.method == 'GET':
            ticket_id = request.args.get('ticket_id')
            user_id = get_id_by_login()
            db_connection = MySqlBase().connection()
            db_connection.open()
            try:
                cursor = db_connection.connection.cursor()
                cursor.execute('SELECT * FROM issues WHERE user_id = %s AND id = %s', (user_id, ticket_id,))
                row = cursor.fetchall()      
            finally:
                db_connection.close()
            
            for rows in row:        
                ticket_id = rows[0]
                comments = json.loads(rows[3])
                history_chat_.append({'comments': comments})
                _status_ticket = rows[8]
                
            _operator = 'no_operator'
        return render_template('viewticket.html', login=session.get('login'), rule=rule, id=ticket_id, history_chat=history_chat_, status_ticket=_status_ticket, operator=_operator)    
    
@routes.route('/view_profile', methods=['GET', 'POST'])
def viewprofile():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        if not user_id:
            return redirect(url_for('.users'))
        else:
            session.pop('id_stored', None)   
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            row = cursor.fetchall()      
        finally:
            db_connection.close()
        for rows in row:
            username = rows[1]
            password = rows[2]
            __rule = rows[4]
            session['pwd_stored'] = password
            
            if __rule == 4:
                rule = 'Пользователь'
            elif __rule == 3:
                rule = 'Сотрудник'
            elif __rule == 2:
                rule = 'Администратор' 
            elif __rule == 1:
                rule = 'Заблокирован'  
       
    if request.method == 'POST':
        user_id = request.form['user_id']
        username = request.form['username']
        rule = request.form['urule']
        
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            if session.get('pwd_stored') != request.form['password']:
                cursor.execute("UPDATE users SET password = %s WHERE id = %s", (request.form['password'], user_id,))    
                db_connection.connection.commit()  
                
            if rule == 'Пользователь':
                rule = 4
            elif rule == 'Сотрудник':
                rule = 3
            elif rule == 'Администратор':
                rule = 2 
            elif rule == 'Заблокирован':
                rule = 1
                
            cursor.execute("UPDATE users SET username = %s, rule = %s WHERE id = %s", (username, rule, user_id,)) 
            session['id_stored'] = user_id
            db_connection.connection.commit()   
            session.pop('pwd_stored', None)                    
        finally:
            db_connection.close()
             
        return redirect(url_for('.viewprofile', user_id=session.get('id_stored'))) 
        #str(self._hash.sha(value))
        
    return render_template('admin/view_profile.html', login=session.get('login'), rule=session.get('type'), user_id=user_id, username=username, password=password, urule=rule, rules=['Пользователь', 'Сотрудник', 'Администратор', 'Заблокирован'])    


@routes.route('/inventory_list', methods=['GET', 'POST'])
def inventorylist():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    _devices = []
    db_connection = MySqlBase().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute('SELECT * FROM devices')
        row = cursor.fetchall()      
    finally:
        db_connection.close()
    
    for rows in row:
        if rows[1] == 'null':
            continue
    
        _devices.append(rows)      
    
    return render_template('admin/materials.html', login=session.get('login'), rule=session.get('type'), devices=_devices)    

@routes.route('/inventory_add', methods=['GET', 'POST'])
def inventoryadd():
    if checkLogin() == False:
        return redirect(url_for('.login'))
    if request.method == 'POST':
        inventory_number = request.form['inventory_number']
        inventory_name = request.form['inventory_name']
        inventory_date = request.form['inventory_date']
        inventory_floor = request.form['inventory_floor']
        inventory_office = request.form['inventory_office']
        inventory_type = request.form['inventory_type']
        inventory_responsible = request.form['inventory_responsible']
        
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
         
            insert_query = "INSERT INTO devices VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"
            params = (
               inventory_number, 
               inventory_name, 
               inventory_date, 
               inventory_floor, 
               inventory_office,
               inventory_type,
               inventory_responsible
            )
            cursor.execute(insert_query, params)
            db_connection.connection.commit()
            
        finally:
            db_connection.close()
    
    data = []
    row=get_users()
    for rows in row:
        data.append(rows[0])
        
    return render_template('admin/material_add.html', users=data, login=session.get('login'), rule=session.get('type'))    




@routes.route('/inventory_edit', methods=['GET', 'POST'])
def inventoryedit():
    if checkLogin() == False:
        return redirect(url_for('.login'))   
    if request.method == 'GET':
        has_only_del = request.args.get('delete')
        inv_number = request.args.get('inv_number')
        if has_only_del == 'true':
            session['inv_number'] = inv_number
            db_connection = MySqlBase().connection()
            db_connection.open()
            try:
                cursor = db_connection.connection.cursor()
                cursor.execute('DELETE FROM devices WHERE inventory_number = %s', (session.get('inv_number'),))
                db_connection.connection.commit()
            finally:
                db_connection.close()
            return redirect(url_for('.inventorylist'))     
        
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            cursor.execute('SELECT * FROM devices WHERE inventory_number = %s', (inv_number,))
            row_data = cursor.fetchall()      
        finally:
            db_connection.close()
        
        for data in row_data:
            inventory_number = data[1]
            inventory_name = data[2]
            inventory_date = data[3]
            inventory_floor = data[4]
            inventory_office = data[5]    
            inventory_type = data[6]
            inventory_responsible = data[7]       
     
    if request.method == 'POST':
        inventory_number = request.form['inventory_number']
        inventory_name = request.form['inventory_name']
        inventory_date = request.form['inventory_date']
        inventory_floor = request.form['inventory_floor']
        inventory_office = request.form['inventory_office']
        inventory_type = request.form['inventory_type']
        inventory_responsible = request.form['inventory_responsible']
        
        db_connection = MySqlBase().connection()
        db_connection.open()
        try:
            cursor = db_connection.connection.cursor()
            
            cursor.execute('DELETE FROM devices WHERE inventory_number = %s', (session.get('inv_number'),))
            db_connection.connection.commit()
            
            insert_query = "INSERT INTO devices VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"
            params = (
               inventory_number, 
               inventory_name, 
               inventory_date, 
               inventory_floor, 
               inventory_office,
               inventory_type,
               inventory_responsible
            )
            cursor.execute(insert_query, params)
            db_connection.connection.commit()
            
        finally:
            db_connection.close()
    
    data = []
    row=get_users()
    for rows in row:
        data.append(rows[0])
            
    return render_template('admin/material_edit.html', users=data, login=session.get('login'), rule=session.get('type'), inventory_number=inventory_number, inventory_name=inventory_name, inventory_date=inventory_date,inventory_floor=inventory_floor,inventory_office=inventory_office, inventory_type=inventory_type, inventory_responsible=inventory_responsible)    
