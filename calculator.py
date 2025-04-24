class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""
    
    def add(self, x, y):
        """Add two numbers and return the result."""
        return x + y
    
    def subtract(self, x, y):
        """Subtract the second number from the first and return the result."""
        return x - y
    
    def multiply(self, x, y):
        """Multiply two numbers and return the result."""
        return x * y
    
    def divide(self, x, y):
        """Divide the first number by the second and return the result.
        
        Raises:
            ValueError: If attempting to divide by zero.
        """
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y