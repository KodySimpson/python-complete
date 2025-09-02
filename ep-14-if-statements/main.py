# Episode 12: If Statements in Python

# Section 1: Basic If Statement

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult!")

# If statement with a condition that's False
age = 16
if age >= 18:
    print("You are an adult!")  # This won't print

# Section 2: If-Else Statements

# If-else statement
age = 16
if age >= 18:
    print("You are an adult!")
else:
    print("You are not an adult yet.")

# Another example
temperature = 75
if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# Section 3: If-Elif-Else Statements

# Multiple conditions with elif
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Another example with elif
day = "Monday"
if day == "Saturday":
    print("It's the weekend!")
elif day == "Sunday":
    print("It's the weekend!")
elif day == "Friday":
    print("TGIF!")
else:
    print("It's a weekday.")

# Section 4: If Statements with Input

# Get user input and use it in if statements
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")
    print("You can drive!")
    print("You are an adult!")
else:
    years_until_adult = 18 - age
    print(f"You will be an adult in {years_until_adult} years.")

# Another input example
password = input("Enter the password: ")
if password == "secret123":
    print("Access granted!")
else:
    print("Access denied!")

# Section 5: Complex Conditions

# Using boolean operators in if statements
age = 25
has_ticket = True
has_id = False

if age >= 18 and has_ticket and has_id:
    print("You can enter the club!")
elif age >= 18 and has_ticket:
    print("You need to show ID to enter.")
else:
    print("You cannot enter the club.")

# Using OR in conditions
is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("You can sleep in!")
else:
    print("Time to go to work!")

# Section 6: Practical Exercise

############
## Exercise: Create a simple grade calculator
print("=== Grade Calculator ===")

# Get student information
name = input("Enter student name: ")
score = int(input("Enter test score (0-100): "))

# Calculate grade
print(f"\n=== Grade Report ===")
print(f"Student: {name}")
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
    print("Excellent work!")
elif score >= 80:
    print("Grade: B")
    print("Good job!")
elif score >= 70:
    print("Grade: C")
    print("Satisfactory work.")
elif score >= 60:
    print("Grade: D")
    print("Needs improvement.")
else:
    print("Grade: F")
    print("Failed. Please retake the test.")

# Additional feedback
if score >= 80:
    print("You're doing well in this class!")
elif score >= 60:
    print("You're passing, but could improve with more study.")
else:
    print("Consider getting extra help or tutoring.") 