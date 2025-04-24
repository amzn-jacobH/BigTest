import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 5), 15)
        self.assertEqual(self.calculator.multiply(-2, 3), -6)
        self.assertEqual(self.calculator.multiply(-2, -2), 4)
    
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.divide(-6, 2), -3)
        self.assertEqual(self.calculator.divide(0, 5), 0)
        
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()