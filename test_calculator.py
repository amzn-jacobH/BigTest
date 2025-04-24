import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(self.calc.add(1e15, 1), 1000000000000001)
        self.assertAlmostEqual(self.calc.add(1e-8, 1e-9), 1.1e-8, places=10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
        self.assertEqual(self.calc.subtract(1e15, 1), 999999999999999)
        self.assertAlmostEqual(self.calc.subtract(1e-8, 1e-9), 9e-9, places=10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01, places=7)
        self.assertEqual(self.calc.multiply(1e15, 2), 2e15)
        self.assertAlmostEqual(self.calc.multiply(1e-8, 1e-8), 1e-16, places=17)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)
        self.assertEqual(self.calc.divide(1e15, 1e3), 1e12)
        self.assertAlmostEqual(self.calc.divide(1e-8, 1e8), 1e-16, places=17)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_type_checking(self):
        with self.assertRaises(TypeError):
            self.calc.add("2", 3)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, "3")
        with self.assertRaises(TypeError):
            self.calc.multiply("2", "3")
        with self.assertRaises(TypeError):
            self.calc.divide(6, "3")

    def test_floating_point_precision(self):
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=6)

if __name__ == '__main__':
    unittest.main()