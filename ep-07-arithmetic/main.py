# Episode 7: Arithmetic Operations in Python

# Section 1: Basic Arithmetic Operations

# Addition
print(1 + 2) # 3
print(1.0 + 2.0) # 3.0

# You can store the result of operations in a variable
sum = 1 + 2
print(sum)

# Subtraction
print(1 - 2) # -1

# Multiplication
print(2 * 3) # 6
print(2.0 * 3.0) # 6.0

# Division
print(10 / 2) # 5.0, when doing division, the result is a float
print(10.0 / 3) # 3.3333333333333335

# Modulus (getting the remainder of a division)
print(10 % 3) # 1

# Exponentiation
print(2 ** 3) # 8
print(2.0 ** 3.0) # 8.0

# Floor Division (chops off the decimal part)
print(10 // 3) # 3

# Section 2: Type Mixing (int vs float)

#######
## What happens when you mix int and float?
print(1 + 2.0) # 3.0
print(1.0 + 2) # 3.0
print(1 - 2.0) # -1.0
print(1.0 - 2) # -1.0
print(1 * 2.0) # 2.0
print(1.0 * 2) # 2.0
print(1 / 2.0) # 0.5
print(1.0 / 2) # 0.5
print(1 % 2.0) # 1.0
# Answer: When you mix int and float, the result is a float

# Section 3: Order of Operations

print("Order of Operations (PEMDAS): Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")

# Example without parentheses
result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)  # Output: 2 + 3 * 4 = 14

# Example with parentheses
result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)  # Output: (2 + 3) * 4 = 20

# Mixed operations
result3 = 10 / 2 + 3 ** 2
print("10 / 2 + 3 ** 2 =", result3)  # Output: 10 / 2 + 3 ** 2 = 14.0

# Section 4: Assignment Operators

# Assignment operators combine arithmetic operations with assignment
# They are shortcuts for common operations

# Addition assignment (+=)
x = 5
x += 3  # Same as: x = x + 3
print("x += 3:", x)  # Output: 8

# Subtraction assignment (-=)
y = 10
y -= 4  # Same as: y = y - 4
print("y -= 4:", y)  # Output: 6

# Multiplication assignment (*=)
z = 3
z *= 5  # Same as: z = z * 5
print("z *= 5:", z)  # Output: 15

# Division assignment (/=)
a = 20
a /= 4  # Same as: a = a / 4
print("a /= 4:", a)  # Output: 5.0

# Modulus assignment (%=)
b = 17
b %= 5  # Same as: b = b % 5
print("b %= 5:", b)  # Output: 2

# Exponentiation assignment (**=)
c = 2
c **= 3  # Same as: c = c ** 3
print("c **= 3:", c)  # Output: 8

# Floor division assignment (//=)
d = 17
d //= 5  # Same as: d = d // 5
print("d //= 5:", d)  # Output: 3

# Section 5: Practical Exercise

############
## Excercise: Calculate the area of a circle
# Area of a circle = π * r^2
radius = 5
pi = 3.14159
area = pi * radius ** 2
print("Area of a circle with radius", radius, "is", area)