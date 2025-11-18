from src.isbn import normalize_isbn

def test_idempotencia():
    s = "978-0-306-40615-7"
    assert normalize_isbn(normalize_isbn(s)) == normalize_isbn(s)
