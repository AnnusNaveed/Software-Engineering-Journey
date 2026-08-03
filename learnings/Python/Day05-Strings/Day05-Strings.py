# Part 1 — Creating Strings
print("-" * 32)
print("Part 1 — Creating Strings")
print("-" * 32)

name = "Sara"
email = "sara@23.com"
print(name)
print(email)

# Part 2 — String Indexing
print("-" * 32)
print("Part 2 — String Indexing")
print("-" * 32)

language = "Python"
print(language[0])  # P
print(language[1])  # y
print(language[2])  # t
print(language[3])  # h
print(language[4])  # o
print(language[5] + "\n")  # n
print(language[-1])  # n
print(language[-2])  # o

# Visual
"""
 Python
 
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5

 -6 -5 -4 -3 -2 -1
"""

# Part 3 — String Slicing
print("-" * 32)
print("Part 3 — String Slicing")
print("-" * 32)

text = "Python is a programming language"
print(text[0:6])  # Python
print(text[7:23])  # is
print(text[10:20])  # a programming
print(text[24:32])  # language
print(text[0:])  # Python is a programming language
print(text[-32:])  # Python is a programming language

# Part 4 — Length of String
print("-" * 32)
print("Part 4 — Length of String")
print("-" * 32)

course = "Software Engineering"
print("Length = " + str(len(course)))  # 20

# Part 5 — String Concatenation
print("-" * 32)
print("Part 5 — String Concatenation")
print("-" * 32)

first = "Software"
second = "Engineering"

full = first + " " + second
print(full)

# Part 6 — String Repetition
print("=" * 45)
print("Part 6 — String Repetition")
print("=" * 45)

print("Python " * 5)

# Part 7 — Membership Operators
print("-" * 32)
print("Part 7 — Membership Operators")
print("-" * 32)

sentence = "Python is a programming language"
print("Python" in sentence)  # True
print("Java" in sentence)  # False

print("Python" not in sentence)  # False
print("Java" not in sentence)  # True
print("Python" in sentence and "Java" not in sentence)  # True
print("Python" in sentence or "Java" not in sentence)  # True
print("Python is a programming language 2" in sentence)  # False

# Part 8 — Case Conversion
print("-" * 32)
print("Part 8 — Case Conversion")
print("-" * 32)

text = "software engineering"
print(f"Upper Case: {text.upper()}")  # SOFTWARE ENGINEERING
print(f"Lower Case: {text.lower()}")  # software engineering
print(f"Title Case: {text.title()}")  # Software Engineering
print(f"Capitalized: {text.capitalize()}")  # Software engineering
print(f"Swap Case: {text.swapcase()}")  # SOFTWARE ENGINEERING
print(
    f"Casefold: {text.casefold()}"
)  # coverts string to lowercase for case insensitive comparisons, more aggressive than lower()).
print(f"Is Upper: {text.isupper()}")  # False
print(f"Is Lower: {text.islower()}")  # True
print(f"Is Title: {text.istitle()}")  # False
print(f"Is Alpha: {text.isalpha()} , Because it contains spaces")  # False
print(f"Is Digit: {text.isdigit()}")  # False
print(f"Is All Numbers : {text.isalnum()} , Because it contains spaces")  # False

# Part 9 — Remove Spaces
print("-" * 32)
print("Part 9 — Remove Spaces")
print("-" * 32)

name = "   Sara   "
print(f"Before Strip: '{name}'")
print(f"After LStrip: '{name.lstrip()}'")
print(f"After RStrip: '{name.rstrip()}'")
print(f"After Strip: '{name.strip()}'")


# Part 10 — Replace Text
print("-" * 32)
print("Part 10 — Replace Text")
print("-" * 32)

text = "I like Python programming"
print(f"Before Replace: {text}")
print(f"After Replace: {text.replace('Python', 'Java')}")
"""Note: The replace() method does not change the original string. It returns a new string with the replaced values."""
print("Original Text:", text)

# Part 11 — Find Text
print("-" * 32)
print("Part 11 — Find Text")
print("-" * 32)

text = "Software Engineering"
# True with the index of first occurrence of substring if found else -1
print(text.find("Software"))  # position is 0
print(text.find("Engineering"))  # position is 9
print(text.find("engineering"))  # False with -1 value
print(text.find("Python"))  # False with -1 value

# Part 12 — Count Characters
print("-" * 32)
print("Part 12 — Count Characters")
print("-" * 32)

word = "banana"
print(word.count("b"))
print(word.count("a"))
print(word.count("n"))

# Part 13 — Split
print("-" * 32)
print("Part 13 — Split")
print("-" * 32)

languages = "Python Java C++"
result = languages.split()
print(result)

# Part 14 — Join
print("-" * 32)
print("Part 14 — Join")
print("-" * 32)

letters = ["P", "Y", "T", "H", "O", "N"]
print("Before join :", letters)
word = "-".join(letters)
print("After join :", word)

# Part 15 — startswith() & endswith()
print("-" * 32)
print("Part 15 — startswith() & endswith()")
print("-" * 32)

filename = "report.pdf"
print(filename.startswith("report"))  # True
print(filename.startswith("..."))  # False
print(filename.endswith("df"))  # True

# Part 16 — Validation Methods
print("-" * 32)
print("Part 16 — Validation Methods")
print("-" * 32)

print("Python".isalpha())  # True
print("12345".isdigit())  # True
print("Python123".isalnum())  # True
print("Python 123".isalnum())  # False

# Part 17 — f-Strings
print("-" * 32)
print("Part 17 — f-Strings")
print("-" * 32)

name = "Ali"
age = 22
print(f"Your name is '{name}' & your age is '{age}' ")

# Part 18 — Escape Characters
print("-" * 32)
print("Part 18 — Escape Characters")
print("-" * 32)

print('1. He said "Hello" ')
print("2. Python\nProgramming")
print("3. Name\tAge")

# Part 19 — Raw Strings
print("-" * 32)
print("Part 19 — Raw Strings")
print("-" * 32)

path = r"C:\Users\Annus\Documents"
print(path)

# Part 20 — Immutability
print("-" * 32)
print("Part 20 — Immutability")
print("-" * 32)

name = "Python"
# name[0] = "J"  TypeError
name = "Mara" + name[2:]
print(name)

"""Challenge Practice"""
print("=" * 32)
print("\tChallenge Practice")
print("=" * 32)

# Challenge 1: Print the first and last character of your name.
print("Challenge 1")
print("-" * 32)

name = "Annus"
print("The first character is : ", name[0])
print("The last character is : ", name[4])


# Challenge 2: Ask the user for their full name and print it in UPPERCASE.
print("-" * 32)
print("Challenge 2")
print("-" * 32)

full_name = input("Enter your full name :")
print("The UPPERCASE is :", full_name.upper())

# Challenge 3
"""Ask the user for a sentence and print:
Number of characters
Number of words
Hint: Use len() and split()."""

print("-" * 32)
print("Challenge 3")
print("-" * 32)

sentence = input("Enter the sentence  :")
print(f"1. Number of characters :{len(sentence)}")
print(
    f"2. Number of Words  :{sentence.split()} \n\tand length ={len(sentence.split())}"
)

# Challenge 4
"""Replace every space with _
Example:
Software Engineering Journey
Output:
Software_Engineering_Journey"""

print("-" * 32)
print("Challenge 3")
print("-" * 32)

string = "Software Engineering Journey"
print("Before Replacement :", string)
print(f"After Replacement :{string.replace(' ','_')}")

# Challenge 5
"""Check whether a filename ends with .pdf.
Example:
Input:
resume.pdf
Output:
Valid PDF"""

print("-" * 32)
print("Challenge 5")
print("-" * 32)

while True:
    enter = input("Input File: ")
    if enter.endswith(".pdf"):
        print("Valid PDF")
        break
    else:
        print("Invalid PDF. Try again.\n")

"""⭐ Bonus Challenge
Ask the user for an email address.
Print:
Username (before @)
Domain name (after @)
Example:
Input:
annus@gmail.com
Output:
Username : annus
Domain : gmail.com
Hint: Use split("@")."""

print("=" * 32)
print("⭐ Bonus Challenge")
print("=" * 32)

enter = input("Enter an email address: ")

if enter.count("@") == 1:
    parts = enter.split("@")

    if parts[0] and parts[1]:
        print(f"Username : {parts[0]}")
        print(f"Domain   : {parts[1]}")
    else:
        print("Username or Domain cannot be empty.")
else:
    print("Invalid email address.")

# All case coverage program
print("=" * 32)
print("⭐ Bonus Challenge")
print("=" * 32)

while True:
    email = input("Enter an email address: ").strip()

    # Must contain exactly one '@'
    if email.count("@") != 1:
        print("Email must contain exactly one '@'.\n")
        continue

    username, domain = email.split("@")

    # Username missing
    if username == "":
        print("Username cannot be empty.\n")
        continue

    # Domain missing
    if domain == "":
        print("Domain cannot be empty.\n")
        continue

    # Domain must contain '.'
    if "." not in domain:
        print("Domain must contain a '.' (e.g., gmail.com).\n")
        continue

    # Domain starts with '.'
    if domain.startswith("."):
        print("Domain cannot start with '.'.\n")
        continue

    # Domain ends with '.'
    if domain.endswith("."):
        print("Domain cannot end with '.'.\n")
        continue

    print("\nValid Email Address")
    print(f"Username : {username}")
    print(f"Domain   : {domain}")
    break
