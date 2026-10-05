import pytest
from math_utils import *
def test_multiply():
    assert multiply(3, 4) == 12
def test_divide():
    assert divide(10, 2) == 5
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
#exercise 2
@pytest.mark.parametrize(
    "password,truth",[("pass12345", True),("pass1", False),("testingpassword", False)]
)
def test_valid_password(password,truth):
    assert validate_password(password) is truth
#exercise 3
@pytest.mark.parametrize(
    "n,expected",[(2, True),(3, False),(0, False),(-2, True),(7, False),]
)
def test_is_even(n, expected):
    assert is_even(n) == expected