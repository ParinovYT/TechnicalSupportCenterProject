from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, OK
import time

from mysqlx import Error
from src.core.database.device import Device
from src.core.classes.report.base import ReportBase
from src.core.database.report import Report
from src.core.database.user_info import UserInfo


class Create(ReportBase):
    def __init__(self) -> None:
        super().__init__()
    
    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self, token: str, issue: str, inventory_number: str) -> None:
        MySQl = self._DB
        db_connection = MySQl.connection()
        MySQlQueries = MySQl.queries()
        query_user_info: MySQlQueries = UserInfo(db_connection)
        query_device: MySQlQueries = Device(db_connection, self._model_device).get_by_inventory_number()
        try:
            self._model_token.token = token

            db_connection.open()
            MySQlQueries = MySQl.queries()
            query_user_info: MySQlQueries = UserInfo(db_connection)

            query_user_info.execute(token = self._model_token.token)

            if query_user_info.status_code != OK:
                self._status_code = query_user_info.status_code
                return

            query_device.execute(inventory_number)

            if query_device.status_code != OK:
                self._status_code = query_device.status_code
                return

            self._model_issue.user_id = query_user_info.id
            self._model_issue.issue = issue
            self._model_issue.device_id = query_device.response.id #!!!РЕАЛИЗОВАТЬ КЛАСС Device В КОТОРОМ БУДЕТ БУДЕТ ИНФОРМАЦИЯ ОБ deivces ПО ЕГО inventory_number!!!
            self._model_issue.created_at = int(time.time())
            self._model_issue.updated_at = int(time.time())
            self._model_issue.line = 1
            self._model_issue.status = False

            query_sign_in: MySQlQueries = Report(db_connection).create(self._model_issue)
            query_sign_in.execute()
            self._status_code = query_sign_in.status_code
            return

        except ValueError:
            self._status_code = BAD_REQUEST

        except Error as e:
            print(e)
            self._status_code = INTERNAL_SERVER_ERROR

        finally:
            db_connection.close()