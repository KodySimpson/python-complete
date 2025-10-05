"""
Episode 34: Exceptions and handling them with try/except
https://docs.python.org/3/library/exceptions.html
"""

# ------------------------------------------------------------
# 0) Trigger exceptions (commented for live demo)
# ------------------------------------------------------------
# Uncomment one at a time at the start of your talk to show
# a real traceback, then re-comment to keep the script runnable.

# ZeroDivisionError
# print(1 / 0)

# ValueError
# int("not-a-number")

# KeyError
# {}["missing"]

# IndexError
# [1, 2, 3][10]

# FileNotFoundError
# open("definitely_not_here.txt", "r")

# TypeError
# len(5)

# ------------------------------------------------------------
# 1) What are exceptions?
# ------------------------------------------------------------
# Exceptions signal that something went wrong during execution.
# If unhandled, they terminate the program and print a traceback.
# We can handle them with try/except blocks to recover gracefully.


# ------------------------------------------------------------
# 2) Basic try/except with multiple exception types
# ------------------------------------------------------------
def safe_divide(a, b):
    """Divide a by b and handle common errors.

    Demonstrates:
    - catching specific exceptions (ZeroDivisionError, TypeError)
    """
    print(f"Dividing {a!r} by {b!r}...")
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: cannot divide by zero.", e)
        return None
    except TypeError as e:
        print("Error: numbers required for division.", e)
        return None
    # Success path (kept outside try so we only catch errors from a / b)
    print("Success! Result:", result)
    return result


# ------------------------------------------------------------
# 3) Handling conversion errors (ValueError)
# ------------------------------------------------------------
def parse_int(s: str):
    """Convert string to int safely, returning None on failure."""
    try:
        return int(s)
    except ValueError as e:
        print(f"Could not convert {s!r} to int:", e)
        return None


# ------------------------------------------------------------
# 4) Handling missing keys (KeyError) with a helper
# ------------------------------------------------------------
def safe_get(mapping: dict, key, default=None):
    try:
        return mapping[key]
    except KeyError:
        print(f"Key {key!r} not found; returning default {default!r}")
        return default


# ------------------------------------------------------------
# 5) Using else for success-only code
# ------------------------------------------------------------
def safe_divide_with_else(a, b):
    """Same behavior as safe_divide, but uses an else block.

    Using else keeps the try-suite minimal so only the risky operation
    is inside try. The else runs only if no exception occurred.
    """
    print(f"Dividing {a!r} by {b!r} (with else)...")
    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Error: cannot divide by zero.", e)
        return None
    except TypeError as e:
        print("Error: numbers required for division.", e)
        return None
    else:
        print("Success! Result:", result)
        return result


# ------------------------------------------------------------
# 6) Common mistakes to avoid
# ------------------------------------------------------------
# - Avoid bare `except:`; it catches KeyboardInterrupt/SystemExit too.
# - Catch the narrowest exception types you expect.
# - Don’t silently swallow exceptions; at least log or report them.


# ------------------------------------------------------------
# 7) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Exceptions: Basics ===")

    print("-- Division examples --")
    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide("10", 2)

    print("-- Conversion examples --")
    print("parse_int('42') ->", parse_int("42"))
    print("parse_int('abc') ->", parse_int("abc"))
    print()

    print("-- KeyError example --")
    data = {"name": "Kody", "role": "Teacher"}
    print("name:", safe_get(data, "name"))
    print("age:", safe_get(data, "age", default="unknown"))
    print()

    print("-- else example --")
    safe_divide_with_else(9, 3)
    safe_divide_with_else(5, 0)

    print("=== Key Takeaways ===")
    print("- Use try/except to handle specific error types you expect.")
    print("- Put success-only code in else.")
    print("- Prefer precise exceptions over bare except.")

    print("\n=== Try it yourself ===")
    print("1) Build a robust calculator that never crashes on bad input.")
    print("2) Wrap file opening to print a friendly message on FileNotFoundError.")
    print("3) Extend safe_divide to log errors to a file (hint: use try/finally).")
