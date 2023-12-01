import hashlib

from src.core.classes.security import Security


def my_sha256_string(input_string: str, encoding='utf-8'):
    """
    Calculate SHA-256 hash for a given string.

    Args:
        input_string (str): The input string to hash.
        encoding (str): The encoding of the input string. Default is 'utf-8'.

    Returns:
        str: The SHA-256 hash as a hexadecimal string.
    """
    sha256_hash = hashlib.sha256(input_string.encode(encoding))
    return sha256_hash.hexdigest()


def my_sha256_bytes(input_bytes: bytes):
    """
    Calculate SHA-256 hash for a given bytes object.

    Args:
        input_bytes (bytes): The input bytes to hash.

    Returns:
        bytes: The SHA-256 hash as bytes.
    """
    sha256_hash = hashlib.sha256(input_bytes)
    return sha256_hash.digest()


def test_sha256():
    text: str = 'Hello'
    text2: bytes = b'Help'
    obj = Security().hash()
    assert obj.sha(text) == my_sha256_string(text)
    assert obj.sha(text2) == my_sha256_bytes(text2)
