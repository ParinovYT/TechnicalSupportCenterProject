import re

from src.core.classes.validation import ValidationBase


class Validation(ValidationBase):
    def is_username(self, value: str) -> bool:
        """
        Can only be present: hyphen, underscore, Latin characters only
        """
        return bool(re.compile(r'^[A-Za-z0-9_-]{2,256}$').match(value))

    def is_password(self, value: str) -> bool:
        """
        Minimum password requirements: one upper case character, one lower case character, one digit, one special character, length from 8 to 64 characters.
        """
        return bool(re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W]).{8,64}$').match(value))
