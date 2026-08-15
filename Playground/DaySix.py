# Program 1 — Student Marks Manager
marks = [87, 91, 79, 95]
students = ["Ali", "Ahmed", "Sara", "Annus"]
print("\n------ Student Marks ------\n")

# zip() combines two lists element by element into pairs.
for student, mark in zip(students, marks):
    print(f"{student:<8} : {mark}")  # left-aligned in a field of 8 characters

print("\nHighest Marks :", max(marks))
print("Lowest Marks  :", min(marks))
print("Average Marks :", sum(marks) / len(marks))

# Program 2 — Shopping Cart
"""Output
Shopping Cart

1. Laptop
2. Mouse
3. Keyboard
4. Headphones
Total Items : 4"""

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")
cart.append("Headphones")

print("\n------ Shopping Cart ------\n")

for index, item in enumerate(cart, start=1):
    print(f"{index}. {item}")

print("\nTotal Items :", len(cart))

# Challenge = Allow the user to add 5 products using input().

for i in range(5):
    product = input(f"Enter Product {i + 1}: ")
    cart.append(product)

print("\n------ Updated Shopping Cart ------\n")

for index, item in enumerate(cart, start=1):
    print(f"{index}. {item}")

print(f"\nTotal Items : {len(cart)}")

# ✅ Program 3 — To-Do List
"""Output
Today's Tasks
1. Study Python
2. Complete Assignment
3. Exercise
4. Git Commit"""
tasks = ["Study Python", "Complete Assignment", "Exercise", "Git Commit"]

print("\n------ Today's Tasks ------\n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Challenge Ask the user to enter 5 tasks.
for i in range(5):
    Tasks = input(f"Enter Task {i+1}: ")
    tasks.append(Tasks)

print("\n------ Updated To-Do List ------\n")
for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# Program 4 — Contact Book
"""Output
Contacts
Ali
Ahmed
Sara
Annus"""

contacts = ["Ali", "Ahmed", "Sara", "Annus"]
print("\n------ Contact Book ------\n")

for contact in contacts:
    print(contact)

search = input("\nSearch Contact: ")
if search in contacts:
    print("Contact Found!")
else:
    print("Contact Not Found!")

# 💰 Program 5 — Expense Tracker
"""Output
Expenses
Food      : 500
Travel    : 1200
Internet  : 2000
Books     : 800
Total Expense : 4500"""
expenses = [500, 1200, 2000, 800]
categories = ["Food", "Travel", "Internet", "Books"]
print("\n------ Expense Tracker ------\n")
for category,expense in zip(categories,expenses):
    print(f"{category:<10}{expense}")
print("\nTotal Expense :",sum(expenses))
#Challenge

'''Calculate
Highest expense
Lowest expense
Average expense'''
print("\nHighest Expense :",max(expenses))
print("\nLowest Expense :",min(expenses))
print("\nAverage Expense :",sum(expenses)/len(expenses))
