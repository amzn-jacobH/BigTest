class Calculator:
    def add(self, x, y):
        """Add two numbers"""
        return x + y

    def subtract(self, x, y):
        """Subtract two numbers"""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers"""
        return x * y

    def divide(self, x, y):
        """Divide two numbers"""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y