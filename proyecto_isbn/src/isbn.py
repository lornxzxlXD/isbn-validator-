def normalize_isbn(s):
    if not s:
        return ""
    s = s.replace(" ", "").replace("-", "")
    if not all(c.isdigit() or c=='X' for c in s):
        return ""
    return s

def is_valid_isbn10(s):
    s = normalize_isbn(s)
    if len(s)!=10: return False
    if s[-1]=='X':
        digits = [10]
    else:
        if not s[-1].isdigit(): return False
        digits = [int(s[-1])]
    for c in s[:-1]:
        if not c.isdigit(): return False
    digits = [int(c) if c.isdigit() else 10 for c in s[:-1]] + digits
    total = sum((10-i)*digits[i] for i in range(10))
    return total % 11 == 0

def is_valid_isbn13(s):
    s = normalize_isbn(s)
    if len(s)!=13 or not s.isdigit(): return False
    total = sum((3 if i%2 else 1)*int(s[i]) for i in range(12))
    check = (10 - (total % 10)) % 10
    return check == int(s[12])

def detect_isbn(s):
    s = normalize_isbn(s)
    if len(s)==10 and is_valid_isbn10(s): return "ISBN-10"
    if len(s)==13 and is_valid_isbn13(s): return "ISBN-13"
    return "INVALID"
