class Calculator:
    def add(self, x, y):
        """Add two numbers and return the result."""
        return x + y
    
    def subtract(self, x, y):
        """Subtract y from x and return the result."""
        return x - y
    
    def multiply(self, x, y):
        """Multiply two numbers and return the result."""
        return x * y
    
    def divide(self, x, y):
        """Divide x by y and return the result."""
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y