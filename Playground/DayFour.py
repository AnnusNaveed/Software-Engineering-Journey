# Program 1 — Greeting System
def line():
    print("-" * 34)


def greet(name):
    line()
    print("Welcome to Software Engineering Journey")
    print(f"Hello, {name}!")
    print("Have a great learning session!")
    line()
    print()


line()
print("Program 1 — Greeting System")
line()
user_name = input("Please enter your name: ")
greet(user_name)


# Program 2 — Modular Calculator
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


line()
print("Program 2 — Modular Calculator")
line()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
line()

print("Addition =", add(num1, num2))
print("Subtraction =", subtract(num1, num2))
print("Multiplication =", multiply(num1, num2))
print(f"Division = {divide(num1, num2)}\n")


# Program 3 — Student Result System
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A+"
    elif marks >= 80 and marks < 90:
        return "A"
    elif marks >= 70 and marks < 80:
        return "B"
    elif marks >= 60 and marks < 70:
        return "C"
    elif marks >= 50 and marks < 60:
        return "D"
    elif marks >= 0 and marks < 50:
        return "F"
    else:
        return "Invalid marks. Please enter a value between 0 and 100."


line()
print("Program 3 — Student Result System")
line()
student_name = input("Enter the student's name: ")
marks = float(input("Enter the student's marks (0-100): "))
grade = calculate_grade(marks)

print("\n----- Result -----")
print("Student Name:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print(
    "Pass / Fail:",
    (
        "Pass"
        if marks >= 50 and marks in [50, 100]
        else (
            "Fail"
            if marks < 50 and marks in [0, 49]
            else "Invalid marks. Please enter a value between 0 and 100."
        )
    ),
)
(
    print("Percentage:", marks, "%")
    if marks in [0, 100]
    else print("Percentage: Invalid marks. Please enter a value between 0 and 100.")
)
print(
    "Remarks:",
    (
        "Excellent"
        if grade in ["A+", "A"]
        else (
            "Good"
            if grade == "B"
            else (
                "Average"
                if grade == "C"
                else "Needs Improvement" if grade == "D" else "Fail"
            )
        )
    ),
)


# Program 4 — Geometry Calculator
PI = 3.14159


def rectangle_area(length, width):
    return length * width


def circle_area(radius):
    return PI * radius**2


def triangle_area(base, height):
    return 0.5 * base * height


line()
print("Program 4 — Geometry Calculator")
line()
print("Rectangle Area:", rectangle_area(5, 3))
print("Circle Area:", circle_area(5))
print("Triangle Area:", triangle_area(5, 3))


# Program 5 — Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


line()
print("Program 5 — Temperature Converter")
line()
while True:
    line()
    print("Welcome to Temperature Converter Menu!")
    line()
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        temperature = float(input("Enter the temperature: "))
        print("Celsius to Fahrenheit:", celsius_to_fahrenheit(temperature))
    elif choice == "2":
        temperature = float(input("Enter the temperature: "))
        print("Fahrenheit to Celsius:", fahrenheit_to_celsius(temperature))
    elif choice == "3":
        print("Exiting the program.")
        line()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
