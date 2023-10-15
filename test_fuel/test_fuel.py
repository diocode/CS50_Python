import fuel
import pytest

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("2/4") == 50
    assert fuel.convert("4/4") == 100

    with pytest.raises(ValueError):
        fuel.convert("4/2")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")

    with pytest.raises(ValueError):
        fuel.convert("A/100")


def test_gauge():
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(75) == "75%"