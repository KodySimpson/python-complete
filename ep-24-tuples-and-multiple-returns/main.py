# Episode 21: Tuples and Multiple Return Values in Python

# Tuples are ordered, immutable collections. Functions often use tuples to
# return multiple values in a single, convenient package.

# Section 1: What is a Tuple?

# Creating a tuple
coordinates = (10, 20)
print(f"A tuple example: {coordinates}")

# Accessing tuple items
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Section 2: Returning Multiple Values (Tuples under the hood)

# Function that returns multiple values
def get_name_and_age():
	name = "Alice"
	age = 25
	return name, age  # Python returns a tuple here

# Unpacking multiple return values
person_name, person_age = get_name_and_age()
print(f"Name: {person_name}, Age: {person_age}")

# Section 3: Explicit Tuple Returns and Unpacking

# Function that returns a tuple explicitly
def get_coordinates():
	return (10, 20)

# Using the returned coordinates with unpacking
x, y = get_coordinates()
print(f"Coordinates: ({x}, {y})")

# You can also ignore values you don't need using underscore
first, _ = ("first", "second")
print(f"First only: {first}")

# Section 4: Practical Functions Using Tuples

# Function that calculates area and perimeter of a rectangle
def calculate_rectangle(length, width):
	area = length * width
	perimeter = 2 * (length + width)
	return area, perimeter

rect_area, rect_perimeter = calculate_rectangle(10, 5)
print(f"Rectangle 10x5 => Area={rect_area}, Perimeter={rect_perimeter}")

# Function that splits a full name into first and last
def split_full_name(full_name):
	parts = full_name.strip().split()
	if len(parts) == 0:
		return ("", "")
	if len(parts) == 1:
		return (parts[0], "")
	# Join everything except the last as first name(s)
	first = " ".join(parts[:-1])
	last = parts[-1]
	return first, last

first_name, last_name = split_full_name("Ada Lovelace")
print(f"First: {first_name}, Last: {last_name}")

# Section 5: Mini Exercise

############
## Exercise: Create a function that returns (min_value, max_value)
print("=== Min/Max Finder ===")

def find_min_max(numbers):
	if not numbers:
		return (None, None)
	minimum = numbers[0]
	maximum = numbers[0]
	for value in numbers[1:]:
		if value < minimum:
			minimum = value
		if value > maximum:
			maximum = value
	return minimum, maximum

sample = [3, 1, 9, 4, 7]
mn, mx = find_min_max(sample)
print(f"Numbers: {sample}")
print(f"Min: {mn}, Max: {mx}")


