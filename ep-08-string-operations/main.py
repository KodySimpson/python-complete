# Episode 8: String Operations in Python

# Section 1: Creating Strings

# Single quotes
single_quoted = 'Hello World'
print("Single quotes:", single_quoted)

# Double quotes
double_quoted = "Hello World"
print("Double quotes:", double_quoted)

# Triple quotes for multiline strings
multiline = """This is a
multiline string
that spans multiple lines"""
print("Multiline string:")
print(multiline)

# Escape characters: A way to insert special characters into a string
#  or to add quotes without conflict with the string
print("New line:\nThis is on a new line")
print("Tab:\tThis is tabbed")
print("Quote: \"This is in quotes\"")
print("Single quote: 'It\'s a nice day'")
print("Backslash: \\This has a backslash")

# Section 2: String Concatenation

# String concatenation (joining strings together)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

# You can concatenate strings with the + operator
greeting = "Hello, " + "World!"
print(greeting)

# You can also use the += operator to append to a string
message = "Welcome to "
message += "Python programming!"
print(message)

# Section 3: String Methods

# Converting case
text = "Hello World"
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())

# Removing whitespace
messy_text = "   Hello World   "
print("Original:", repr(messy_text))  # repr() shows whitespace
print("Stripped:", repr(messy_text.strip()))
print("Left stripped:", repr(messy_text.lstrip()))
print("Right stripped:", repr(messy_text.rstrip()))

# Isdigit()
print("Isdigit:", "123".isdigit())
print("Isdigit:", "123a".isdigit())

# Replacing text
sentence = "I love Java programming"
new_sentence = sentence.replace("Java", "Python")
print("Original:", sentence)
print("Replaced:", new_sentence)

# Section 4: String Indexing and Slicing

# String indexing (accessing individual characters)
text = "Python"
print("Text:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("Second character:", text[1])

# String slicing (getting substrings)
print("First 3 characters:", text[0:3])  # or text[:3]
print("Last 3 characters:", text[-3:])
print("Characters 1 to 4:", text[1:4])
print("Every second character:", text[::2])

# Section 5: String Length

# Getting string length
text = "Hello World"
print("Text:", text)
print("Length:", len(text))

# Section 6: Splitting and Joining

# Splitting strings
sentence = "Python is a great programming language"
words = sentence.split()
print("Original sentence:", sentence)
print("Split into words:", words)

# Joining strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print("Words:", words)
print("Joined sentence:", sentence)