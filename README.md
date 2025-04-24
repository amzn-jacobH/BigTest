# Calculator Unit Tests

This project contains a simple calculator implementation with unit tests.

## Structure
- `calculator.py`: Contains the Calculator class implementation
- `test_calculator.py`: Contains the unit tests for the Calculator class

## Running Tests
To run the tests, use pytest:

```bash
pytest test_calculator.py
```

## Test Cases
The following test cases are implemented:

1. Addition
   - Regular addition
   - Adding negative numbers
   - Adding zeros

2. Subtraction
   - Regular subtraction
   - Subtracting equal numbers
   - Subtracting from zero

3. Multiplication
   - Regular multiplication
   - Multiplication with negative numbers
   - Multiplication with zero

4. Division
   - Regular division
   - Division with decimal results
   - Division with zero as numerator
   - Division by zero (error case)
