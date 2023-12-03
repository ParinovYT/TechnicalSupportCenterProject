from http.client import INTERNAL_SERVER_ERROR, OK
import json
from src.core.database.connection import Connection
from src.core.classes.mysql.queries import MySqlQuery


class TemplateIssue(MySqlQuery):
    def __init__(self, connection: Connection):
        super().__init__(connection)

    @property
    def get(self) -> str:
        return self._response

    @property
    def status_code(self) -> int:
        return self._status_code

    def execute(self) -> None:
        try:
            cursor = self._connection.connection.cursor()

            cursor.execute("""
            SELECT template_issueses.id,
            ci.value as category,
            issue,
            solution
            FROM template_issueses
            JOIN technical_support.category_issue ci
            on ci.id = template_issueses.category_id
            """)

            rows = cursor.fetchall()

            result_data = {"categories": []}

            current_category = None
            category_data = {"category": "", "list": []}

            for row in rows:
                category = row[1]  # Assuming category is at index 1 in the result
                issue_id = row[0]  # Assuming issue_id is at index 0 in the result
                issue = row[2]  # Assuming issue is at index 2 in the result
                solution = row[3]  # Assuming solution is at index 3 in the result

                if current_category != category:
                    if category_data["category"]:
                        result_data["categories"].append(category_data)

                    current_category = category
                    category_data = {"category": category, "list": []}

                category_data["list"].append({
                    "issue_id": issue_id,
                    "issue": issue,
                    "solution": solution
                })

            if category_data["category"]:
                result_data["categories"].append(category_data)

            self._response = json.dumps(result_data)
            self._status_code = OK

        except Exception as e:
            self._response = '{}'
            self._status_code = INTERNAL_SERVER_ERROR
            print(e)