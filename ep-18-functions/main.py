# Episode 18: Functions in Python

# Functions are blocks of reusable code that perform a specific task.
# They help organize your code and avoid repeating the same code multiple times.

# Section 1: Basic Function Definition

# Defining a simple function
def greet():
    print("Hello, World!")

# Calling the function
print("Calling greet function:")
greet()
greet() # call it how many times you want :D. code re-use!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

# Calling function with arguments
print("\nCalling greet_person function:")
greet_person("Alice")
greet_person("Bob")

# Section 2: Functions with Multiple Parameters

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

# Calling with multiple arguments
print("Adding numbers:")
add_numbers(5, 3)
add_numbers(10, 20)

# Function with different data types
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Calling with different arguments
print("\nDescribing people:")
describe_person("Alice", 25, "New York")
describe_person("Bob", 30, "Los Angeles")

# Section 3: Local vs Global Variables

# Global variable
global_name = "Global Alice"

def demonstrate_scope():
    # Local variable
    local_name = "Local Bob"
    print(f"Inside function - Local: {local_name}")
    print(f"Inside function - Global: {global_name}")

# Calling the function
print("Demonstrating variable scope:")
demonstrate_scope()
print(f"Outside function - Global: {global_name}")
# print(local_name)  # This would cause an error - local_name is not accessible here

# Section 4: Functions with Lists

# Function that works with lists
def print_list_items(items):
    print("List items:")
    for item in items:
        print(f"- {item}")

# Function that modifies a list
def add_item_to_list(item, my_list):
    my_list.append(item)
    print(f"Added '{item}' to the list")

# Using these functions
fruits = ["apple", "banana"]
print("Original list:")
print_list_items(fruits)

add_item_to_list("orange", fruits)
print("After adding item:")
print_list_items(fruits)

# Section 5: Practical Exercise

############
## Exercise: Create a simple greeting system with functions
print("=== Greeting System ===")

# Function to get user information
def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    return name, age, city

# Function to create a greeting
def create_greeting(name, age, city):
    print(f"\nHello, {name}!")
    print(f"You are {age} years old and live in {city}.")
    
    if age < 18:
        print("You are a minor.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior.")

# Function to ask if user wants to continue
def ask_to_continue():
    response = input("\nWould you like to greet another person? (yes/no): ")
    return response.lower() == "yes"

# Main greeting function
def greeting_system():
    print("Welcome to the Greeting System!")
    
    while True:
        name, age, city = get_user_info()
        create_greeting(name, age, city)
        
        if not ask_to_continue():
            print("Goodbye!")
            break

# Run the greeting system
greeting_system() 