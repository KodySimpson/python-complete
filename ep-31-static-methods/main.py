"""
Episode 31: Static Methods

In this episode you'll learn:
- What a static method is and how it differs from instance and class methods
- When to use a static method (utility helpers, validation, pure functions)
- How to call static methods from the class and from an instance
"""

# ------------------------------------------------------------
# 1) What is a static method?
# ------------------------------------------------------------
# A static method belongs to the class namespace, but it DOES NOT receive
# the special 'self' (instance) or 'cls' (class) parameter automatically.
#
# Use static methods for helper functions that:
# - don't need to read or modify instance state (self)
# - don't need to read or modify class state (cls)

# The method is logically related to the class, but doesn’t need access to class or instance state.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(number):
        return number % 2 == 0


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

# ------------------------------------------------------------
# 2) Static methods as validators/utilities used by other methods
# ------------------------------------------------------------
# A common pattern is to keep small, reusable logic as a static method
# and call it from __init__, classmethods, or instancemethods.

class User:
    def __init__(self, username):
        if User.is_valid_username(username):
            self.username = username
        else:
            print("Invalid username. Falling back to 'guest'.")
            self.username = "guest"

    def info(self):
        return f"User(username='{self.username}')"

    @staticmethod
    def is_valid_username(username):
        # Rule: letters/numbers only and length 3..15 (inclusive)
        return username.isalnum() and 3 <= len(username) <= 15


# ------------------------------------------------------------
# 3) Comparing instance, class, and static methods together
# ------------------------------------------------------------
# - Instance method: uses 'self' (per-object data)
# - Class method: uses 'cls' (class-level, works well for alternative constructors)
# - Static method: no automatic 'self' or 'cls' (pure helper)

class Circle:
    pi = 3.14159  # class variable (shared default)

    def __init__(self, radius):
        self.radius = radius

    # Instance method: needs per-object data
    def area(self):
        return Circle.pi * (self.radius ** 2)

    # Class method: great for alternative constructors
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    # Static method: pure function that does not touch class or instance state
    @staticmethod
    def circle_area(radius):
        return 3.14159 * (radius ** 2)


# ------------------------------------------------------------
# 4) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Static Methods: Utility Helpers (MathUtils) ===")
    print(f"2 + 3 = {MathUtils.add(2, 3)}")
    print(f"Is 10 even? {MathUtils.is_even(10)}")

    # Static methods can also be called from an instance, but that's less common
    mu = MathUtils()
    print(f"2 + 8 (via instance) = {mu.add(2, 8)}")
    print()

    print("=== Static Methods as Validators (User) ===")
    u1 = User("kody")
    u2 = User("a!")  # invalid per our simple rule
    print(u1.info())
    print(u2.info())
    # You can also call the validator directly without any object
    print(f"Is 'alex123' valid? {User.is_valid_username('alex123')}")
    print()

    print("=== Instance vs Class vs Static (Circle) ===")
    c1 = Circle(10)
    print(f"c1.area() using instance radius: {c1.area()}")

    c2 = Circle.from_diameter(20)
    print(f"c2.radius from diameter 20: {c2.radius}")
    print(f"c2.area(): {c2.area()}")

    # Static method does not need an instance
    print(f"Circle.circle_area(5): {Circle.circle_area(5)}")
    # You technically can call it via an instance, but it's just sugar
    print(f"c1.circle_area(5) (via instance): {c1.circle_area(5)}")
    print()

    print("=== Key Takeaways ===")
    print("- Use instance methods when you need per-object data (self)")
    print("- Use class methods for class-level behavior and alt constructors (cls)")
    print("- Use static methods for standalone helpers with no self/cls")


