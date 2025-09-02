# Episode 9: Input and Output in Python

# Section 1: Getting User Input

# The input() function gets text from the user
name = input("What is your name? ")
print("Hello,", name)

# Input always returns a string
age_input = input("How old are you? ")
print("Age input type:", type(age_input))
print("Age input value:", age_input)

# Section 2: Type Conversion

# When we get input, it's always a string. 
# If we want to use it as a number, we need to convert it to a number.

# Converting string input to numbers
age = int(input("How old are you? "))
print("Age as integer:", age)
print("Age type:", type(age))

# Converting to float
height = float(input("What is your height in meters? "))
print("Height as float:", height)
print("Height type:", type(height))

# Converting numbers to strings
number = 42
text = str(number)
print("Number as string:", text)
print("Text type:", type(text))

# Section 3: Calculator Exercise

############
## Exercise: Create a simple calculator
print("=== Simple Calculator ===")

# Get two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print(f"\nResults:")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}") 