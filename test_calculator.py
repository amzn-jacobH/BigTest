import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixture by creating a calculator instance."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition function."""
        self.assertEqual(self.calc.add(4, 7), 11)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        """Test subtraction function."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Test multiplication function."""
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
    
    def test_divide(self):
        """Test division function."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()