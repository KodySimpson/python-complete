# Episode 17: Break and Continue in Python

# Break and continue are control statements that help you control the flow of loops.
# They work with both while loops and for loops.

# Section 1: Break Statement

# Break exits the loop entirely
print("=== Break Example ===")
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(f"Number: {i}")

print("Loop finished!")

# Break in while loop
print("\n=== Break in While Loop ===")
count = 0
while count < 10:
    count += 1
    if count == 5:
        break  # Exit when count reaches 5
    print(f"Count: {count}")

print("While loop finished!")

# Section 2: Continue Statement

# Continue skips the rest of the current iteration
print("\n=== Continue Example ===")
for i in range(1, 6):
    if i == 3:
        continue  # Skip the rest when i equals 3
    print(f"Number: {i}")

print("Loop finished!")

# Continue in while loop
print("\n=== Continue in While Loop ===")
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # Skip the rest when count equals 3
    print(f"Count: {count}")

print("While loop finished!")

# Section 3: Break vs Continue Comparison

print("\n=== Break vs Continue Comparison ===")

# Using break
print("Using break (exits loop):")
for i in range(1, 6):
    if i == 3:
        break
    print(f"Break: {i}")

# Using continue
print("\nUsing continue (skips iteration):")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"Continue: {i}")

# Section 4: Practical Break Examples

# Finding the first occurrence
print("\n=== Finding First Occurrence ===")
numbers = [1, 3, 5, 7, 9, 11, 13]
search_for = 7

for number in numbers:
    if number == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found!")

# Password validation with break
print("\n=== Password Validation ===")
correct_password = "secret123"
max_attempts = 3

for attempt in range(max_attempts):
    password = input(f"Enter password (attempt {attempt + 1}/{max_attempts}): ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password!")
else:
    print("Too many attempts. Access denied!")

# Section 5: Practical Continue Examples

# Skipping even numbers
print("\n=== Skipping Even Numbers ===")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# Input validation with continue
print("\n=== Input Validation ===")
valid_numbers = []

for i in range(5):
    user_input = input(f"Enter number {i + 1}: ")
    
    # Skip if input is not a number
    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue
    
    number = int(user_input)
    
    # Skip if number is negative
    if number < 0:
        print("Please enter a positive number.")
        continue
    
    valid_numbers.append(number)
    print(f"Added: {number}")

print(f"Valid numbers collected: {valid_numbers}")

# Section 6: Nested Loops with Break and Continue

print("\n=== Nested Loops ===")

# Break in nested loop (breaks inner loop only)
for i in range(1, 4):
    print(f"Outer loop: {i}")
    for j in range(1, 4):
        if j == 2:
            break  # Breaks inner loop only
        print(f"  Inner loop: {j}")

print("\n=== Nested Loops with Continue ===")

# Continue in nested loop
for i in range(1, 4):
    print(f"Outer loop: {i}")
    for j in range(1, 4):
        if j == 2:
            continue  # Skips inner loop iteration
        print(f"  Inner loop: {j}")

# Section 7: Practical Exercise

############
## Exercise: Create a number guessing game with break and continue
print("=== Enhanced Number Guessing Game ===")

import random
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("I'm thinking of a number between 1 and 100.")
print("Type 'quit' to exit early.")

while attempts < max_attempts:
    user_input = input(f"Enter your guess (attempt {attempts + 1}/{max_attempts}): ")
    
    # Check for quit command
    if user_input.lower() == 'quit':
        print("Game ended by user.")
        break
    
    # Validate input
    if not user_input.isdigit():
        print("Please enter a valid number!")
        continue
    
    guess = int(user_input)
    attempts += 1
    
    # Check if guess is in valid range
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100!")
        continue
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break

# Check if game ended without guessing
if attempts >= max_attempts and guess != secret_number:
    print(f"Game over! The number was {secret_number}.") 