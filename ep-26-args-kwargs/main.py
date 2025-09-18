# Episode 22: *args and **kwargs in Python

# *args and **kwargs allow functions to accept a variable number of arguments.
# *args collects positional arguments into a tuple, **kwargs collects keyword arguments into a dictionary.

# Section 1: Understanding *args

# *args allows a function to accept any number of positional arguments.
# The asterisk (*) tells Python to collect all positional arguments into a tuple.

def sum_numbers(*args):
    print(f"Received arguments: {args}")
    print(f"Type of args: {type(args)}")
    total = 0
    for number in args:
        total += number
    return total

# Testing with different numbers of arguments
print("=== Testing *args ===")
result1 = sum_numbers(1, 2, 3)
print(f"Sum of 1, 2, 3: {result1}")

result2 = sum_numbers(10, 20, 30, 40, 50)
print(f"Sum of 10, 20, 30, 40, 50: {result2}")

result3 = sum_numbers(5)  # Just one argument
print(f"Sum of 5: {result3}")

result4 = sum_numbers()  # No arguments
print(f"Sum of no arguments: {result4}")

# Section 2: *args with Regular Parameters

# You can mix *args with regular parameters.
# Regular parameters must come before *args.

def greet_and_sum(greeting, *numbers):
    print(f"{greeting}")
    if numbers:
        total = sum(*numbers)
        print(f"Sum of numbers: {total}")
    else:
        print("No numbers provided")

# Testing mixed parameters
print("\n=== *args with regular parameters ===")
greet_and_sum("Hello!", 1, 2, 3, 4, 5)
greet_and_sum("Hi there!", 10, 20)
greet_and_sum("Good morning!")  # No numbers

# Section 3: Understanding **kwargs

# **kwargs allows a function to accept any number of keyword arguments.
# The double asterisk (**) tells Python to collect all keyword arguments into a dictionary.

def create_profile(**kwargs):
    print(f"Received keyword arguments: {kwargs}")
    print(f"Type of kwargs: {type(kwargs)}")
    
    print("Profile details:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Testing with different keyword arguments
print("\n=== Testing **kwargs ===")
create_profile(name="Alice", age=25, city="New York")
create_profile(username="bob123", email="bob@example.com", is_active=True)
create_profile(title="Manager", department="IT", salary=75000, experience=5)

# Section 4: **kwargs with Regular Parameters

# You can mix **kwargs with regular parameters.
# Regular parameters must come before **kwargs.

def create_user(username, **user_info):
    print(f"Creating user: {username}")
    print("Additional information:")
    for key, value in user_info.items():
        print(f"  {key}: {value}")

# Testing mixed parameters
print("\n=== **kwargs with regular parameters ===")
create_user("alice123", email="alice@example.com", age=25, city="Boston")
create_user("bob456", full_name="Bob Smith", department="Engineering")
create_user("charlie789")  # No additional info

# Section 5: Combining *args and **kwargs

# You can use both *args and **kwargs in the same function.
# Order must be: regular parameters, *args, **kwargs

def flexible_function(required_param, *args, **kwargs):
    print(f"Required parameter: {required_param}")
    print(f"Positional arguments (*args): {args}")
    print(f"Keyword arguments (**kwargs): {kwargs}")

# Testing the flexible function
print("\n=== Combining *args and **kwargs ===")
flexible_function("Hello", 1, 2, 3, name="Alice", age=25)
flexible_function("World", "a", "b", "c", color="blue", size="large")
flexible_function("Test")  # Just the required parameter

# Section 6: Practical Examples with *args

# Function to find the maximum of any number of values
def find_maximum(*numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

# Function to concatenate strings
def concatenate_strings(*strings):
    return " ".join(strings)

# Function to calculate average
def calculate_average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Testing practical examples
print("\n=== Practical *args Examples ===")
print(f"Maximum of 1, 5, 3, 9, 2: {find_maximum(1, 5, 3, 9, 2)}")
print(f"Maximum of 10, 20: {find_maximum(10, 20)}")
print(f"Maximum of single number 42: {find_maximum(42)}")

print(f"Concatenated: {concatenate_strings('Hello', 'beautiful', 'world')}")
print(f"Concatenated: {concatenate_strings('Python', 'is', 'awesome', '!')}")

print(f"Average of 1, 2, 3, 4, 5: {calculate_average(1, 2, 3, 4, 5)}")
print(f"Average of 10, 20, 30: {calculate_average(10, 20, 30)}")

# Section 7: Practical Examples with **kwargs

# Function to create a configuration object
def create_config(**settings):
    config = {}
    for key, value in settings.items():
        config[key] = value
    return config

# Function to format a message with various options
def format_message(message, **format_options):
    formatted = message
    
    if format_options.get('uppercase', False):
        formatted = formatted.upper()
    
    if format_options.get('lowercase', False):
        formatted = formatted.lower()
    
    if 'prefix' in format_options:
        formatted = format_options['prefix'] + formatted
    
    if 'suffix' in format_options:
        formatted = formatted + format_options['suffix']
    
    return formatted

# Function to log information with flexible details
def log_info(message, **details):
    print(f"LOG: {message}")
    if details:
        print("Details:")
        for key, value in details.items():
            print(f"  {key}: {value}")

# Testing practical examples
print("\n=== Practical **kwargs Examples ===")
config = create_config(database_url="localhost:5432", debug=True, max_connections=100)
print(f"Configuration: {config}")

print(f"Formatted: {format_message('hello world', uppercase=True)}")
print(f"Formatted: {format_message('HELLO WORLD', lowercase=True, prefix='>>> ')}")
print(f"Formatted: {format_message('test', prefix='[', suffix=']')}")

log_info("User logged in", user_id=123, timestamp="2024-01-15", ip_address="192.168.1.1")
log_info("Database connection failed", error_code=500, retry_count=3)

# Section 8: Advanced Examples

# Function that demonstrates unpacking with *args and **kwargs
def demonstrate_unpacking(*args, **kwargs):
    print("Unpacked *args:")
    for i, arg in enumerate(args):
        print(f"  args[{i}] = {arg}")
    
    print("Unpacked **kwargs:")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

# Unpacking lists and dictionaries
print("\n=== Unpacking Examples ===")
numbers = [1, 2, 3, 4, 5]
user_info = {"name": "Alice", "age": 25, "city": "New York"}

# Unpack the list into *args
demonstrate_unpacking(*numbers)

# Unpack the dictionary into **kwargs
demonstrate_unpacking(**user_info)

# Unpack both
demonstrate_unpacking(*numbers, **user_info)

# Section 9: Real-World Applications

# Function to create a flexible database query
def build_query(table_name, *columns, **conditions):
    query = f"SELECT {', '.join(columns) if columns else '*'} FROM {table_name}"
    
    if conditions:
        where_clauses = []
        for column, value in conditions.items():
            where_clauses.append(f"{column} = '{value}'")
        query += " WHERE " + " AND ".join(where_clauses)
    
    return query

# Function to create HTML elements with flexible attributes
def create_html_element(tag, content, **attributes):
    attr_string = ""
    for attr, value in attributes.items():
        attr_string += f' {attr}="{value}"'
    
    return f"<{tag}{attr_string}>{content}</{tag}>"

# Function to send notifications with flexible options
def send_notification(message, **options):
    print(f"Notification: {message}")
    
    if options.get('email', False):
        print("  - Sent via email")
    
    if options.get('sms', False):
        print("  - Sent via SMS")
    
    if options.get('push', False):
        print("  - Sent as push notification")
    
    if 'priority' in options:
        print(f"  - Priority: {options['priority']}")

# Testing real-world applications
print("\n=== Real-World Applications ===")
query1 = build_query("users", "name", "email", "age")
print(f"Query 1: {query1}")

query2 = build_query("products", "name", "price", category="electronics", in_stock=True)
print(f"Query 2: {query2}")

html1 = create_html_element("div", "Hello World", class_name="container", id="main")
print(f"HTML 1: {html1}")

html2 = create_html_element("a", "Click here", href="https://example.com", target="_blank")
print(f"HTML 2: {html2}")

send_notification("New message received", email=True, priority="high")
send_notification("System maintenance", sms=True, push=True, priority="low")

# Section 10: Best Practices and Common Pitfalls

# ✅ GOOD: Clear parameter names and documentation
def process_data(*data_items, **processing_options):
    """
    Process multiple data items with flexible options.
    
    Args:
        *data_items: Variable number of data items to process
        **processing_options: Processing options like sort=True, filter=None
    """
    print(f"Processing {len(data_items)} items")
    print(f"Options: {processing_options}")

# ❌ BAD: Unclear what *args and **kwargs contain
def bad_function(*args, **kwargs):
    # What kind of arguments are expected?
    # What options are available?
    pass

# ✅ GOOD: Use meaningful names when possible
def create_user_profile(*required_fields, **optional_fields):
    print("Required fields:", required_fields)
    print("Optional fields:", optional_fields)

# Testing best practices
print("\n=== Best Practices ===")
process_data("item1", "item2", "item3", sort=True, filter="active")
create_user_profile("name", "email", "password", age=25, city="Boston")

# Section 11: Practical Exercise

############
## Exercise: Create a flexible calculator system
print("=== Flexible Calculator System ===")

# Function to perform calculations with flexible operations
def calculate(*numbers, **options):
    if not numbers:
        return 0
    
    operation = options.get('operation', 'sum')
    precision = options.get('precision', 2)
    
    if operation == 'sum':
        result = sum(numbers)
    elif operation == 'product':
        result = 1
        for num in numbers:
            result *= num
    elif operation == 'average':
        result = sum(numbers) / len(numbers)
    elif operation == 'max':
        result = max(numbers)
    elif operation == 'min':
        result = min(numbers)
    else:
        result = sum(numbers)  # Default to sum
    
    return round(result, precision)

# Function to create a report with flexible formatting
def create_report(title, *data_points, **formatting):
    print(f"\n=== {title} ===")
    
    # Apply formatting options
    if formatting.get('uppercase', False):
        title = title.upper()
    
    for i, point in enumerate(data_points, 1):
        prefix = formatting.get('prefix', f"{i}.")
        suffix = formatting.get('suffix', "")
        print(f"{prefix} {point}{suffix}")

# Function to get user input for calculations
def get_calculation_input():
    print("\nEnter numbers (separated by spaces):")
    numbers_input = input("Numbers: ")
    numbers = [float(x) for x in numbers_input.split()]
    
    print("\nChoose operation:")
    print("1. Sum")
    print("2. Product (multiply all)")
    print("3. Average")
    print("4. Maximum")
    print("5. Minimum")
    
    operation_choice = input("Enter choice (1-5): ")
    operations = {
        "1": "sum",
        "2": "product", 
        "3": "average",
        "4": "max",
        "5": "min"
    }
    operation = operations.get(operation_choice, "sum")
    
    precision = int(input("Decimal places (default 2): ") or "2")
    
    return numbers, operation, precision

# Function to demonstrate different calculation methods
def demonstrate_calculations():
    print("Demonstrating different calculation methods:")
    
    # Method 1: Basic sum
    result1 = calculate(1, 2, 3, 4, 5)
    print(f"Sum of 1,2,3,4,5: {result1}")
    
    # Method 2: Product with precision
    result2 = calculate(2, 3, 4, operation='product', precision=1)
    print(f"Product of 2,3,4: {result2}")
    
    # Method 3: Average with high precision
    result3 = calculate(10, 20, 30, 40, operation='average', precision=3)
    print(f"Average of 10,20,30,40: {result3}")
    
    # Method 4: Max and min
    result4 = calculate(5, 2, 8, 1, 9, operation='max')
    result5 = calculate(5, 2, 8, 1, 9, operation='min')
    print(f"Max of 5,2,8,1,9: {result4}")
    print(f"Min of 5,2,8,1,9: {result5}")

# Function to demonstrate report creation
def demonstrate_reports():
    print("\nDemonstrating report creation:")
    
    # Basic report
    create_report("Shopping List", "Apples", "Bananas", "Milk", "Bread")
    
    # Formatted report
    create_report("Task List", "Complete project", "Review code", "Write tests", 
                 prefix="Task", suffix=" ✓", uppercase=True)
    
    # Numbered report
    create_report("Priority Items", "Fix bug", "Update documentation", "Deploy app",
                 prefix="Priority")

# Main calculator system
def calculator_system():
    print("Welcome to the Flexible Calculator System!")
    print("This system demonstrates *args and **kwargs in action.")
    
    while True:
        print("\nChoose an option:")
        print("1. Perform calculation")
        print("2. See calculation examples")
        print("3. See report examples")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            numbers, operation, precision = get_calculation_input()
            result = calculate(*numbers, operation=operation, precision=precision)
            print(f"\nResult: {result}")
            
        elif choice == "2":
            demonstrate_calculations()
            
        elif choice == "3":
            demonstrate_reports()
            
        elif choice == "4":
            print("Thank you for using the calculator system!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the calculator system
calculator_system()
