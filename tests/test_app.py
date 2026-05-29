import pytest
from src.app import add, subtract, multiply, divide, power, modulo, calculate


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_power():
    assert power(2, 8) == 256.0
    assert power(3, 3) == 27.0
    assert power(5, 0) == 1.0


def test_modulo():
    assert modulo(10, 3) == 1.0
    assert modulo(7, 2) == 1.0
    assert modulo(9, 3) == 0.0


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot modulo by zero"):
        modulo(10, 0)


def test_calculate_dispatch():
    assert calculate("add", 1, 2) == 3
    assert calculate("multiply", 3, 4) == 12
    assert calculate("power", 2, 10) == 1024.0
    assert calculate("modulo", 10, 3) == 1.0


def test_calculate_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        calculate("sqrt", 16, 0)
