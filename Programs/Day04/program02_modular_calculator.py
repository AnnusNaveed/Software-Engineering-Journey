def line():
    print("-" * 34)


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