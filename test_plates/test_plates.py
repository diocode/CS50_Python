from plates import is_valid

def test_start():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False

def test_len():
    assert is_valid("C") == False
    assert is_valid("CS505050") == False
    assert is_valid("CCSSHHGG") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punctuation():
    assert is_valid("CS50.") == False
    assert is_valid("CS_50") == False
    assert is_valid("CSA 50") == False