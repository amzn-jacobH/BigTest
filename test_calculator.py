import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)
        result = self.calc.add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)
        result = self.calc.subtract(1, 1)
        self.assertEqual(result, 0)
        result = self.calc.subtract(0, 5)
        self.assertEqual(result, -5)

    def test_multiply(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
        result = self.calc.multiply(-2, 3)
        self.assertEqual(result, -6)
        result = self.calc.multiply(0, 5)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)
        result = self.calc.divide(0, 5)
        self.assertEqual(result, 0)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()