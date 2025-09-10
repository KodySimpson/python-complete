# Episode 16: While Loops in Python

# Loops are a way to repeat code.
# While loops are a type of loop that will continue to run as long as a condition is true.

# Section 1: Basic While Loop

# Simple while loop
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1
print("Loop finished!")

# Section 2: Avoiding Infinite Loops

# WARNING: Infinite loops can crash your program!
# Always make sure your loop condition will eventually become False

# ❌ BAD: This would run forever (infinite loop)
# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     # Missing: count += 1

# Another example of avoiding infinite loops
temperature = 75
while temperature > 70:
    print(f"Temperature is {temperature}°F - still warm!")
    temperature -= 5  # This makes temperature eventually <= 70
print("Temperature has cooled down.")

# A cool example of a while loop
password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong password. {remaining} attempts remaining.")

# Loops are great for going through lists
fruits = ["apple", "banana", "orange", "grape"]
index = 0

print("Processing fruits:")
while index < len(fruits):
    print(f"Fruit {index + 1}: {fruits[index]}")
    index += 1

# Loops are great for finding elements in a list
# Find if a word is in a list
looking_for = "banana"
fridge = ["apple", "banana", "orange", "grape"]
index = 0
found = False
while index < len(fridge):
    if fridge[index] == looking_for:
        found = True
        print(f"Found '{looking_for}' at index {index}")
    index += 1
if not found:
    print(f"'{looking_for}' not found in the list.")

# Fun excersise!!
print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100.")

import random
secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    # Get user's guess
    guess = int(input(f"Enter your guess (attempt {attempts + 1}/{max_attempts}): "))
    attempts += 1
    
    # Check the guess
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break

# Check if game is over
if attempts >= max_attempts and guess != secret_number:
    print(f"Game over! The number was {secret_number}.") 