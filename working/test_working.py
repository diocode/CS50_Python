from working import convert
import pytest

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") =="09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("19:60 AM to 50:60 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9 AM - 5 PM")

def test_times():
    with pytest.raises(ValueError):
        convert("19:60 AM to 50:60 PM")
        convert("13 AM to 17 PM")

def test_to():
    with pytest.raises(ValueError):
        convert("9 AM  5 PM")