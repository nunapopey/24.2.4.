# test.py
import pytest
from calc import Calculator    # Не забудьте импортировать ваш класс калькулятора

class TestCalc:
    def setup_method(self):
        self.calc = Calculator()  # Инициализация объекта калькулятора

    def test_multiply_success(self):
        assert self.calc.multiply(2, 4) == 8

    def test_division_success(self):
        assert self.calc.divide(16, 4) == 4

    def test_subtraction_success(self):
        assert self.calc.subtract(10, 3) == 7

    def test_adding_success(self):
        assert self.calc.add(4, 6) == 10

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(1, 0)