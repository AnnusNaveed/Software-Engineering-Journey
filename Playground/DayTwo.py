# Program 1 — Age Checker
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Program 2 — Positive Negative Zero
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Program 3 — Student Grade
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 0 and marks < 60:
    print("Grade: F")

# Program 4 — Login System
username = str(input("Enter username: "))
password = int(input("Enter password: "))
if username == "admin":
    if password == 1234:
        print("Login successful.")
    else:
        print("Incorrect credentials.")

# Program 5 — Largest Number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)

