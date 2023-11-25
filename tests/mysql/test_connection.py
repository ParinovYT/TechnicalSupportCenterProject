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