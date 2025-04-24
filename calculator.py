class Calculator:
    """A simple calculator class that provides basic arithmetic operations."""
    
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
        """Divide x by y and return the result.
        
        Raises:
            ValueError: If attempting to divide by zero.
        """
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y