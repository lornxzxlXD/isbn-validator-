from src.isbn import is_valid_isbn13

def test_valid_isbn13():
    assert is_valid_isbn13("9780306406157")

def test_invalid_checksum():
    assert not is_valid_isbn13("9780306406158")
