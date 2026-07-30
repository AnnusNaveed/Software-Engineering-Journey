# Truthy & Falsy Practice

# Program 0.1 — Empty String Check
name = input("Enter your name: ")

if name:
    print("Welcome,", name)
else:
    print("Name cannot be empty.")

# Program 0.2 — Number Check
number = int(input("Enter a number: "))
if number:
    print("Non zero number:", number)
else:
    print("The number is zero.")

# Program 0.3 — List Check
subjects = ["python", "git"]

if subjects:
    print("Subjects available.", subjects)
else:
    print("No subjects found.")

# Program 0.4 — Boolean Toggle
is_raining = False
if is_raining:
    print("It's raining. Don't forget your umbrella!")
else:
    print("It's not raining. Enjoy your day!")

# Mini Challenge: A program that checks whether the user entered a name.
name = input("Enter your name: ")
if name:
    print("Welcome,", name)
else:
    print("Please enter your name")

trusty = bool(input("Enter a boolean value (True/False): "))
if trusty:
    print("You entered a truthy value.")
else:
    print("You entered a falsy value.")
