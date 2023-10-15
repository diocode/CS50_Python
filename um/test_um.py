from um import count

def test_valid():
    assert count("um") == 1
    assert count("aumz") == 0
    assert count(" um ") == 1
    assert count("Um, you ok?") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, you ok?") == 1
