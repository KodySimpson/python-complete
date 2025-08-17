# Episode 23: Classes and Objects (Basics)

# In Python, a class is a blueprint for modeling real-world things.
# An object is an instance of a class.
# We'll start with the basics: defining a class, creating objects, attributes, and methods.

## Defining a Class

class Car:
    # The __init__ method is a special method that is called when an object is created.
    # if you are familiar with other programming languages, it is similar to the constructor.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    # Methods are functions that are defined inside a class.
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating...")
        self.speed += 10

    def brake(self):
        print(f"{self.make} {self.model} is braking...")
        self.speed -= 10

# Now that we have defined the blueprint(class), we can create objects from it.

my_car = Car("Tesla", "Model 3", 2025)
car2 = Car("Toyota", "Corolla", 2020)

# We can call methods on the object.
print(my_car.get_description())

# We can access attributes on the object.
print(f"My car is going {my_car.speed} mph")
my_car.accelerate()
my_car.accelerate()
print(f"My car is going {my_car.speed} mph")
my_car.brake()
print(f"My car is going {my_car.speed} mph")

## Another example

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} to {self.owner}'s account. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance. {self.owner} has {self.balance} in their account.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.owner}'s account. New balance is {self.balance}")

# Now that we have defined the blueprint(class), we can create objects from it.

my_account = BankAccount("John Doe", 1000)
print(f"My account balance is {my_account.balance}")
my_account.deposit(500)
my_account.withdraw(200)
print(f"My account balance is {my_account.balance}")

# We can also create multiple objects from the same class.

account1 = BankAccount("Jane Doe", 500)
account2 = BankAccount("Jim Doe", 1000)

account1.deposit(100)
account2.withdraw(200)

print(f"Account 1 balance is {account1.balance}")
print(f"Account 2 balance is {account2.balance}")