"""
Episode 33: Inheritance

In this episode you'll learn:
- What inheritance is and why to use it
- How to create a subclass and call super().__init__
- How to override methods in subclasses
- Using isinstance/issubclass and a quick look at MRO
"""

# ------------------------------------------------------------
# 1) The idea: reuse and specialize behavior
# ------------------------------------------------------------
# Inheritance lets one class (a subclass) reuse and specialize another
# class (a base class). It helps avoid duplication and express "is-a"
# relationships.

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def get_description(self) -> str:
        return f"{self.year} {self.make} {self.model}"

    def accelerate(self, amount: int = 10):
        self.speed += amount
        print(f"{self.get_description()} accelerates by {amount}. Speed = {self.speed}")

    def brake(self, amount: int = 10):
        self.speed = max(0, self.speed - amount)
        print(f"{self.get_description()} brakes by {amount}. Speed = {self.speed}")


# ------------------------------------------------------------
# 2) Subclassing: ElectricCar extends Car
# ------------------------------------------------------------
# ElectricCar is a kind of Car (an "is-a" relationship). It reuses Car's
# attributes and behavior, and adds battery-specific details.

class ElectricCar(Car):
    # If a subclass defined __init__, it no longer calls the base __init__ automatically. You
    # must call it explicitly with super() if you want to use the parent's initialization logic.
    def __init__(self, make: str, model: str, year: int, battery_kwh: int):
        # Call the base initializer to ensure base fields are set
        super().__init__(make, model, year)
        self.battery_kwh = battery_kwh
        self.charge = 100  # percentage

    # Override a method to specialize behavior
    def accelerate(self, amount: int = 10):
        # Keep base acceleration behavior
        super().accelerate(amount)
        # Add extra behavior: drain a bit of battery when accelerating
        drain = max(1, amount // 10)
        self.charge = max(0, self.charge - drain)
        print(f"Battery drains by {drain}%. Charge = {self.charge}%")

    def plug_in(self):
        self.charge = 100
        print(f"{self.get_description()} charged to 100%")


# ------------------------------------------------------------
# 3) Another example: BankAccount hierarchy
# ------------------------------------------------------------
# Demonstrates two different subclasses specializing a shared base class.

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"{self.owner}: deposited ${amount:.2f}. Balance = ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        if amount > self.balance:
            print(f"{self.owner}: insufficient funds. Balance = ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"{self.owner}: withdrew ${amount:.2f}. Balance = ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        # Reuse base behavior to credit interest
        self.deposit(interest)
        print(f"{self.owner}: interest applied at {self.interest_rate*100:.1f}%")


class CheckingAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0.0, overdraft_limit: float = 0.0, transaction_fee: float = 1.0):
        super().__init__(owner, balance)
        self.overdraft_limit = float(overdraft_limit)
        self.transaction_fee = float(transaction_fee)

    # Override withdraw: allow overdraft up to limit and charge a fee
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        total = amount + self.transaction_fee
        if self.balance - total < -self.overdraft_limit:
            print(f"{self.owner}: overdraft limit exceeded. Balance = ${self.balance:.2f}")
            return
        self.balance -= total
        print(
            f"{self.owner}: withdrew ${amount:.2f} (+${self.transaction_fee:.2f} fee). Balance = ${self.balance:.2f}"
        )


# ------------------------------------------------------------
# 4) isinstance, issubclass, and MRO
# ------------------------------------------------------------
# - isinstance(obj, Class) -> True if obj is an instance of Class or a subclass
# - issubclass(Sub, Base) -> True if Sub derives from Base
# - .mro() (method resolution order) shows the order Python uses to find methods


def demo_type_checks(car):
    print("isinstance checks:")
    print("- car is Car:", isinstance(car, Car))
    print("- car is ElectricCar:", isinstance(car, ElectricCar))
    print()


# ------------------------------------------------------------
# 5) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Base class behavior ===")
    car = Car("Toyota", "Corolla", 2021)
    print(car.get_description())
    car.accelerate()
    car.brake()
    print()

    print("=== Subclass overrides + super() ===")
    ev = ElectricCar("Tesla", "Model 3", 2024, battery_kwh=75)
    print(ev.get_description())
    ev.accelerate(20)  # uses subclass override and calls super()
    ev.brake(5)
    ev.plug_in()
    print()

    print("=== BankAccount hierarchy ===")
    sav = SavingsAccount("Dana", 1000.0, interest_rate=0.05)
    sav.apply_interest()
    sav.withdraw(200)
    chk = CheckingAccount("Eli", 200.0, overdraft_limit=100.0, transaction_fee=2.0)
    chk.withdraw(250)  # within overdraft + fee
    chk.withdraw(100)  # likely exceeds remaining overdraft
    print()

    print("=== isinstance / issubclass / MRO ===")
    demo_type_checks(ev)
    print("issubclass(ElectricCar, Car):", issubclass(ElectricCar, Car))
    print("MRO for ElectricCar:", [cls.__name__ for cls in ElectricCar.mro()])
    print()

    print("=== When to use what ===")
    print("- Use inheritance for clear 'is-a' relationships that reuse behavior.")

    print("\n=== Try it yourself ===")
    print("1) Create a SportsCar subclass that accelerates faster than Car.")
    print("2) Add a Truck subclass with 'payload_kg' and override brake to slow more.")
    print("3) Override __str__ in your subclasses to customize printing.")
