# Bonus — Inventory File System

# Major Challenge — Inventory Management System
"""
Objective:

Build a persistent Inventory System using:

1. Add Product
2. Search Product
3. Update Quantity
4. Delete Product
5. Display All Products
6. Calculate Inventory Value 
   Formula: (quantity × price) 
7. Detect Low Stock
   For example: quantity < 5

Concepts Integrated:

List
Dictionaries
Functions
JSON
File Handling
Exception Handling
Input Validation
CRUD Operations
Persistent Storage
"""

import json
import os


FILE_NAME = "data/inventory.json"

# Create data directory if it does not exist
os.makedirs("data", exist_ok=True)


# ============================================================
# LOAD INVENTORY
# ============================================================

def load_inventory():

    try:

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:

        print("Inventory file not found. Starting with empty inventory.")
        return []

    except json.JSONDecodeError:

        print("Inventory file is empty or contains invalid JSON.")
        return []

    except OSError as error:

        print(f"Unable to read inventory: {error}")
        return []


# ============================================================
# SAVE INVENTORY
# ============================================================

def save_inventory(inventory):

    try:

        with open(FILE_NAME, "w") as file:
            json.dump(inventory, file, indent=4)

    except OSError as error:

        print(f"Unable to save inventory: {error}")


# ============================================================
# 1. ADD PRODUCT
# ============================================================

def add_product():

    inventory = load_inventory()

    # Product ID validation
    while True:

        product_id = input("Product ID: ").strip().upper()

        if not product_id:

            print("Product ID cannot be empty.")
            continue

        duplicate = False

        for product in inventory:

            if product.get("id") == product_id:

                duplicate = True
                break

        if duplicate:

            print("Product ID already exists.")
            print("Please enter a unique Product ID.")
            continue

        break


    # Product Name validation
    while True:

        name = input("Product Name: ").strip()

        if not name:

            print("Product name cannot be empty.")
            continue

        name = name.title()
        break


    # Quantity validation
    while True:

        try:

            quantity = int(input("Quantity: "))

            if quantity < 0:

                print("Quantity cannot be negative.")
                continue

            break

        except ValueError:

            print("Please enter a valid whole number.")


    # Price validation
    while True:

        try:

            price = float(input("Price: "))

            if price <= 0:

                print("Price must be greater than 0.")
                continue

            break

        except ValueError:

            print("Please enter a valid numeric price.")


    product = {

        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price

    }

    inventory.append(product)

    save_inventory(inventory)

    print("\nProduct added successfully.")


# ============================================================
# 2. SEARCH PRODUCT
# ============================================================

def search_product():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    search_id = input("Enter Product ID to search: ").strip().upper()

    if not search_id:

        print("Product ID cannot be empty.")
        return


    for product in inventory:

        if product.get("id") == search_id:

            print("\n========== PRODUCT FOUND ==========")

            print(f'ID       : {product["id"]}')
            print(f'Name     : {product["name"]}')
            print(f'Quantity : {product["quantity"]}')
            print(f'Price    : Rs.{product["price"]:.2f}')

            print("===================================")

            return


    print("Product not found.")


# ============================================================
# 3. UPDATE QUANTITY
# ============================================================

def update_quantity():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    product_id = input("Enter Product ID: ").strip().upper()

    if not product_id:

        print("Product ID cannot be empty.")
        return


    for product in inventory:

        if product.get("id") == product_id:

            while True:

                try:

                    new_quantity = int(
                        input("Enter New Quantity: ")
                    )

                    if new_quantity < 0:

                        print("Quantity cannot be negative.")
                        continue

                    break

                except ValueError:

                    print("Please enter a valid whole number.")


            product["quantity"] = new_quantity

            save_inventory(inventory)

            print("Quantity updated successfully.")

            return


    print("Product not found.")


# ============================================================
# 4. DELETE PRODUCT
# ============================================================

def delete_product():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    product_id = input("Enter Product ID to delete: ").strip().upper()

    if not product_id:

        print("Product ID cannot be empty.")
        return


    for product in inventory:

        if product.get("id") == product_id:

            inventory.remove(product)

            save_inventory(inventory)

            print("Product deleted successfully.")

            return


    print("Product not found.")


# ============================================================
# 5. VIEW ALL PRODUCTS
# ============================================================

def view_inventory():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    print("\n========== INVENTORY ==========")

    for number, product in enumerate(inventory, start=1):

        try:

            print(
                f'{number}. '
                f'{product["id"]} | '
                f'{product["name"]} | '
                f'Qty: {product["quantity"]} | '
                f'Rs.{product["price"]:.2f}'
            )

        except KeyError as error:

            print(
                f"Product #{number} is invalid. "
                f"Missing field: {error}"
            )

    print("=" * 32)


# ============================================================
# 6. CALCULATE INVENTORY VALUE
# ============================================================

def inventory_value():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    total_value = 0

    print("\n========== INVENTORY VALUE ==========")

    for product in inventory:

        try:

            value = product["quantity"] * product["price"]

            total_value += value

            print(
                f'{product["name"]} : '
                f'Rs.{value:.2f}'
            )

        except KeyError as error:

            print(f"Invalid product record. Missing field: {error}")


    print("------------------------------------")
    print(f"Total Inventory Value : Rs.{total_value:.2f}")
    print("====================================")


# ============================================================
# 7. DETECT LOW STOCK
# ============================================================

def low_stock():

    inventory = load_inventory()

    if not inventory:

        print("\nNo products found.")
        return


    found = False

    print("\n========== LOW STOCK ==========")

    for product in inventory:

        try:

            if product["quantity"] < 5:

                found = True

                print(
                    f'{product["id"]} | '
                    f'{product["name"]} | '
                    f'Qty: {product["quantity"]}'
                )

        except KeyError as error:

            print(
                f"Invalid product record. "
                f"Missing field: {error}"
            )


    if not found:

        print("No low-stock products.")

    print("===============================")


# ============================================================
# MAIN PROGRAM
# ============================================================

while True:

    print("""
========================================
        INVENTORY MANAGEMENT SYSTEM
========================================

1. Add Product
2. Search Product
3. Update Quantity
4. Delete Product
5. View All Products
6. Calculate Inventory Value
7. Detect Low Stock
8. Exit

========================================
""")

    choice = input("Enter your choice: ").strip()


    if choice == "1":

        add_product()


    elif choice == "2":

        search_product()


    elif choice == "3":

        update_quantity()


    elif choice == "4":

        delete_product()


    elif choice == "5":

        view_inventory()


    elif choice == "6":

        inventory_value()


    elif choice == "7":

        low_stock()


    elif choice == "8":

        print("\nThank you for using Inventory Management System.")
        break


    else:

        print("\nInvalid choice. Please select 1-8.")


'''
Architecture:

                 INVENTORY SYSTEM
                        │
                        ↓
                inventory.json
                        │
                        ↓
                load_inventory()
                        │
                        ↓
             List of Dictionaries
                        │
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
       ADD           SEARCH            UPDATE
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                     DELETE
                        ↓
                      VIEW
                        ↓
                INVENTORY VALUE
                        ↓
                   LOW STOCK
                        │
                        ↓
                 save_inventory()
                        │
                        ↓
                inventory.json


| Operation       | Concept                       |
| --------------- | ----------------------------- |
| Add             | `append()`                    |
| Search          | `for` + condition             |
| Update          | Dictionary modification       |
| Delete          | `remove()`                    |
| View            | Iteration + formatting        |
| Inventory Value | Calculation                   |
| Low Stock       | Conditional logic             |
| Persistence     | `json.dump()` / `json.load()` |
| Robustness      | `try/except` + validation     |
| Menu            | `while True` + conditionals   |


'''