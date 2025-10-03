"""
Episode 32: Properties (@property)

In this episode you'll learn:
- Why properties are useful vs raw attribute access and manual getters/setters
- How to declare a read-only property
- How to add a setter for validation/transformation
- How to add a deleter when appropriate
- When to choose properties vs methods
"""

# ------------------------------------------------------------
# 1) The problem: raw attribute access has no validation
# ------------------------------------------------------------
# Directly exposing attributes is simple, but it can allow invalid state.
# We can use properties to add validation and custom setting logic.

class RectangleRaw:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# ------------------------------------------------------------
# 2) Properties: start with a read-only computed property
# ------------------------------------------------------------
# Use @property to present a method as an attribute. Great for computed values.

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # leading underscore: internal backing field

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        # Computed read-only property
        return (self._celsius * 9 / 5) + 32


# ------------------------------------------------------------
# 3) Add a setter for validation/transformation
# ------------------------------------------------------------
# With @<prop>.setter we can validate inputs when users assign attributes.

class Rectangle:
    def __init__(self, width, height):
        self._width = 0
        self._height = 0
        self.width = width     # go through setter validation
        self.height = height   # go through setter validation

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            print("Width must be non-negative. Using 0.")
            value = 0
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            print("Height must be non-negative. Using 0.")
            value = 0
        self._height = value

    @property
    def area(self):
        # Presented as an attribute, but computed from width/height
        return self._width * self._height


# ------------------------------------------------------------
# 4) Optional: Deleter to manage lifecycle
# ------------------------------------------------------------
# @<prop>.deleter is less common, but useful for cleaning up state or denying deletion.

class Profile:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name or not new_name.strip():
            print("Name cannot be empty. Keeping previous value.")
            return
        self._name = new_name.strip()

    @name.deleter
    def name(self):
        print("Name deletion is not allowed; setting to 'anonymous' instead.")
        self._name = "anonymous"


# ------------------------------------------------------------
# 5) Properties vs Methods: guidance
# ------------------------------------------------------------
# Use a property when:
# - it reads like data (noun) and is cheap to compute
# - you want to intercept reads/writes for validation without changing the API
#
# Prefer a method when:
# - the operation is expensive, has side effects, or requires parameters


# ------------------------------------------------------------
# 6) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Raw Attributes: no validation ===")
    r_raw = RectangleRaw(10, 5)
    print(f"area: {r_raw.area()}")
    r_raw.width = -20  # no validation here -> allows impossible state
    print("Direct assignment allowed a negative width; object is now in an invalid state.")
    print(f"area after invalid width: {r_raw.area()}")
    print()

    print("=== Properties: read-only + computed ===")
    t = Temperature(25)
    print(f"celsius: {t.celsius}")
    print(f"fahrenheit (computed): {t.fahrenheit}")
    # t.fahrenheit = 100  # AttributeError if attempted; no setter defined
    print()

    print("=== Properties with setters: validation ===")
    r = Rectangle(10, 5)
    print(f"width: {r.width}, height: {r.height}, area: {r.area}")
    r.width = -3  # triggers validation
    r.height = 7
    print(f"width: {r.width}, height: {r.height}, area: {r.area}")
    print()

    print("=== Deleter example ===")
    p = Profile("Kody")
    print(f"name: {p.name}")
    del p.name  # intercepted by deleter
    print(f"name after deletion attempt: {p.name}")
    p.name = "   Alex   "
    print(f"name after setter/strip: {p.name}")
    p.name = ""  # invalid -> ignored
    print(f"name after invalid set: {p.name}")
    print()

    print("=== Key Takeaways ===")
    print("- @property turns methods into attribute-like accessors")
    print("- Add setters for validation/transformation; omit to make read-only")
    print("- Use properties for cheap, data-like access; methods for heavier work")


