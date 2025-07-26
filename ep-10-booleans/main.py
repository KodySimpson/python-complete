# Episode 10: Booleans and Comparison Operators in Python

# Section 1: Boolean Values

# Boolean values are True and False
is_true = True
is_false = False
print("True value:", is_true)
print("False value:", is_false)
print("Type of True:", type(True))

# Section 2: Comparison Operators

# Equal to (==)
print("5 == 5:", 5 == 5)  # True
print("5 == 3:", 5 == 3)  # False

# Not equal to (!=)
print("5 != 3:", 5 != 3)  # True
print("5 != 5:", 5 != 5)  # False

# Greater than (>)
print("5 > 3:", 5 > 3)    # True
print("3 > 5:", 3 > 5)    # False

# Less than (<)
print("3 < 5:", 3 < 5)    # True
print("5 < 3:", 5 < 3)    # False

# Greater than or equal to (>=)
print("5 >= 5:", 5 >= 5)  # True
print("5 >= 3:", 5 >= 3)  # True
print("3 >= 5:", 3 >= 5)  # False

# Less than or equal to (<=)
print("3 <= 3:", 3 <= 3)  # True
print("3 <= 5:", 3 <= 5)  # True
print("5 <= 3:", 5 <= 3)  # False

# Section 3: String Comparisons

# Strings can be compared too
name1 = "Alice"
name2 = "Bob"
print("Alice == Alice:", name1 == "Alice")  # True
print("Alice == Bob:", name1 == name2)      # False

# String comparison is alphabetical
print("Alice < Bob:", name1 < name2)        # True
print("Bob > Alice:", name2 > name1)        # True

# Section 4: Comparison with Variables

# Using variables in comparisons
age = 25
minimum_age = 18
print("Age:", age)
print("Minimum age:", minimum_age)
print("Age >= minimum age:", age >= minimum_age)

# Comparing different data types
temperature = 75.5
target_temp = 70
print("Temperature:", temperature)
print("Target temperature:", target_temp)
print("Temperature > target:", temperature > target_temp)

# Section 5: Practical Exercise

############
## Exercise: Create a simple age checker
print("=== Age Checker ===")

# Get user's age
user_age = int(input("Enter your age: "))

# Check different age-based criteria
is_adult = user_age >= 18
is_teenager = user_age >= 13 and user_age <= 19
is_senior = user_age >= 65
can_vote = user_age >= 18
can_drive = user_age >= 16

# Display results
print(f"\n=== Age Analysis ===")
print(f"Your age: {user_age}")
print(f"Are you an adult? {is_adult}")
print(f"Are you a teenager? {is_teenager}")
print(f"Are you a senior? {is_senior}")
print(f"Can you vote? {can_vote}")
print(f"Can you drive? {can_drive}")

# Provide specific feedback. Will go over this in more detail in a future episode.
if user_age >= 18:
    print("✓ You are an adult!")
else:
    years_until_adult = 18 - user_age
    print(f"✗ You will be an adult in {years_until_adult} years.")

if user_age >= 65:
    print("✓ You qualify for senior discounts!")
else:
    years_until_senior = 65 - user_age
    print(f"✗ You will qualify for senior discounts in {years_until_senior} years.") 