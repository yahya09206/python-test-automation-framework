from day03_locate_by_tag_get_attr.get_elements_by_class_name import driver
from my_first_test import add, subtract, assertTitle

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -5) == -6

def test_subtract_numbers():
    assert subtract(10, 4) == 6

def test_title_name():
    title = driver.get("https://practice.cydeo.com")

    assert driver.title(title)