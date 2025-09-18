# Episode 23: Default Parameters in Python

# Default parameters allow you to make some arguments optional in your functions.
# If a parameter has a default value, you don't have to provide it when calling the function.

# Section 1: Basic Default Parameters

# Function with one default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling with both parameters
greet("Alice", "Hi")

# Calling with just the required parameter (uses default for greeting)
greet("Bob")

# Function with multiple default parameters
def create_profile(name, age=18, city="Unknown"):
    print(f"Profile: {name}, {age} years old, from {city}")

# Different ways to call the function
print("Creating profiles:")
create_profile("Alice")  # Uses defaults for age and city
create_profile("Bob", 25)  # Uses default for city
create_profile("Charlie", 30, "Boston")  # Provides all values

# Section 2: Mixing Required and Default Parameters

# Function with required parameters first, then defaults
def describe_person(name, age, city="Unknown", occupation="Student"):
    print(f"{name} is {age} years old, lives in {city}, and works as a {occupation}.")

# Different calling patterns
print("Describing people:")
describe_person("Alice", 25)  # Uses defaults for city and occupation
describe_person("Bob", 30, "New York")  # Uses default for occupation
describe_person("Charlie", 35, "Los Angeles", "Engineer")  # All parameters

# Section 3: Default Parameters with Different Data Types

# Default with string
def print_message(message="No message provided"):
    print(f"Message: {message}")

# Default with number
def calculate_area(length, width=1):
    area = length * width
    print(f"Area: {area}")

# Default with boolean
def check_status(name, is_active=True):
    status = "active" if is_active else "inactive"
    print(f"{name} is {status}")

# Default with list
def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    print(f"List: {my_list}")

# Testing these functions
print("Testing different default types:")
print_message()
print_message("Hello World!")

calculate_area(5)
calculate_area(5, 3)

check_status("Alice")
check_status("Bob", False)

add_to_list("apple")
add_to_list("banana")

# Section 4: Practical Examples

# Function for creating user accounts
def create_user(username, email, is_admin=False, is_verified=False):
    print(f"Creating user: {username}")
    print(f"Email: {email}")
    print(f"Admin: {is_admin}")
    print(f"Verified: {is_verified}")
    print("---")

# Creating different types of users
print("Creating users:")
create_user("alice", "alice@email.com")
create_user("admin", "admin@email.com", is_admin=True)
create_user("verified_user", "user@email.com", is_verified=True)

# Function for formatting text
def format_text(text, prefix="", suffix="", uppercase=False):
    result = text
    if uppercase:
        result = result.upper()
    result = prefix + result + suffix
    print(f"Formatted: '{result}'")

# Testing text formatting
print("\nText formatting:")
format_text("hello world")
format_text("hello world", prefix=">>> ")
format_text("hello world", suffix=" <<<")
format_text("hello world", prefix=">>> ", suffix=" <<<", uppercase=True)

# Section 5: Common Pitfalls and Best Practices

# ❌ BAD: Using mutable objects as defaults
def bad_function(items=[]):
    items.append("new item")
    print(f"Items: {items}")

# This can cause unexpected behavior
print("Bad function (mutable default):")
bad_function()
bad_function()  # The list persists between calls!

# ✅ GOOD: Using None as default for mutable objects
def good_function(items=None):
    if items is None:
        items = []
    items.append("new item")
    print(f"Items: {items}")

# This works correctly
print("\nGood function (None as default):")
good_function()
good_function()  # Each call gets a fresh list

# Section 6: Practical Exercise

############
## Exercise: Create a customizable greeting system
print("=== Customizable Greeting System ===")

# Function to create a greeting with defaults
def create_greeting(name, greeting="Hello", punctuation="!", time_of_day=""):
    if time_of_day:
        full_greeting = f"{greeting} {name} {time_of_day}{punctuation}"
    else:
        full_greeting = f"{greeting} {name}{punctuation}"
    print(full_greeting)

# Function to get user preferences
def get_greeting_preferences():
    name = input("Enter your name: ")
    
    greeting = input("Enter greeting (or press Enter for default): ")
    if not greeting:
        greeting = "Hello"
    
    punctuation = input("Enter punctuation (or press Enter for default): ")
    if not punctuation:
        punctuation = "!"
    
    time_of_day = input("Enter time of day (or press Enter to skip): ")
    
    return name, greeting, punctuation, time_of_day

# Main greeting function
def greeting_system():
    print("Welcome to the Customizable Greeting System!")
    print("You can customize your greeting or use defaults.")
    
    while True:
        name, greeting, punctuation, time_of_day = get_greeting_preferences()
        
        print("\nYour customized greeting:")
        create_greeting(name, greeting, punctuation, time_of_day)
        
        # Show default greeting for comparison
        print("Default greeting:")
        create_greeting(name)
        
        continue_choice = input("\nCreate another greeting? (yes/no): ")
        if continue_choice.lower() != "yes":
            print("Goodbye!")
            break

# Run the greeting system
greeting_system() 