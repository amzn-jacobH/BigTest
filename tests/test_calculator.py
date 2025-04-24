import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation"""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test subtraction operation"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiplication(self):
        """Test multiplication operation"""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

if __name__ == '__main__':
    unittest.main()