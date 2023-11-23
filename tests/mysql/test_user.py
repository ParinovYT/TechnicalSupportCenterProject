import time

from src.core.classes.mysql import MySql

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

def test_create_rule():
    db_connection = MySql().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor(prepared=True,)
        insert_query = "INSERT INTO rules VALUES (NULL, %s);"
        params = ('user',)

        cursor.execute(insert_query, params)
        db_connection.connection.commit()

        print("Rule Insert successful.")
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
            return None
    finally:
        db_connection.close()

def test_create_user():
    db_connection = MySql().connection()
    db_connection.open()
    try:
        cursor = db_connection.connection.cursor(prepared=True,)
        insert_query = "INSERT INTO `users` VALUES (NULL, %s, %s, %s);"
        current_time = int(time.time())
        params = ('user1', current_time, get_rule_by_value('user'))

        cursor.execute(insert_query, params)
        db_connection.connection.commit()  # Важно применить изменения в базе данных

        print("User Insert successful.")
    finally:
        db_connection.close()