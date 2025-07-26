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

# Counting elements
letters = ["a", "b", "a", "c", "a", "b"]
print("Letters:", letters)
print("Count of 'a':", letters.count("a"))
print("Count of 'b':", letters.count("b"))

# Finding elements
print("Index of 'c':", letters.index("c"))

# Section 6: Lists with Input

# Creating a list from user input
print("Enter 3 favorite colors:")
colors = []
colors.append(input("Color 1: "))
colors.append(input("Color 2: "))
colors.append(input("Color 3: "))
print("Your favorite colors:", colors)

# Another way to get input
print("Enter 3 numbers:")
numbers = []
for i in range(3):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)
print("Your numbers:", numbers)

# Section 7: Practical Exercise

############
## Exercise: Create a simple shopping list manager
print("=== Shopping List Manager ===")

# Initialize shopping list
shopping_list = []

# Add items to the list (limited to 3 items to avoid loops)
print("Add 3 items to your shopping list:")
item1 = input("Item 1: ")
shopping_list.append(item1)

item2 = input("Item 2: ")
shopping_list.append(item2)

item3 = input("Item 3: ")
shopping_list.append(item3)

# Display the list
print(f"\n=== Your Shopping List ===")
print(f"You have {len(shopping_list)} items:")
print(f"1. {shopping_list[0]}")
print(f"2. {shopping_list[1]}")
print(f"3. {shopping_list[2]}")

# Ask if user wants to remove an item
remove_item = input("\nDo you want to remove an item? (yes/no): ").lower()
if remove_item == "yes":
    item_to_remove = input("Enter the item to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"Removed '{item_to_remove}' from your list.")
    else:
        print(f"'{item_to_remove}' is not in your list.")

# Final list
print(f"\n=== Final Shopping List ===")
print("Your final list:")
if len(shopping_list) >= 1:
    print(f"1. {shopping_list[0]}")
if len(shopping_list) >= 2:
    print(f"2. {shopping_list[1]}")
if len(shopping_list) >= 3:
    print(f"3. {shopping_list[2]}") 