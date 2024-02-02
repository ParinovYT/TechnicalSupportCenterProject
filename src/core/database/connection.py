import os
import mysql.connector
from src.config import Config

from src.core.classes.mysql.connection import MySqlConnection


class Connection(MySqlConnection):
    def __init__(self):
        if Config.get['use_docker_db'] == True:
            self.__host = os.environ.get('DATABASE_HOST', 'localhost')
            self.__port = os.environ.get('DATABASE_PORT', '3306')
            self.__user = os.environ.get('DATABASE_USER', 'user')
            self.__password = os.environ.get('DATABASE_PASSWORD', 'userpassword')
            self.__database = os.environ.get('DATABASE_NAME', 'technical_support')
        else:
            self.__host = Config.get['db_host_without_docker']
            self.__port = Config.get['db_port_without_docker']
            self.__user = Config.get['db_user_without_docker']
            self.__password = Config.get['db_password_without_docker']
            self.__database = Config.get['db_database_without_docker']
            
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
