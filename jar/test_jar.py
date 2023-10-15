from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar("Hello")
    with pytest.raises(ValueError):
        Jar(-100)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(200)
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(183)
    assert jar.size == 193

    with pytest.raises(ValueError):
        jar.deposit(100)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(5)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(5)
