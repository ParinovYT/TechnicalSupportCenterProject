import mysql.connector

from src.core.classes.mysql.connection import MySqlConnection


class Connection(MySqlConnection):
    def __init__(self):
        self.__host = 'localhost'
        self.__port = '3306'
        self.__user = 'user'
        self.__password = 'userpassword'
        self.__database = 'technical_support'
        self.connection = None

    def open(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.__host,
                port=self.__port,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            print("Connection opened successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
        else:
            print("No active connection to close.")
