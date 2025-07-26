# Episode 11: Boolean Logic Operators & Expressions

# Section 1: Boolean Logical Operators

# AND operator - both conditions must be True
age = 25
has_license = True
print("Age >= 18 AND has license:", age >= 18 and has_license)  # True
print("Age >= 30 AND has license:", age >= 30 and has_license)  # False

# OR operator - at least one condition must be True
is_student = True
is_employed = False
print("Is student OR employed:", is_student or is_employed)  # True
print("Is student OR is_employed:", is_student or is_employed)  # True

# NOT operator - reverses the boolean value
is_raining = True
print("Is raining:", is_raining)
print("NOT is_raining:", not is_raining)  # False

# Section 2: Combining Comparison and Logical Operators

# Using AND with comparisons
temperature = 75
humidity = 60
print("Temperature >= 70 AND humidity < 70:", temperature >= 70 and humidity < 70)  # True
print("Temperature >= 80 AND humidity < 50:", temperature >= 80 and humidity < 50)  # False

# Using OR with comparisons
age = 16
income = 25000
print("Age >= 18 OR income >= 30000:", age >= 18 or income >= 30000)  # False
print("Age >= 16 OR income >= 20000:", age >= 16 or income >= 20000)  # True

# Using NOT with comparisons
is_weekend = False
print("Is weekend:", is_weekend)
print("NOT is_weekend:", not is_weekend)  # True

# Section 3: Complex Boolean Expressions

# Multiple conditions with AND
has_id = True
has_money = True
is_old_enough = True
can_buy_alcohol = has_id and has_money and is_old_enough
print("Can buy alcohol:", can_buy_alcohol)

# Multiple conditions with OR
is_holiday = False
is_weekend = True
is_vacation = False
can_sleep_in = is_holiday or is_weekend or is_vacation
print("Can sleep in:", can_sleep_in)

# Mixing AND and OR
is_student = True
has_id = True
has_money = False
can_enter_club = (is_student and has_id) or has_money
print("Can enter club:", can_enter_club)

# Section 4: Operator Precedence and Parentheses

# Without parentheses (AND has higher precedence than OR)
result1 = True and False or True
print("True AND False OR True:", result1)  # True

# With parentheses to control order
result2 = True and (False or True)
print("True AND (False OR True):", result2)  # True

# More complex example
weather_good = True
has_time = False
has_money = True
will_go_outside = weather_good and (has_time or has_money)
print("Will go outside:", will_go_outside)  # True

# Section 5: Boolean Expressions with Input

# Get user input and create boolean expressions
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"

# Check if user can enter (age 18+ and has ticket and has ID)
can_enter = age >= 18 and has_ticket and has_id
print("Can enter:", can_enter)

# Check if user gets discount (under 12 OR over 65)
gets_discount = age < 12 or age > 65
print("Gets discount:", gets_discount)

# Check if user needs supervision (under 18 and not with parent)
is_with_parent = input("Are you with a parent? (yes/no): ").lower() == "yes"
needs_supervision = age < 18 and not is_with_parent
print("Needs supervision:", needs_supervision)

# Section 6: Practical Exercise

############
## Exercise: Create a movie theater access checker
print("=== Movie Theater Access Checker ===")

# Get user information
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
has_money = input("Do you have money for snacks? (yes/no): ").lower() == "yes"
is_with_parent = input("Are you with a parent? (yes/no): ").lower() == "yes"
movie_rating = input("What is the movie rating? (G/PG/PG-13/R): ").upper()

# Check different access criteria
can_enter_movie = has_ticket and age >= 18
can_enter_with_parent = has_ticket and age < 18 and is_with_parent
can_watch_g_rated = has_ticket and (age >= 18 or is_with_parent)
can_watch_pg_rated = has_ticket and (age >= 18 or (age >= 13 and is_with_parent))
can_watch_pg13_rated = has_ticket and (age >= 13 and (age >= 18 or is_with_parent))
can_watch_r_rated = has_ticket and age >= 17 and (age >= 18 or is_with_parent)
can_buy_snacks = has_money and (age >= 18 or is_with_parent)

# Display results
print(f"\n=== Access Results ===")
print(f"Can enter movie (18+): {can_enter_movie}")
print(f"Can enter with parent: {can_enter_with_parent}")
print(f"Can watch G-rated: {can_watch_g_rated}")
print(f"Can watch PG-rated: {can_watch_pg_rated}")
print(f"Can watch PG-13-rated: {can_watch_pg13_rated}")
print(f"Can watch R-rated: {can_watch_r_rated}")
print(f"Can buy snacks: {can_buy_snacks}")

# Provide specific feedback based on movie rating
if movie_rating == "G" and can_watch_g_rated:
    print("✓ You can watch this G-rated movie!")
elif movie_rating == "PG" and can_watch_pg_rated:
    print("✓ You can watch this PG-rated movie!")
elif movie_rating == "PG-13" and can_watch_pg13_rated:
    print("✓ You can watch this PG-13-rated movie!")
elif movie_rating == "R" and can_watch_r_rated:
    print("✓ You can watch this R-rated movie!")
else:
    print("✗ You cannot watch this movie with the current rating and your age/parental situation.") 