def line():
    print("-" * 32)


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