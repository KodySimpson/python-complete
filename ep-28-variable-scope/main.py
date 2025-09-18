## Variable Scope in Python

# this is a global variable since it is defined outside of any function
x = 10

if 2 + 2 == 4:
    # this is also a global variable since it is defined outside of any function
    x = 20
    print(f"Inside the if block: {x}")
    
    y = 30 # this too! Weird if you are from other languages.
    
print(f"Outside the if block: {x}")
print(f"Outside the if block: {y}")

def my_function():
    x = 40 # This is a local variable (to the function) since it is defined inside a function
    print(f"Inside the function: {x}")
    
my_function()
print(f"Outside the function: {x}") # This prints the global x, not the local function x