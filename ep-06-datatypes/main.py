# Episode 6: Basic Data Types in Python

# Section 1: Numeric Types

# Integers (int): Whole numbers without decimals, can be positive or negative.
my_integer = 42
print("Integer example:", my_integer)
print("Type:", type(my_integer))

# Numbers in python can be really big
my_big_integer = 123456789012345678901234567890
print("Big integer example:", my_big_integer)
print("Type:", type(my_big_integer))

# You can also use underscores to make numbers more readable
my_big_integer = 123_456_789_012_345_678_901_234_567_890
print("Big integer with underscores:", my_big_integer)

# You can do math with integers, we will cover this in more detail in the next episodes
sum_int = my_integer + 8
print("Sum of integers:", sum_int)

# Floats (float): Numbers with decimal points.
my_float = 3.14
print("Float example:", my_float)
print("Type:", type(my_float))

# Floats can be in exponential notation too
my_float = 1.23e-4 # 1.23 * 10^-4 or 0.000123
print("Float in exponential notation:", my_float)

# Section 2: Strings (str): Text data, enclosed in single or double quotes.
my_string = "Hello, Python!"
print("String example:", my_string)
print("Type:", type(my_string))

# String concatenation (joining strings)
greeting = my_string + " Welcome to data types."
print("Concatenated string:", greeting)

# Section 3: Booleans (bool): True or False values, often from comparisons.
is_true = True
is_false = False
print("Boolean True:", is_true)
print("Type:", type(is_true))

# Section 4: None (no value)
#
# None represents the absence of a value. It is its own type: NoneType.
favorite_food = None # We will need to store my favorite food, but we don't know it yet
print("None example:", favorite_food)
print("Type:", type(favorite_food))

favorite_food = "pizza"
print("Favorite food:", favorite_food)
print("Type:", type(favorite_food))