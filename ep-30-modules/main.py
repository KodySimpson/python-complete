# Episode 22: Creating and Using Your Own Modules

# Modules are files containing Python code that can be imported and used in other programs.
# This episode focuses on creating your own modules and the different ways to import from them.

# Section 1: Understanding Modules

# A module is simply a Python file (.py) that contains functions, variables, or classes
# that you want to use in other programs.

# We have created a calculator module in 'calculator.py' with these functions:
# - add(a, b)
# - subtract(a, b) 
# - multiply(a, b)
# - divide(a, b)
# - power(a, b)

# Section 2: Method 1 - Import the Entire Module

# Import the entire calculator module
import calculator

print("=== Method 1: Import Entire Module ===")
print(calculator.PI)
print("5 + 3 =", calculator.add(5, 3))
print("10 - 4 =", calculator.subtract(10, 4))
print("6 * 7 =", calculator.multiply(6, 7))
print("15 / 3 =", calculator.divide(15, 3))
print("2 ^ 8 =", calculator.power(2, 8))

# Advantages of this method:
# - Clear where functions come from
# - No naming conflicts
# - Easy to see all available functions

# Section 3: Method 2 - Import Specific Functions

# Import only the functions you need
from calculator import add, multiply

print("\n=== Method 2: Import Specific Functions ===")
print("20 + 15 =", add(20, 15))
print("4 * 6 =", multiply(4, 6))

# Advantages of this method:
# - Shorter code (no module prefix needed)
# - Only import what you need
# - Cleaner function calls

# Section 4: Method 3 - Import with Aliases

# Import the entire module with a different name
import calculator as calc

print("\n=== Method 3: Import with Alias ===")
print("8 + 12 =", calc.add(8, 12))
print("9 - 3 =", calc.subtract(9, 3))
print("5 * 4 =", calc.multiply(5, 4))

# Advantages of this method:
# - Shorter module name
# - Avoid naming conflicts
# - Still clear where functions come from

# Section 5: Method 4 - Import Specific Functions with Aliases

# Import specific functions with custom names
from calculator import add as addition, multiply as times

print("\n=== Method 4: Import Specific Functions with Aliases ===")
print("7 + 8 =", addition(7, 8))
print("3 * 9 =", times(3, 9))

# Advantages of this method:
# - Custom function names
# - Avoid naming conflicts
# - Short function calls

# Section 6: Method 5 - Import All Functions (Not Recommended)

# Import all functions from the module
from calculator import *

print("\n=== Method 5: Import All Functions ===")
print("12 + 5 =", add(12, 5))
print("20 - 7 =", subtract(20, 7))
print("6 * 8 =", multiply(6, 8))
print("25 / 5 =", divide(25, 5))
print("3 ^ 4 =", power(3, 4))

# Disadvantages of this method:
# - Can cause naming conflicts
# - Hard to know where functions come from
# - Generally not recommended for large modules

# Section 7: Practical Example - Building a Calculator

print("\n=== Practical Example: Building a Calculator ===")

# Let's use different import methods to build a simple calculator
import calculator as calc

def simple_calculator():
    """A simple calculator using our module"""
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    
    choice = input("Enter your choice (1-5): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        result = calc.add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = calc.subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = calc.multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        result = calc.divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == "5":
        result = calc.power(num1, num2)
        print(f"{num1} ^ {num2} = {result}")
    else:
        print("Invalid choice!")