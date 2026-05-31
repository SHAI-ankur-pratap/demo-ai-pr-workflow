import pytest
import math
from src.app import add, subtract, multiply, divide, power, modulo, square_root, logarithm, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 3) == 7

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_power():
    assert power(2, 8) == 256.0

def test_modulo():
    assert modulo(10, 3) == 1.0

def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(10, 0)

def test_square_root():
    assert square_root(16) == 4.0
    assert square_root(0) == 0.0
    assert square_root(2) == pytest.approx(math.sqrt(2))

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        square_root(-1)

def test_logarithm():
    assert logarithm(100, 10) == pytest.approx(2.0)
    assert logarithm(math.e) == pytest.approx(1.0)
    assert logarithm(8, 2) == pytest.approx(3.0)

def test_logarithm_invalid():
    with pytest.raises(ValueError, match="Cannot take log of zero or negative number"):
        logarithm(0)
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
        logarithm(10, 1)

def test_calculate_sqrt():
    assert calculate("sqrt", 16) == 4.0

def test_calculate_log():
    assert calculate("log", 100, 10) == pytest.approx(2.0)

def test_calculate_unknown():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate("cube", 3, 0)
