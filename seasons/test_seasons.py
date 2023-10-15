from seasons import parse_date
import pytest
from datetime import date

def test_parse_date_valid():
    input_str = "2023-10-15"
    result = parse_date(input_str)
    expected = date(2023, 10, 15)
    assert result == expected

def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("Hello")

if __name__ == "__main__":
    pytest.main()
