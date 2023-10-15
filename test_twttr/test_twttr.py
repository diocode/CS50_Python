from twttr import shorten

def test_vowels():
    assert shorten("this a test") == "ths  tst"
    assert shorten("A tesT thIs might BE") == " tsT ths mght B"

def test_novowels():
    assert shorten("FMTG lk") == "FMTG lk"
    assert shorten("ytrPtGH") == "ytrPtGH"

def test_punctuation():
    assert shorten("Hello, this is a test") == "Hll, ths s  tst?"
    assert shorten("..,,-") == "..,,-"

def test_notstr():
    assert shorten("123") == "123"
    assert shorten("") == ""