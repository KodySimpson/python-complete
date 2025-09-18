# Episode 20: Dictionaries in Python

# Dictionaries are collections of key-value pairs.
# Unlike lists which use indices, dictionaries use keys to access values.

# Section 1: Creating Dictionaries

# Creating a dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Person dictionary:", person)

# Creating an empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary as a collection of similar data (like a phone book)
phone_book = {
    "Alice": "555-0101",
    "Bob": "555-0102", 
    "Charlie": "555-0103",
    "Diana": "555-0104"
}
print("Phone book:", phone_book)

# Dictionary of student grades
grades = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 78
}
print("Student grades:", grades)

# Section 2: Accessing Dictionary Values

# Accessing values using keys
person = {"name": "Alice", "age": 25, "city": "New York"}

# Doing it like this opens the door to errors. If the key doesn't exist, it will throw an error.
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# Using get() method (safer way to access since it returns None if the key doesn't exist)
print("Name:", person.get("name"))
print("Country:", person.get("country"))  # Returns None if key doesn't exist
print("Country:", person.get("country", "Unknown"))  # Returns default value

# Section 3: Modifying Dictionaries

# Adding new key-value pairs
person = {"name": "Alice", "age": 25}
print("Original:", person)

person["city"] = "New York"
person["occupation"] = "Engineer"
print("After adding:", person)

# Updating existing values
person["age"] = 26
print("After updating age:", person)

# Removing items
del person["occupation"]
print("After removing occupation:", person)

# Using pop() method
removed_age = person.pop("age")
print(f"Removed age: {removed_age}")
print("After pop:", person)

# Section 4: Dictionary Methods

# Getting all keys
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Keys:", person.keys())

# Getting all values
print("Values:", person.values())

# Getting all items (key-value pairs)
print("Items:", person.items())

# Checking if key exists
print("Has 'name':", "name" in person)
print("Has 'country':", "country" in person)

# Getting dictionary length
print("Number of items:", len(person))

# Section 5: Iterating Through Dictionaries

# Iterating through keys
print("Iterating through keys:")
for key in person.keys():
    print(f"Key: {key}")

# Iterating through values
print("\nIterating through values:")
for value in person.values():
    print(f"Value: {value}")

# Iterating through items
print("\nIterating through items:")
for key, value in person.items():
    print(f"{key}: {value}")

# Section 6: Nested Dictionaries

# Dictionary containing other dictionaries
students = {
    "alice": {
        "age": 20,
        "grade": "A",
        "subjects": ["Math", "Science"]
    },
    "bob": {
        "age": 22,
        "grade": "B",
        "subjects": ["History", "English"]
    }
}

# Accessing nested values
print("Alice's age:", students["alice"]["age"])
print("Bob's subjects:", students["bob"]["subjects"])

# Modifying nested values
students["alice"]["grade"] = "A+"
print("Updated Alice's grade:", students["alice"]["grade"])

# Section 7: Dictionaries with Functions

# Function that creates a dictionary
def create_person(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }

# Function that processes dictionary
def display_person(person_dict):
    print(f"Name: {person_dict['name']}")
    print(f"Age: {person_dict['age']}")
    print(f"City: {person_dict['city']}")

# Using these functions
alice = create_person("Alice", 25, "New York")
display_person(alice)

# Function that updates dictionary
def update_age(person_dict, new_age):
    person_dict["age"] = new_age
    return person_dict

# Using the update function
updated_alice = update_age(alice, 26)
display_person(updated_alice)

# Section 8: Practical Exercise

############
## Exercise: Create a simple contact book
print("=== Contact Book ===")

# Initialize empty contact book
contacts = {}

# Function to add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print(f"Added {name} to contacts!")

# Function to view a contact
def view_contact():
    name = input("Enter name to view: ")
    if name in contacts:
        contact = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"{name} not found in contacts.")

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nAll contacts:")
    for name, info in contacts.items():
        print(f"{name}: {info['phone']}")

# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted {name} from contacts.")
    else:
        print(f"{name} not found in contacts.")

# Main contact book function
def contact_book():
    print("Welcome to Contact Book!")
    
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View contact")
        print("3. List all contacts")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            list_contacts()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the contact book
contact_book() 