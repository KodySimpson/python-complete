# Episode 11: Boolean Logic Operators & Expressions

# Section 1: Boolean Logical Operators: AND, OR, NOT

# AND operator - both conditions must be True
age = 25
has_license = True
print("Age >= 18 AND has license:", age >= 18 and has_license)  # True
print("Age >= 30 AND has license:", age >= 30 and has_license)  # False

# OR operator - at least one condition must be True
is_student = True
is_employed = False
print("Is student OR employed:", is_student or is_employed)  # True
print("Is student OR is_employed:", is_student or is_employed)  # True

# NOT operator - reverses the boolean value
is_raining = True
print("Is raining:", is_raining)
print("NOT is_raining:", not is_raining)  # False

# Boolean Expressions: Using Comparison and Logical Operators to make expressions that evaluate to True or False
x = 10
y = 20
z = 5

# Using AND
print("x < y AND y > z:", x < y and y > z)  # True (10 < 20 and 20 > 5)

# Using OR
print("x > y OR z < y:", x > y or z < y)  # True (10 > 20 is False, but 5 < 20 is True)

# Using NOT
print("NOT (x > z):", not (x > z))  # False (10 > 5 is True, so NOT True = False)

# Complex expression
print("((x < y) AND (y < 30)) OR (z == 5):", ((x < y) and (y < 30)) or (z == 5))
# True (10 < 20 and 20 < 30 is True, OR 5 == 5 is True → overall True)

# Some more realistic examples
is_member = input("Are you a member? (y/n): ")
item_price = float(input("What is the price of the item? "))
discount_applied = is_member == "y" and item_price > 100
print("Discount applied:", discount_applied)

has_degree = False
years_experience = 6
print("Meets job requirements:", has_degree or years_experience >= 5)  

# Operator Precedence: 
 # 1. NOT
 # 2. AND
 # 3. OR
 # 4. Comparison operators (==, !=, <, >, <=, >=)
 
print("not True and False:", not True and False)  
# (not True) and False → False and False → False

print("True or False and False:", True or False and False)  
# True or (False and False) → True or False → True

print("(True or False) and False:", (True or False) and False)  
# (True or False) → True → True and False → False=

print("not False or False and True:", not False or False and True)  
# (not False) or (False and True) → True or False → True