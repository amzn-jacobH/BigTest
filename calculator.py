class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
            
        Raises:
            TypeError: If inputs are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Result of a - b
            
        Raises:
            TypeError: If inputs are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
            
        Raises:
            TypeError: If inputs are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        return a * b

    def divide(self, a, b):
        """Divide a by b.
        
        Args:
            a (int/float): Numerator
            b (int/float): Denominator
            
        Returns:
            float: Result of a / b
            
        Raises:
            TypeError: If inputs are not numbers
            ValueError: If attempting to divide by zero
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b