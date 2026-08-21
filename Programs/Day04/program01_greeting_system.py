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