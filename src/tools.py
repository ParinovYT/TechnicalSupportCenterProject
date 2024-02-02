import random
import re
import secrets
import string

def generate_password():
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W]).{8,64}$'

    while True:
        password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in
                           range(random.randint(8, 64)))
        if re.match(pattern, password):
            return password

def is_valid_password(password):
    errors = []
    if len(password) < 8 or len(password) > 64:
        errors.append('-&nbsp;должен содержать от 8 до 64 символов')
    
    if not re.search('[A-Z]', password):
        errors.append('-&nbsp;должен содержать хотя бы одну заглавную букву (от A до Z)')
        
    if not re.search('[a-z]', password):
        errors.append('-&nbsp;должен содержать хотя бы одну строчную букву (от a до z)')

    if not re.search('\d', password):
        errors.append('-&nbsp;должен содержать хотя бы одну цифру (от 0 до 9)')

    if not re.search('[\W]', password):
        errors.append('-&nbsp;должен содержать хотя бы один специальный символ (не буквенно-цифровой символ)')

    if errors:
        return 'Пароль не соответствует требованиям:<br>' + '<br>'.join(errors)
    else:
        return ''
    
def is_valid_username(username):
    errors = []

    if len(username) < 4 or len(username) > 64:
        errors.append('-&nbsp;должен содержать от 4 до 64 символов')

    if re.search('\W', username):
        errors.append('-&nbsp;не должен содержать специальные символы')

    if ' ' in username:
        errors.append('-&nbsp;не должен содержать пробелы')

    if errors:
        return 'Логин не соответствует требованиям:<br>' + '<br>'.join(errors)
    else:
        return ''