
from calculator import Calculator
import pytest


calculator = Calculator()


def test_addition():
    assert calculator.add(5, 5) == 10


def test_subtraction():
    assert calculator.subtract(10, 5) == 5


def test_multiplication():
    assert calculator.multiply(4, 5) == 20


def test_division():
    assert calculator.divide(20, 5) == 4


def test_division_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
