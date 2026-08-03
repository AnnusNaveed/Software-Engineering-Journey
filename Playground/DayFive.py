def line():
    print("-" * 32)


print("=" * 32)
print("\tPrograms Development")
print("=" * 32)

# Program 1 — String Basics Utility
"""Take the user's name and display useful information."""
line()
print("Program 1 — String Basics Utility")
line()

name = input("Enter Your Full Name: ")
print("\n------ String Information ------")

print(f"Original Name : {name}")
print(f"Uppercase     : {name.upper()}")
print(f"Lowercase     : {name.lower()}")
print(f"Title Case    : {name.title()}")
print(f"Characters    : {len(name)}")
print(f"Words         : {len(name.split())}")

# Program 2 — Palindrome Checker
"""A palindrome reads the same forward and backward."""
line()
print("Program 2 — Palindrome Checker")
line()

word = input("Enter a Word: ").lower()

if word == word[::-1]:  # new concept used for the reverse of string/sequence
    print("Palindrome")
else:
    print("Not Palindrome")

# Program 3 — Password Validator
"""Rules
Password must have:
Minimum 8 characters
At least one uppercase letter
At least one lowercase letter
At least one digit"""
line()
print("Program 3 — Password Validator")
line()

print("=" * 45)
print("Professional Password Strength Checker")
print("=" * 45)

special_characters = "!@#$%^&*()_-+=<>?/{}[]|\\:;\"'.,~`"

while True:

    password = input("Enter Password: ")
    line()

    # ----------------------------
    # Basic Validation
    # ----------------------------

    if password == "":
        print("Password cannot be empty.\n")
        continue

    if " " in password:
        print("Password cannot contain spaces.\n")
        continue

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # ----------------------------
    # Check Each Character
    # ----------------------------

    for character in password:

        if character.isupper():
            has_upper = True

        if character.islower():
            has_lower = True

        if character.isdigit():
            has_digit = True

        if character in special_characters:
            has_special = True

    # ----------------------------
    # Password Score
    # ----------------------------

    score = 0

    if len(password) >= 8:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    # ----------------------------
    # Display Missing Requirements
    # ----------------------------

    if len(password) < 8:
        print("Password should contain at least 8 characters.")

    if not has_upper:
        print("Missing Uppercase Letter.")

    if not has_lower:
        print("Missing Lowercase Letter.")

    if not has_digit:
        print("Missing Digit.")

    if not has_special:
        print("Missing Special Character.")

    # ----------------------------
    # Password Rating
    # ----------------------------

    print("\nPassword Strength:")

    if score == 5:
        print("⭐⭐⭐⭐⭐ Excellent Password")
        print("Password Accepted.")
        break

    elif score == 4:
        print("⭐⭐⭐⭐ Strong Password")

    elif score == 3:
        print("⭐⭐⭐ Medium Password")

    elif score == 2:
        print("⭐⭐ Weak Password")

    else:
        print("⭐ Very Weak Password")
    line()
    print("\nPlease try again.\n")

# Program 4 — Email Validator
"""
Check whether an email follows a basic format.
Rules
Contains @
Ends with .com """

line()
print("Program 4 — Email Validator")
line()

while True:
    email = input("Enter your email :").strip()
    if "@" in email and email.endswith(".com"):
        print("Valid Email")
        print("--------Terminated--------")
        break
    else:
        print("Invalid Email ! Try Again")
        line()

# Program 5 — Text Analyzer
line()
print("Program 5 — Text Analyzer")
line()

text = input("Enter Text: ")
print("\n------ Analysis ------")
print("Characters :", len(text))
print("Words :", len(text.split()))
print("Uppercase :", text.upper())
print("Lowercase :", text.lower())
