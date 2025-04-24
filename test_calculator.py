import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    A test suite for the Calculator class.
    
    This class contains unit tests for all the arithmetic operations
    provided by the Calculator class, including edge cases and error handling.
    """

    def setUp(self):
        """
        Set up a fresh Calculator instance for each test.
        """
        self.calc = Calculator()
    
    def test_add(self):
        """
        Test the add method of the Calculator class.
        """
        self.assertEqual(self.calc.add(3, 5), 8, "Failed to add positive numbers")
        self.assertEqual(self.calc.add(-1, 1), 0, "Failed to add a negative and a positive number")
        self.assertEqual(self.calc.add(0, 0), 0, "Failed to add zeros")
        self.assertEqual(self.calc.add(-5, -7), -12, "Failed to add negative numbers")
    
    def test_subtract(self):
        """
        Test the subtract method of the Calculator class.
        """
        self.assertEqual(self.calc.subtract(5, 3), 2, "Failed to subtract positive numbers")
        self.assertEqual(self.calc.subtract(1, 1), 0, "Failed to subtract equal numbers")
        self.assertEqual(self.calc.subtract(0, 5), -5, "Failed to subtract from zero")
        self.assertEqual(self.calc.subtract(-3, -5), 2, "Failed to subtract negative numbers")
    
    def test_multiply(self):
        """
        Test the multiply method of the Calculator class.
        """
        self.assertEqual(self.calc.multiply(3, 5), 15, "Failed to multiply positive numbers")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "Failed to multiply a negative and a positive number")
        self.assertEqual(self.calc.multiply(0, 5), 0, "Failed to multiply by zero")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "Failed to multiply negative numbers")
    
    def test_divide(self):
        """
        Test the divide method of the Calculator class.
        """
        self.assertEqual(self.calc.divide(6, 2), 3, "Failed to divide with whole number result")
        self.assertEqual(self.calc.divide(5, 2), 2.5, "Failed to divide with fractional result")
        self.assertEqual(self.calc.divide(0, 5), 0, "Failed to divide zero")
        self.assertEqual(self.calc.divide(-6, 2), -3, "Failed to divide with negative dividend")
        self.assertEqual(self.calc.divide(6, -2), -3, "Failed to divide with negative divisor")
        
        with self.assertRaises(ValueError, msg="Failed to raise ValueError on division by zero"):
            self.calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()