# Program 1 — Student Database
"""Objective

Store student information using a dictionary.
Output
========== Student Database ==========
Name        : Annus
Age         : 22
Department  : BS Computer Science
CGPA        : 3.82
City        : Lahore
======================================"""

student = {
    "Name": "Annus",
    "Age": 22,
    "Department": "BS Computer Science",
    "CGPA": 3.42,
    "City": "Lahore",
}

print("=" * 38)
print("      Student Database")
print("=" * 38)

for key, value in student.items():
    print(f"{key:<12}: {value}")
print("=" * 38)

# Program 2 — Phone Book
"""Objective
Search contacts using dictionary keys."""
phone_book = {
    "Ali": "03001234567",
    "Ahmed": "03111234567",
    "Sara": "03221234567",
    "Annus": "03331234567",
}
name = input("Enter Contact Name: ").strip().title()
if name in phone_book:
    print(f"{name}'s Number: {phone_book[name]}")
else:
    print("Contact Not Found")

# Challenge: Allow the user to add a new contact.
new_name = input("New Contact: ").strip().title()
number = int(input("Phone Number:  "))
phone_book[new_name] = number

# Program 3 — Product Catalog
"""Objective
Store product prices."""
products = {"Laptop": 150000, "Mouse": 2500, "Keyboard": 5000, "Monitor": 35000}
print("------ Product Catalog ------")
for product, price in products.items():
    print(f"{product:<12}: Rs.{price}")

# Challenge: Find the most expensive product.
most_expensive = max(
    products, key=products.get
)  # finds the dictionary key whose value is the largest
"""
products → dictionary containing product names and prices.
products.get → tells max() to compare products based on their values (prices).
max(...) → finds the product with the highest price.
most_expensive → stores the product name (key)."""
print(f"The most expensive product = {most_expensive} : {products[most_expensive]}")

# Program 4 — Bank Account Manager
account = {"Account No": "PK001", "Name": "Annus", "Balance": 50000}

print("------ Bank Account ------")
for key, value in account.items():
    print(f"{key:<12} :{value}")
deposit = int(input("\nEnter Deposit Amount :"))
account["Balance"] += deposit
print("\nUpdated Balance :", account["Balance"])


# Challenge: Add a withdrawal feature with a balance check.
def withdrawal(amount):
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    if amount <= account["Balance"]:
        account["Balance"] -= amount
        print("Withdrawal Successful!")
        print(f"Remaining Balance :{account['Balance']}")
    else:
        print("Insufficient Balance!")
        print("Available Balance :", account["Balance"])


enter = int(input("\nEnter Withdrawal Amount :"))
withdrawal(enter)

# Program 5 — Grade Manager
marks = {"PF": 90, "OOP": 88, "DSA": 95, "DB": 91, "AI": 87}

print("------ Grade Manager ------")
for subject, mark in marks.items():
    print(f"{subject:<8} :{mark}")

average = sum(marks.values()) / len(marks)
print(f"\nHighest :{max(marks.values())}")
print(f"Lowest :{min(marks.values())}")
print(f"Average :{average:.2f}")
