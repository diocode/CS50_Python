from bank import value


def test_return_0():
    assert value("hello, it's me") == 0
    assert value("Hello Mark") == 0


def test_return_20():
    assert value("hi, it's me") == 20
    assert value("Hi there!") == 20


def test_return_100():
    assert value("Greetings Sir") == 100
    assert value("Fuck off") == 100
