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