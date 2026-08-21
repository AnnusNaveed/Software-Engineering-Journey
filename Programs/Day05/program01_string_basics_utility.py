def line():
    print("-" * 32)

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