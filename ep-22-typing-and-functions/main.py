# Episode 22: Type Hints with Functions in Python

# Type hints let you annotate function parameters and return values with
# expected types. They make code easier to read and help tools catch mistakes.

# Section 1: Basic Parameter and Return Type Hints

def add(a: int, b: int) -> int:
    return a + b

sum_result: int = add(10, 20)
print(f"add(10, 20) -> {sum_result}")

def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

message: str = get_greeting("Alice")
print(message)

# A function that returns nothing can be annotated with `-> None`
def greet(name: str) -> None:
    print(f"Hi, {name}")

greet("Bob")

# Section 2: Type Hints with Lists

# You can annotate list element types using list[ElementType]
def double_numbers(numbers: list[int]) -> list[int]:
    doubled: list[int] = []
    for n in numbers:
        doubled.append(n * 2)
    return doubled

original_numbers: list[int] = [1, 2, 3, 4]
doubled_numbers = double_numbers(original_numbers)
print(f"Original: {original_numbers}")
print(f"Doubled: {doubled_numbers}")

# Section 3: Type Hints with Tuples and Multiple Returns

# When a function returns multiple values, Python packs them into a tuple.
# You can annotate the exact tuple shape using tuple[Type1, Type2, ...]
def calculate_rectangle(length: float, width: float) -> tuple[float, float]:
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

rect_area, rect_perimeter = calculate_rectangle(10.0, 5.0)
print(f"Rectangle 10x5 => Area={rect_area}, Perimeter={rect_perimeter}")

# Section 4: Combining with Previous Concepts

def is_even(number: int) -> bool:
    return number % 2 == 0

print(f"4 is even? {is_even(4)}")
print(f"7 is even? {is_even(7)}")

# Section 5: Practical Exercise

############
## Exercise: Add type hints to these functions and test them
print("=== Typed Statistics ===")

def parse_numbers_csv(text: str) -> list[int]:
    parts = text.split(",")
    numbers: list[int] = []
    for p in parts:
        p = p.strip()
        if p:
            numbers.append(int(p))
    return numbers

def stats_min_max_avg(numbers: list[int]) -> tuple[int, int, float]:
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for value in numbers:
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value
        total += value
    average = total / len(numbers)
    return minimum, maximum, average

user_input = input("Enter comma-separated integers (e.g., 3, 1, 9, 4): ")
nums = parse_numbers_csv(user_input)
mn, mx, avg = stats_min_max_avg(nums)
print(f"Numbers: {nums}")
print(f"Min: {mn}, Max: {mx}, Avg: {avg:.2f}")


