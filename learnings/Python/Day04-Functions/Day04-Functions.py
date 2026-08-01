# First Function
from threading import local


def greet():
    print("Hello, welcome to the Python functions!\n")


greet()


# Calling Multiple Times
def welcome():
    print("Welcome Annus!")


welcome()
welcome()
welcome()  # one function can be reused many times


# Function with One Parameter
def greet(name):
    print(f"Hello, {name}")


print()
greet("Ali")
greet("Sara")
greet("Ahmed\n")


# Function with Multiple Parameters
def student(name, age):
    print(f"Student Name: '{name}' & Age: '{age}' ")


student("Ali", 20)
student("Sara", 22)
student("Ahmed", 21)


# Function Returning a Value
def add(num1, num2):
    return num1 + num2


result = add(55, 6)
print(f"\nThe sum is: {result}\n")


""" Difference Between print() & return"""


# Example 1
def square(x):
    print(x * x)  # This will print the square but not return it


result = square(5)  # This will print 25 but result will be None
print(f"The result of square function is: {result}\n")  # This will print None


# Example 2
def square_return(x):
    return x * x  # This will return the square


result = square_return(5)  # This will return 25
print(f"The result of square_return function is: {result}\n")  # This will print 25


# Local Variable
def local():
    x = 2
    print(f"The value of local variable is: {x}\n")


# print(x) NameError Because x exists only inside the function.
local()

# Global Variable
name = "Ali"


def display():
    print(f"The value of global variable is: {name}")


display()
print(
    name, "\n"
)  # success because name is a global variable and can be accessed outside the function.


# Calculator Function
def calculator(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    (
        print("Division =", a / b, "\n")
        if b > 0
        else print("Division by zero is not allowed\n")
    )


calculator(2, 17)


# Even or Odd Function
def even_odd(num):
    if num % 2 == 0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is an Odd Number")


even_odd(5)
even_odd(10)
even_odd(0)


# Grade Function
def grade(marks):
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
    else:
        print("Enter number in the range from 0 to 100")


print("\n" "Grade Function Test Cases:")
grade(99)
grade(90)
grade(100)
grade(102)
grade(85)
grade(80)
grade(75)
grade(70)
grade(65)
grade(60)
grade(55)
grade(0)
grade(6)
grade(-90)


# Area Function
def area(length, width):
    return length * width


rectangle = area(5.66, 10)
print(f"\nThe area of rectangle is: {rectangle}\n")


# Function Calling Another Function
def line():
    print("------------------------------")


def heading():
    line()
    print("Software Engineering Journey")
    line()


heading()


# Simple Menu Function
def menu():
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit\n")


menu()

"""Function Practice Challenge"""


# Challenge 1
def say_hello():
    print("Hello World\n")


say_hello()


# Challenge 2
def cube(number):
    return number**3


num = int(input("Enter a number to find its cube: "))
print(f"The cube of {num} is: {cube(num)}\n")


# Challenge 3
def maximum(a, b):
    return max(a, b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The maximum number is: {maximum(num1, num2)}\n")


# Challenge 4
def circle_area(radius):
    π = 3.14159
    return π * radius**2


number = int(input("Enter the radius of the circle: "))
print(f"The area of circle with radius {number} is: {circle_area(number)}\n")


# Challenge 5
def is_prime(number):
    if number <= 1:
        return "Not Prime"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Not Prime"
    return "Prime"


entered_number = int(input("Enter a number to check if it is prime: "))
print(f"The number {entered_number} is: {is_prime(entered_number)}\n")
