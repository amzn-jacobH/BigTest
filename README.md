# Calculator Application with Unit Tests

This is a simple calculator application that demonstrates unit testing in Python.

## Features
- Basic arithmetic operations (add, subtract, multiply, divide)
- Comprehensive unit tests for each operation
- Error handling for division by zero

## Running Tests
To run the tests, execute:
```bash
python -m unittest test_calculator.py
```

## Test Cases
The test suite includes:
- Testing basic arithmetic operations
- Testing with negative numbers
- Testing with zero
- Testing edge cases (like division by zero)
- Multiple assertions per test to ensure thorough coverage

### Detailed Test Cases
1. Addition:
   - Positive numbers: 3 + 5 = 8
   - Negative and positive: -1 + 1 = 0
   - Zero: 0 + 0 = 0

2. Subtraction:
   - Positive numbers: 5 - 3 = 2
   - Equal numbers: 1 - 1 = 0
   - Subtracting from zero: 0 - 5 = -5

3. Multiplication:
   - Positive numbers: 3 * 5 = 15
   - Negative and positive: -2 * 3 = -6
   - Zero: 0 * 5 = 0

4. Division:
   - Whole number result: 6 / 2 = 3
   - Fractional result: 5 / 2 = 2.5
   - Zero as numerator: 0 / 5 = 0
   - Division by zero: Raises ValueError

## Usage Example
```python
calc = Calculator()
result = calc.add(5, 3)  # returns 8
result = calc.divide(6, 2)  # returns 3
```

## Best Practices Demonstrated
1. Use of setUp method to create a fresh calculator instance for each test
2. Multiple assertions per test method to cover various scenarios
3. Testing of edge cases and error conditions
4. Clear and descriptive test method names
5. Use of appropriate assertion methods (assertEqual, assertRaises)
