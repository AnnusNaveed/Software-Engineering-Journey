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