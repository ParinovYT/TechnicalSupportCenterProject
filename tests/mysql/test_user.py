from src.core.classes.models.user import ModelUser
from src.core.classes.mysql.queries import MySqlQuery
from src.core.database.authentication.sign_up import SignUp
from src.core.classes.mysql import MySql
import time
from http.client import OK

def test_connection():
    db_connection = MySql().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor()
        cursor.execute('SELECT 1;')

        rows = cursor.fetchall()

        for row in rows:
            assert row[0] == 1, row[0]
    finally:
        db_connection.close()

def get_rule_by_value(value: str):
    db_connection = MySql().connection()
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

def test_create_user():
    MySQl = MySql()
    MySQlQueries = MySQl.queries()
    db_connection = MySQl.connection()
    db_connection.open()

    try:
        model = ModelUser()
        model.username = 'user1'
        model.password = 'password'
        model.created_at = int(time.time())
        model.rule = get_rule_by_value('L1')
        model.admin = False

        # Import Authentication inside the function to break the circular dependency
        from src.core.database.authentication import Authentication

        query: MySQlQueries = Authentication(db_connection).sign_up(model)
        query.execute()
        assert query.status_code == OK
    finally:
        db_connection.close()