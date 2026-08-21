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