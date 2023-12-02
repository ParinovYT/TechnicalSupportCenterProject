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