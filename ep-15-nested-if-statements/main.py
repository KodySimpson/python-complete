# Episode 13: Nested If Statements in Python

# Section 1: Basic Nested If Statements

# If statements inside other if statements
age = 25
if age >= 18:
    print("You are old enough to drive.")
    if age >= 21:
        print("You can also drink alcohol.")
    else:
        print("You cannot drink alcohol yet.")

# Another simple example
is_raining = True
if is_raining:
    print("It's raining outside.")
    if is_raining:
        print("Bring an umbrella!")

# Section 2: Nested If-Else Statements

# Nested if-else with multiple levels
age = 25
has_license = True
has_car = False

if age >= 18:
    print("You are old enough to drive.")
    if has_license:
        print("You have a license.")
        if has_car:
            print("You can drive your car!")
        else:
            print("You can drive, but you need a car.")
    else:
        print("You need to get a license first.")
else:
    print("You are too young to drive.")

# Section 3: Nested If-Elif-Else Statements

# Complex nested structure with elif
temperature = 75
is_weekend = True
has_money = False

if temperature > 70:
    print("The weather is nice!")
    if is_weekend:
        print("It's the weekend too!")
        if has_money:
            print("Perfect day for shopping!")
        else:
            print("Good day for a free walk in the park.")
    else:
        print("Too bad it's a weekday.")
        if has_money:
            print("Maybe go out for lunch.")
        else:
            print("Enjoy the weather from your window.")
else:
    print("The weather is not so nice.")
    if is_weekend:
        print("Weekend plans might need to change.")
    else:
        print("At least you're working anyway.")

# Section 4: Nested If Statements with Input

# Get user input and use nested if statements
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"

if age >= 18:
    print("You are old enough to enter.")
    if has_ticket:
        print("You have a ticket.")
        has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
        if has_id:
            print("Welcome! You can enter.")
        else:
            print("You need to show ID to enter.")
    else:
        print("You need to buy a ticket first.")
else:
    print("You are too young to enter.")
    if has_ticket:
        print("You have a ticket, but you're too young.")
        is_with_parent = input("Are you with a parent? (yes/no): ").lower() == "yes"
        if is_with_parent:
            print("You can enter with your parent.")
        else:
            print("You need to be with a parent to enter.")
    else:
        print("You need both a ticket and to be with a parent.")

# Section 5: Practical Exercise

############
## Exercise: Create a movie theater access system
print("=== Movie Theater Access System ===")

# Get user information
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
movie_rating = input("What is the movie rating? (G/PG/PG-13/R): ").upper()

# Check access based on age, ticket, and movie rating
print(f"\n=== Access Check ===")

if has_ticket:
    print("✓ You have a ticket.")
    if age >= 18:
        print("✓ You are an adult.")
        if movie_rating == "R":
            print("✓ You can watch R-rated movies.")
            print("Access granted for R-rated movie!")
        elif movie_rating == "PG-13":
            print("✓ You can watch PG-13 movies.")
            print("Access granted for PG-13 movie!")
        elif movie_rating == "PG":
            print("✓ You can watch PG movies.")
            print("Access granted for PG movie!")
        elif movie_rating == "G":
            print("✓ You can watch G-rated movies.")
            print("Access granted for G-rated movie!")
        else:
            print("✗ Invalid movie rating.")
    else:
        print("✗ You are under 18.")
        is_with_parent = input("Are you with a parent? (yes/no): ").lower() == "yes"
        if is_with_parent:
            print("✓ You are with a parent.")
            if movie_rating == "R":
                print("✗ Even with a parent, you cannot watch R-rated movies.")
            elif movie_rating == "PG-13":
                print("✓ With a parent, you can watch PG-13 movies.")
                print("Access granted for PG-13 movie!")
            elif movie_rating == "PG":
                print("✓ With a parent, you can watch PG movies.")
                print("Access granted for PG movie!")
            elif movie_rating == "G":
                print("✓ With a parent, you can watch G-rated movies.")
                print("Access granted for G-rated movie!")
            else:
                print("✗ Invalid movie rating.")
        else:
            print("✗ You need to be with a parent.")
            if movie_rating == "G":
                print("✓ You can watch G-rated movies without a parent.")
                print("Access granted for G-rated movie!")
            else:
                print("✗ You need a parent for this movie rating.")
else:
    print("✗ You need a ticket to enter.")
    print("Please purchase a ticket first.") 