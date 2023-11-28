from src.core.database.report.create import Create
from src.core.classes.mysql.queries import MySqlQuery
from src.core.classes.models.issue import ModelIssue
from src.core.database.connection import Connection


class Report:
    def __init__(self, connection: Connection):
        self.__connection: Connection = connection
    
    def create(self, model_issue: ModelIssue):
        obj: MySqlQuery = Create(self.__connection, model_issue)
        return obj