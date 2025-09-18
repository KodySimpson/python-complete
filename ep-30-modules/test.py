def is_ascending(numbers):
    """Returns whether the given list of numbers is in ascending order."""
    for i in range(len(numbers - 1)):
        if numbers[i+1] < numbers[i]:
            return False
    return True

print(is_ascending([1, 2, 3, 4, 5]))
print(is_ascending([5, 2, 3]))