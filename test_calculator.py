import pytest
from calculator import Calculator

calc = Calculator()


# ---- add ----
def test_add_positive():
    assert calc.add(2, 3) == 5


def test_add_negative():
    assert calc.add(-2, -3) == -5


def test_add_zero():
    assert calc.add(5, 0) == 5


# ---- minus ----
def test_minus_positive():
    assert calc.minus(5, 3) == 2


def test_minus_negative_result():
    assert calc.minus(3, 5) == -2


def test_minus_zero():
    assert calc.minus(5, 0) == 5


# ---- multiply ----
def test_multiply_positive():
    assert calc.multiply(4, 3) == 12


def test_multiply_by_zero():
    assert calc.multiply(5, 0) == 0


def test_multiply_negative():
    assert calc.multiply(-4, 3) == -12


# ---- divide ----
def test_divide_normal():
    assert calc.divide(10, 2) == 5


def test_divide_float():
    assert calc.divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5, 0)
