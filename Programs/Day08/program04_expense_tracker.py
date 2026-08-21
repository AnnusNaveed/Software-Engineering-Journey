# Program 4 — Expense Tracker
"""
Objective:
Store:
Description
Amount
Category
using JSON.
"""

import json

FILE_NAME = "data/expenses.json"


def load_expenses():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found. Starting with empty expenses.")
        return []

    except json.JSONDecodeError:
        print("File is empty or contains invalid JSON.")
        return []


def save_expenses(expenses):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(expenses, file, indent=4)

    except OSError as error:
        print(f"Unable to save expenses: {error}")


def add_expense():

    expenses = load_expenses()

    # Description validation
    while True:

        description = input("Description: ").strip()

        if not description:
            print("Description cannot be empty. Please try again.")
            continue

        description = description.title()
        break

    # Amount validation
    while True:

        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid numeric amount.")

    # Category validation
    while True:

        category = input("Category: ").strip()

        if not category:
            print("Category cannot be empty. Please try again.")
            continue

        category = category.title()
        break

    expense = {"description": description, "amount": amount, "category": category}

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense saved successfully.")


def show_expenses():

    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n========== EXPENSES ==========")

    total = 0

    for number, expense in enumerate(expenses, start=1):

        try:
            print(
                f"{number}. "
                f'{expense["description"]} | '
                f'Rs.{expense["amount"]:.2f} | '
                f'{expense["category"]}'
            )

            total += expense["amount"]

        except KeyError as error:
            print(f"Invalid expense record. Missing field: {error}")

    print(f"\nTotal Expense: Rs.{total:.2f}")


add_expense()
show_expenses()

"""
Description
     ↓
Empty?
 ┌───┴───┐
YES     NO
 ↓       ↓
Ask     Continue
again
         ↓
       Amount
         ↓
   Valid positive number?
      ┌────┴────┐
     NO        YES
      ↓          ↓
    Ask       Continue
    again
                ↓
             Category
                ↓
             Empty?
           ┌────┴────┐
          YES       NO
           ↓         ↓
         Ask      Continue
         again
                    ↓
              Save Expense
"""
