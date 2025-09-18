## Python's Math Module
## https://docs.python.org/3/library/math.html
# A collection of functions and constants that you can import and use in your code.

import math # usually at the top of the file

## Constants
print(math.pi)
print(math.e)

## Functions
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.log(10))

## Useful Functions
print(math.ceil(5.3))
print(math.floor(5.3))
print(math.trunc(5.3))
print(math.fabs(-5))

## Examples

# Calculate the area of a circle with radius 5
radius = 5
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius}: {area:.2f}")

# Get the factorial of 5
print(math.factorial(5))

# if the math module did not exist, we would have to make our own functions
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

# Get the distance between two points
point1 = (1, 2)
point2 = (4, 6)
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
print(f"Distance between {point1} and {point2}: {distance:.2f}")

#or using math.dist in Python 3.8+
print(math.dist(point1, point2))

## In the next part, we will learn how to create our own modules and import them.