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