# Calculator Application

This is a simple calculator application with unit tests.

## Features

The calculator supports the following operations:
- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## Setup

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running Tests

The application includes a comprehensive set of unit tests. To run the tests, use one of the following commands in the root directory of the project:

1. Using unittest:
   ```
   python -m unittest discover tests
   ```

2. Using pytest:
   ```
   pytest tests
   ```

The tests cover all the basic operations (add, subtract, multiply, divide) and include a test for division by zero.

## Project Structure

- `calculator/calculator.py`: Contains the main Calculator class with all operations
- `tests/test_calculator.py`: Contains the unit tests for the Calculator class
- `requirements.txt`: Lists the project dependencies (pytest)

## Contributing

Feel free to contribute to this project by adding more features or improving the existing ones. Make sure to add appropriate unit tests for any new functionality.
