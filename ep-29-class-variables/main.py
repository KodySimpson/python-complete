"""
Episode 24: Instance & Class Variables (with method usage)

This script is a self-contained tutorial:
- What instance variables are and how they differ from class variables
- How to reference class variables in __init__ and instance methods
- How changing class variables affects all instances (unless overridden)
- Using a class variable as a shared counter
- Using self.__class__ to respect inheritance overrides
"""

# ------------------------------------------------------------
# 1) Instance Variables
# ------------------------------------------------------------
# Instance variables belong to each object (instance) of a class
# and are usually set inside __init__ via 'self'.

class Dog:
    # Class variable (shared) for demonstration later
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables (unique per object)
        self.name = name
        self.breed = breed


# ------------------------------------------------------------
# 2) Class Variables
# ------------------------------------------------------------
# Class variables are defined in the class body and shared by all instances,
# unless overridden on a particular instance.

class Car:
    # Class variable: shared by all cars
    wheels = 4

    def __init__(self, make, model):
        # Instance variables
        self.make = make
        self.model = model

        # Referencing a class variable inside __init__:
        # Here we copy the class-level default into an instance attribute.
        # This lets us tweak per-object later without changing the class default.
        self.starting_wheels = Car.wheels

    # Using a class variable in an instance method
    def description_with_class_wheels(self):
        # This reads the current class-level default (Car.wheels).
        # If Car.wheels changes later, this will reflect that change.
        return f"{self.make} {self.model} with {Car.wheels} wheels (class-level lookup)"

    def description_with_instance_wheels(self):
        # This reads the instance attribute set in __init__.
        # It will NOT change if the class variable changes later.
        return f"{self.make} {self.model} started with {self.starting_wheels} wheels (instance snapshot)"

    def override_instance_wheels(self, new_wheels):
        # This creates/updates an INSTANCE attribute 'wheels',
        # overriding the class attribute for THIS object only.
        self.wheels = new_wheels

    def description_with_instance_override(self):
        # If 'self.wheels' exists, it hides the class attribute for this instance.
        # getattr(self, 'wheels', Car.wheels) uses instance 'wheels' if present,
        # otherwise falls back to the class default.
        effective_wheels = getattr(self, 'wheels', Car.wheels)
        return f"{self.make} {self.model} currently shows {effective_wheels} wheels (instance override if any)"


# ------------------------------------------------------------
# 3) Using Class Variables as Shared State (e.g., counters)
# ------------------------------------------------------------
# A common pattern: count how many objects were created.

class BankAccount:
    # Shared counter across all BankAccount instances
    account_count = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

        # Update the shared class-level counter
        BankAccount.account_count += 1

    def info(self):
        return f"{self.owner}'s account | balance: {self.balance}"


# ------------------------------------------------------------
# 5) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Instance vs Class Variables: Dog Example ===")
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Charlie", "Poodle")
    print(f"dog1.name: {dog1.name} | dog1.breed: {dog1.breed}")
    print(f"dog2.name: {dog2.name} | dog2.breed: {dog2.breed}")
    print(f"Shared class variable (Dog.species): {Dog.species}")
    print(f"dog1.species: {dog1.species}")
    print(f"dog2.species: {dog2.species}")
    print()

    print("=== Class Variables Used in __init__ and Methods: Car Example ===")
    car1 = Car("Tesla", "Model 3")
    car2 = Car("Toyota", "Corolla")

    # Using class variable in an instance method
    print(car1.description_with_class_wheels())     # reads Car.wheels (class-level lookup)
    print(car1.description_with_instance_wheels())  # reads instance snapshot set in __init__
    print(car2.description_with_class_wheels())
    print(car2.description_with_instance_wheels())
    print()

    print("Change the class variable Car.wheels from 4 to 6...")
    Car.wheels = 6
    print(car1.description_with_class_wheels())     # now shows 6
    print(car1.description_with_instance_wheels())  # still shows original snapshot (4)
    print(car2.description_with_class_wheels())     # shows 6
    print(car2.description_with_instance_wheels())  # still shows original snapshot (4)
    print()

    print("Override wheels on car1 at the instance level (to 8)...")
    car1.override_instance_wheels(8)
    print(car1.description_with_instance_override())  # 8 (instance override)
    print(car2.description_with_instance_override())  # 6 (class-level, since no override on car2)
    print()

    print("=== Shared Counter via Class Variable: BankAccount Example ===")
    a1 = BankAccount("Alice", 100)
    a2 = BankAccount("Bob", 200)
    a3 = BankAccount("Charlie", 300)
    print(a1.info())
    print(a2.info())
    print(a3.info())
    print(f"Total accounts created (BankAccount.account_count): {BankAccount.account_count}")
    print()

    # === Key Takeaways ===
    # - Instance variables live on each object (self.x).
    # - Class variables live on the class and are shared (ClassName.x).
    # - Referencing class vars in __init__/methods is common for defaults and consistency.
    # - Changing a class variable affects all instances unless an instance overrides it.
    # - Use self.__class__.var to respect subclass overrides (polymorphism).