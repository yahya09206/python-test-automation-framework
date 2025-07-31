from my_first_test import add, subtract

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -5) == -6

def test_subtract_numbers():
    assert subtract(10, 4) == 6