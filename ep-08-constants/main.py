## Constants: Variables that are not meant to be changed.

# Python doesn't enforce constants, it's just something that is good practice
# and is useful.

# Constants are typically written in all caps.
# They are usually defined at the top of the file.
PI = 3.14159
GRAVITY = 9.81
MAX_REQUESTS = 1000 # max number of requests to the API

# you can technically change the value of a constant, but it's not recommended.
# PI = 3.141592653589793
# print(PI)

# Using constants in calculations
print("=== Using Constants in Calculations ===")

# Calculate the area of a circle with radius 5
radius = 5
circle_area = PI * radius ** 2
print(f"Area of circle with radius {radius}: {circle_area:.2f}")

# Calculate the circumference of a circle
circumference = 2 * PI * radius
print(f"Circumference of circle with radius {radius}: {circumference:.2f}")

# Calculate the time it takes for an object to fall 100 meters
distance = 100
fall_time = (2 * distance / GRAVITY) ** 0.5
print(f"Time to fall {distance} meters: {fall_time:.2f} seconds")

# Using the Final type hint so that your IDE can tell you that you are not allowed to change the value of the variable
from typing import Final

PI: Final = 3.14159

# Modern IDEs should complain here if they have type hinting enabled
PI = 3.141592653589793