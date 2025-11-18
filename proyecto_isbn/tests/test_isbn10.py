import pytest
from src.isbn import is_valid_isbn10

def test_valid_isbn10():
    assert is_valid_isbn10("0-306-40615-2")
    assert is_valid_isbn10("0-8044-2957-X")

def test_invalid_len():
    assert not is_valid_isbn10("123456789")

def test_invalid_chars():
    assert not is_valid_isbn10("ABC6406152")
