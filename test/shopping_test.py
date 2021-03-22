



# import the code we want to test
from app.shopping import format_usd


def test_format_usd():
    #assert 2 == 4
    #assert 2 == 2
    assert format_usd(9.5) == "$9.50"
    #assert format_usd(100000000) == "$9.50"
