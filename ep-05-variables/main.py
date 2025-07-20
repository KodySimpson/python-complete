# Section 1: What Are Variables?
# Variables are names that point to (reference) data values stored in memory.
# They act like labels on boxes, making it easy to store, retrieve, and manipulate data.
# In Python, variables are dynamically typed—you don't declare the type upfront.
# Everything in Python is an object, and variables reference these objects.

# Simple assignment: Create a variable and assign a value
age = 69  # 'age' now stores the value 69 in your computer's memory

# Printing variables is a great way to see what values are stored in them.
print(age)
print("Initial age:", age)

# Variables can hold different kinds of data (we'll cover types in the next episode)
name = "Billy Bob Johnson"  # String value
print(name)

# Why variables? They make code readable and reusable—e.g., reuse 'age' in calculations
years_later = age + 5
print("Age in 5 years:", years_later)

# Section 2: How to Properly Name Variables
# Rules:
# - Must start with a letter (a-z, A-Z) or underscore (_).
# - Can contain letters, numbers (0-9), or underscores after the first character.
# - Case-sensitive (myVar != MyVar).
# - Cannot be Python reserved words (keywords like 'if', 'for', 'True', etc.).
# - No special characters like !, @, #, etc.
# - No starting with numbers.

# The convention is to use snake_case for variables/functions

# Valid names
total_score = 100 # snake_case
_total = 50  # Leading underscore is okay
player2 = "Bob"  # Numbers okay after first char

print(total_score)
print(_total)
print(player2)

# Invalid names (uncomment to see SyntaxError)
# 2player = "Invalid"  # Starts with number
# total-score = 100    # Hyphen not allowed
# if = 5               # Reserved word

# Reserved words example: List some common ones
# Full list: False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
# Avoid them! Trying to use one causes SyntaxError.
# Demo: print(if) would error if assigned

# Section 3: Assignment and Reassignment
# Assignment: Use = to bind a name to a value (creates the variable if it doesn't exist).
# Reassignment: Just assign a new value—the variable now points to the new object.

# Initial assignment
counter = 0
print("Initial counter:", counter)

# Reassign
counter = 10
print("Reassigned counter:", counter)

# You can reassign to a different type too (dynamic typing)
counter = "Now a string!"
print("Counter as string:", counter)

# Multiple assignment, assigning multiple variables at once
x = y = z = 42
print("x, y, z:", x, y, z)  # Output: 42 42 42

# Challenge: Try swapping two variables
# (the normal way)
a = 1
b = 2

# Swap
temp = a
a = b
b = temp
print("Swapped a and b:", a, b)

#Cool trick: Swap values easily (no temp var needed)
a = 1
b = 2
a, b = b, a  # Swap
print("Swapped a and b:", a, b)

# You now know how to store data! Yippee!