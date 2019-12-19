"""
Unit tests for the calculator library
"""

import Calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == Calculator.add(2, 2)

    def test_substraction(self):
        assert 2 == Calculator.substract(4, 2)
