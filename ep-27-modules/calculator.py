# A simple calculator module

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b
