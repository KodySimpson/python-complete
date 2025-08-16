# Episode 19: Return Values in Python

# Return values allow functions to send data back to the code that called them.
# This is how functions can be used in calculations and assignments.

# Section 1: Basic Return Values

# Function that returns a simple value
def get_five():
    return 5

# Using the returned value
result = get_five()
print(f"Function returned: {result}")

# Function that returns a string
def get_greeting():
    return "Hello, World!"

# Using the returned string
message = get_greeting()
print(f"Message: {message}")

# Function that returns a calculation
def add_numbers(a, b):
    return a + b

# Using the returned calculation
sum_result = add_numbers(10, 20)
print(f"Sum: {sum_result}")

# Section 2: Return Values in Expressions

# Using return values directly in expressions
def multiply(a, b):
    return a * b

# Using the function in a larger expression
total = multiply(5, 3) + 10
print(f"5 * 3 + 10 = {total}")

# Using return values in print statements
def get_name():
    return "Alice"

print(f"Hello, {get_name()}!")

# Using return values in conditionals
def is_even(number):
    return number % 2 == 0

if is_even(4):
    print("4 is even")
else:
    print("4 is odd")
 
# Section 3: Conditional Returns

# Function with conditional returns
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Testing the function
print(f"Score 95: {get_grade(95)}")
print(f"Score 85: {get_grade(85)}")
print(f"Score 75: {get_grade(75)}")
print(f"Score 55: {get_grade(55)}")

# Function that returns different types
def process_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return 0

# Testing with different inputs
print(f"5 is {process_number(5)}")
print(f"-3 is {process_number(-3)}")
print(f"0 is {process_number(0)}")

# Section 4: Return Values with Lists

# Function that returns a modified list
def double_numbers(numbers):
    doubled = []
    for num in numbers:
        doubled.append(num * 2)
    return doubled

# Using the function
original = [1, 2, 3, 4, 5]
doubled = double_numbers(original)
print(f"Original: {original}")
print(f"Doubled: {doubled}")

# Function that returns filtered list
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Using the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = get_even_numbers(numbers)
print(f"All numbers: {numbers}")
print(f"Even numbers: {evens}")

# Section 5: Return Values in Calculations

# Function that calculates area of a circle
def calculate_circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

# Using the function in calculations
radius = 5
area = calculate_circle_area(radius)
print(f"Circle with radius {radius} has area: {area}")
 
# Section 6: Practical Exercise

############
## Exercise: Create a temperature converter with return values
print("=== Temperature Converter ===")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Function to get conversion choice
def get_conversion_choice():
    print("\nTemperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")
    return choice

# Function to get temperature input
def get_temperature():
    temp = float(input("Enter temperature: "))
    return temp

# Function to display result
def display_result(original_temp, converted_temp, from_unit, to_unit):
    print(f"{original_temp}°{from_unit} = {converted_temp:.1f}°{to_unit}")

# Main conversion function
def temperature_converter():
    print("Welcome to Temperature Converter!")
    
    choice = get_conversion_choice()
    
    if choice == "1":
        celsius = get_temperature()
        fahrenheit = celsius_to_fahrenheit(celsius)
        display_result(celsius, fahrenheit, "C", "F")
    elif choice == "2":
        fahrenheit = get_temperature()
        celsius = fahrenheit_to_celsius(fahrenheit)
        display_result(fahrenheit, celsius, "F", "C")
    else:
        print("Invalid choice!")

# Run the converter
temperature_converter() 