# Episode 16: For Loops in Python

# For loops are used to iterate over sequences (like lists, strings, or ranges).
# They're great when you know how many times you want to repeat something.

# Section 1: Basic For Loop with Range

# Using range() to create a sequence of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

# Range with just end value (starts from 0)
print("\nCounting from 0 to 4:")
for i in range(5):
    print(f"Index: {i}")

# Range with step
print("\nCounting by 2s:")
for i in range(0, 10, 2):
    print(f"Even number: {i}")

# Section 2: For Loops with Lists

# Iterating over list elements
fruits = ["apple", "banana", "orange", "grape"]
print("My favorite fruits:")
for fruit in fruits:
    print(f"I like {fruit}")

# Modifying list elements in a loop
numbers = [1, 2, 3, 4, 5]
print("\nOriginal numbers:", numbers)
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print("Doubled numbers:", numbers)

# Section 3: For Loops with Strings

# Iterating over characters in a string
word = "Python"
print("Letters in 'Python':")
for letter in word:
    print(letter)

# Counting vowels in a string
sentence = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"\nThe sentence '{sentence}' has {vowel_count} vowels.")

# Section 4: Enumerate - Getting Index and Value

# Using enumerate to get both index and value
fruits = ["apple", "banana", "orange"]
print("Fruits with their positions:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Enumerate with custom start
print("\nFruits starting from position 0:")
for index, fruit in enumerate(fruits, 0):
    print(f"Position {index}: {fruit}")

# Section 5: Nested For Loops

# For loops inside other for loops
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each row

# Section 6: For Loops with User Input

# Creating a list from user input using for loop
print("Enter 3 favorite movies:")
movies = []
for i in range(3):
    movie = input(f"Movie {i + 1}: ")
    movies.append(movie)

print("\nYour favorite movies:")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Section 7: Practical Exercise

############
## Exercise: Create a simple grade calculator for multiple students
print("=== Grade Calculator for Multiple Students ===")

# Get number of students
num_students = int(input("How many students? "))

# Lists to store student data
names = []
scores = []
grades = []

# Collect data for each student
for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ")
    score = int(input("Enter test score (0-100): "))
    
    names.append(name)
    scores.append(score)
    
    # Calculate grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    grades.append(grade)

# Display results
print(f"\n=== Grade Report ===")
for i in range(num_students):
    print(f"{names[i]}: {scores[i]}% - Grade {grades[i]}")

# Calculate class average
total_score = sum(scores)
class_average = total_score / num_students
print(f"\nClass Average: {class_average:.1f}%")

# Count grades
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
for grade in grades:
    grade_counts[grade] += 1

print("\nGrade Distribution:")
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count} students") 