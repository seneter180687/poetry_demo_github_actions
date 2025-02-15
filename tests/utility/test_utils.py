from src.utility.utils import addition
from src.config.conf import num1, num2

def test_addition():
    actual_result = addition(num1, num2)
    assert actual_result == num1 + num2