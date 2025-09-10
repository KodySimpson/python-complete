# Episode 19: F-Strings in Python

## F-Strings: Formatted String Literals

# F-Strings are a way to format strings in Python so that you dont have 
# to string together multiple variables and strings using the + operator.

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

# the alternative:
print("My name is " + name + " and I am " + str(age) + " years old.")

## Expressions can be used in f-strings rather than just variables.
x = 10
y = 5
print(f"The sum of {x} and {y} is {x + y}")
print(f"Here is a more complex expression: {(x + y * 2) ** 3}")

title = "how to unclog your toilet"
print(f"The title of this article is {title.title()}")

## You can also use f-strings to format numbers.
price = 1000000000
print(f"The price of this item is {price:.2f}") # 2 decimal places
print(f"The price of this item is {price:,.2f}") # 2 decimal places, comma separator

## A useful shortcut:
random_variable = 45 ** 3
print(f"{random_variable=}") # includes the variable name and the value

## You can also use f-strings to format strings.
name = "John"
age = 30
print(f"{name=} {age=}")

## You can also use f-strings to format multi-line strings.
name = "Kody"
msg = f"""
Hello {name},
This is a multi-line message.
Cheers!
"""
print(msg)