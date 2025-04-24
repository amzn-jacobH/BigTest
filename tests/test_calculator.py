import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test cases."""
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation."""
        result = self.calc.add(2, 2)
        self.assertEqual(result, 4)

    def test_addition_negative(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-3, 7)
        self.assertEqual(result, 4)

    def test_addition_float(self):
        """Test addition with floating point numbers."""
        result = self.calc.add(1.5, 2.7)
        self.assertAlmostEqual(result, 4.2)

    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_subtraction_negative(self):
        """Test subtraction with negative numbers."""
        result = self.calc.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_subtraction_float(self):
        """Test subtraction with floating point numbers."""
        result = self.calc.subtract(5.5, 2.2)
        self.assertAlmostEqual(result, 3.3)

    def test_multiplication(self):
        """Test multiplication operation."""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiplication_zero(self):
        """Test multiplication with zero."""
        result = self.calc.multiply(5, 0)
        self.assertEqual(result, 0)

    def test_multiplication_negative(self):
        """Test multiplication with negative numbers."""
        result = self.calc.multiply(-3, 4)
        self.assertEqual(result, -12)

    def test_division(self):
        """Test division operation."""
        result = self.calc.divide(8, 2)
        self.assertEqual(result, 4)

    def test_division_float(self):
        """Test division resulting in float."""
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)

    def test_division_negative(self):
        """Test division with negative numbers."""
        result = self.calc.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_division_by_zero(self):
        """Test division by zero raises exception."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()