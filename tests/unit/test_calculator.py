import pytest

from src.calculator import add, subtract, multiply, divide


class TestBasicOperations:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2


class TestMultiplyDivideWithValidation:
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)

    def test_divide_input_validation(self):
        """Test divide rejects division by zero."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)
