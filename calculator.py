class Calculator:
    def add(self, a: float, b: float) -> float:
        """Add two numbers together."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract the second number from the first."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers together."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide the first number by the second.
        
        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b