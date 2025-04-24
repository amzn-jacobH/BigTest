class Calculator:
    def add(self, x, y):
        """Add two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtract y from x."""
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers."""
        return x * y

    def divide(self, x, y):
        """Divide x by y."""
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y