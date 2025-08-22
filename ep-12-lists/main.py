# Episode 12: Lists in Python

# Lists are a way to store multiple items in a single variable.
# They are:
# - Ordered
# - Changeable
# - Allow duplicates

# Section 1: Creating Lists

# Creating a list with square brackets
fruits = ["apple", "banana", "orange"]
print("Fruits list:", fruits)

# Lists can contain different data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed list:", mixed_list)

# Empty list
empty_list = []
print("Empty list:", empty_list)

# List with duplicate elements
numbers = [1, 2, 2, 3, 3, 3]
print("Numbers with duplicates:", numbers)

# Section 2: Accessing List Elements

# Accessing elements by index (0-based)
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("Second to last:", fruits[-2])

# Getting list length
print("Number of fruits:", len(fruits))

# Section 3: Modifying Lists

# Changing elements
fruits = ["apple", "banana", "orange"]
print("Original fruits:", fruits)
fruits[1] = "blueberry"
print("After changing index 1:", fruits)

# Adding elements
fruits.append("grape")
print("After append:", fruits)

# Inserting elements at specific positions
fruits.insert(1, "strawberry")
print("After insert at index 1:", fruits)

# Removing elements
fruits.remove("blueberry")
print("After removing 'blueberry':", fruits)

# Removing by index
removed_fruit = fruits.pop(0)
print("Removed fruit:", removed_fruit)
print("After pop:", fruits)

# Section 4: List Slicing

# Creating a list for slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Numbers:", numbers)

# Basic slicing [start:end]
print("First 3 numbers:", numbers[0:3])
print("Numbers 2-5:", numbers[2:6])
print("Last 3 numbers:", numbers[-3:])

# Slicing with step [start:end:step]
print("Every second number:", numbers[::2])
print("Reverse order:", numbers[::-1])
print("Every third number:", numbers[::3])

# Section 5: List Methods

# Sorting
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original numbers:", numbers)
numbers.sort()
print("After sort:", numbers)

# Reverse sorting
numbers.sort(reverse=True)
print("After reverse sort:", numbers)