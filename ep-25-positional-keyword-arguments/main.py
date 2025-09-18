# Episode 21: Positional and Keyword Arguments in Python

# Python functions can accept arguments in two ways: positional and keyword.
# Understanding both types helps you write more flexible and readable code.

# Section 1: Positional Arguments

# Positional arguments are passed to functions in a specific order.
# The order matters - the first argument goes to the first parameter, etc.

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with positional arguments (order matters)
print("Positional arguments:")
describe_pet("dog", "Buddy")  # animal_type="dog", pet_name="Buddy"
describe_pet("cat", "Whiskers")  # animal_type="cat", pet_name="Whiskers"

# If you mix up the order, you get unexpected results
describe_pet("Buddy", "dog")  # This would say "I have a Buddy named dog"

# Section 2: Keyword Arguments

# Keyword arguments are passed with the parameter name and value.
# Order doesn't matter when using keyword arguments.

def describe_pet_keyword(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with keyword arguments (order doesn't matter)
print("\nKeyword arguments:")
describe_pet_keyword(pet_name="Buddy", animal_type="dog")
describe_pet_keyword(animal_type="cat", pet_name="Whiskers")

# You can mix the order and still get the right result
describe_pet_keyword(pet_name="Fluffy", animal_type="rabbit")

# Section 3: Mixing Positional and Keyword Arguments

# You can mix positional and keyword arguments in the same function call.
# Positional arguments must come before keyword arguments.

def create_profile(name, age, city, occupation):
    print(f"Profile: {name}, {age} years old, from {city}, works as {occupation}")

# Mixing positional and keyword arguments
print("\nMixing positional and keyword arguments:")
create_profile("Alice", 25, occupation="Engineer", city="New York")
create_profile("Bob", 30, "Boston", occupation="Teacher")

# This would cause an error - keyword arguments must come after positional ones
# create_profile(name="Charlie", 35, "Chicago", "Doctor")  # SyntaxError!

# Section 4: Functions with Default Parameters and Mixed Arguments

# When functions have default parameters, you can skip them with keyword arguments

def create_user_profile(name, age, city="Unknown", occupation="Student", is_verified=False):
    print(f"User: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Occupation: {occupation}")
    print(f"Verified: {is_verified}")
    print("---")

# Different ways to call the function
print("Creating user profiles with mixed arguments:")
create_user_profile("Alice", 25)  # All positional, uses defaults
create_user_profile("Bob", 30, "Boston")  # Mix of positional and defaults
create_user_profile("Charlie", 35, occupation="Engineer")  # Skip city with keyword
create_user_profile("Diana", 28, "Seattle", "Designer", True)  # All arguments
create_user_profile("Eve", 22, is_verified=True)  # Skip occupation with keyword

# Section 6: Advanced Examples

# Function that demonstrates the flexibility of mixed arguments
def create_event(name, date, time, location, max_attendees=50, is_public=True, requires_rsvp=False):
    print(f"Event: {name}")
    print(f"Date: {date}")
    print(f"Time: {time}")
    print(f"Location: {location}")
    print(f"Max attendees: {max_attendees}")
    print(f"Public: {is_public}")
    print(f"RSVP required: {requires_rsvp}")
    print("---")

# Creating different types of events
print("Creating events:")
create_event("Python Workshop", "2024-01-15", "10:00 AM", "Tech Center")
create_event("Private Meeting", "2024-01-16", "2:00 PM", "Conference Room", 
             is_public=False, requires_rsvp=True)
create_event("Large Conference", "2024-01-20", "9:00 AM", "Convention Center", 
             max_attendees=500, requires_rsvp=True)

# Section 7: Best Practices and Tips

# 1. Use keyword arguments for clarity when you have many parameters
def complex_calculation(a, b, c, d, e, f):
    result = (a + b) * c - d / e + f
    return result

# Hard to read - which number goes with which parameter?
result1 = complex_calculation(1, 2, 3, 4, 5, 6)

# Much clearer with keyword arguments
result2 = complex_calculation(a=1, b=2, c=3, d=4, e=5, f=6)

print(f"Complex calculation result: {result2}")

# 2. Use positional arguments for required parameters, keyword for optional ones
def send_email(to, subject, body, cc=None, bcc=None, priority="normal"):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")
    print(f"Priority: {priority}")
    print("---")

# Clear and readable function calls
print("Sending emails:")
send_email("alice@example.com", "Meeting Tomorrow", "Don't forget our meeting at 2 PM")
send_email("bob@example.com", "Project Update", "Here's the latest project status", 
           cc="manager@example.com", priority="high")

# Section 8: Common Pitfalls

# 1. Don't mix positional and keyword arguments incorrectly
def example_function(a, b, c):
    print(f"a={a}, b={b}, c={c}")

# This works - all positional
example_function(1, 2, 3)

# This works - all keyword
example_function(a=1, b=2, c=3)

# This works - positional then keyword
example_function(1, 2, c=3)

# This would cause an error - keyword then positional
# example_function(a=1, 2, 3)  # SyntaxError!

print("Function calls completed successfully!")

# Section 9: Practical Exercise

############
## Exercise: Create a flexible user registration system
print("=== User Registration System ===")

# Function to register a user with flexible parameters
def register_user(username, email, password, first_name="", last_name="", 
                 age=None, city="", country="", newsletter=False, terms_accepted=False):
    print("=== New User Registration ===")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")  # Hide password
    
    if first_name or last_name:
        print(f"Name: {first_name} {last_name}".strip())
    
    if age:
        print(f"Age: {age}")
    
    if city or country:
        location = f"{city}, {country}".strip(", ")
        print(f"Location: {location}")
    
    print(f"Newsletter: {'Yes' if newsletter else 'No'}")
    print(f"Terms accepted: {'Yes' if terms_accepted else 'No'}")
    print("---")

# Function to get user input
def get_user_input():
    print("Please provide the following information:")
    
    username = input("Username (required): ")
    email = input("Email (required): ")
    password = input("Password (required): ")
    
    print("\nOptional information (press Enter to skip):")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    
    age_input = input("Age: ")
    age = int(age_input) if age_input else None
    
    city = input("City: ")
    country = input("Country: ")
    
    newsletter_input = input("Subscribe to newsletter? (yes/no): ")
    newsletter = newsletter_input.lower() == "yes"
    
    terms_input = input("Accept terms and conditions? (yes/no): ")
    terms_accepted = terms_input.lower() == "yes"
    
    return (username, email, password, first_name, last_name, 
            age, city, country, newsletter, terms_accepted)

# Function to demonstrate different registration methods
def demonstrate_registration_methods():
    print("Demonstrating different registration methods:")
    
    # Method 1: All required parameters only
    register_user("alice123", "alice@example.com", "password123")
    
    # Method 2: Some optional parameters with positional arguments
    register_user("bob456", "bob@example.com", "mypassword", "Bob", "Smith")
    
    # Method 3: Mix of positional and keyword arguments
    register_user("charlie789", "charlie@example.com", "secret123", 
                 first_name="Charlie", age=25, newsletter=True)
    
    # Method 4: All keyword arguments
    register_user(username="diana321", email="diana@example.com", password="securepass",
                 first_name="Diana", last_name="Johnson", age=30, city="New York",
                 country="USA", newsletter=True, terms_accepted=True)

# Main registration system
def registration_system():
    print("Welcome to the User Registration System!")
    print("This system demonstrates positional and keyword arguments.")
    
    while True:
        print("\nChoose an option:")
        print("1. Register a new user")
        print("2. See registration examples")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            user_data = get_user_input()
            register_user(*user_data)
            
        elif choice == "2":
            demonstrate_registration_methods()
            
        elif choice == "3":
            print("Thank you for using the registration system!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the registration system
registration_system()
