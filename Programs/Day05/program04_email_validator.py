def line():
    print("-" * 32)

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