import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-2, -3)
        self.assertEqual(result, -5)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        result = self.calc.subtract(-5, -3)
        self.assertEqual(result, -2)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        result = self.calc.multiply(4, 5)
        self.assertEqual(result, 20)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        result = self.calc.multiply(-3, -4)
        self.assertEqual(result, 12)
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        result = self.calc.divide(-12, -3)
        self.assertEqual(result, 4)
    
    def test_divide_by_zero(self):
        """Test division by zero raises an exception."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()