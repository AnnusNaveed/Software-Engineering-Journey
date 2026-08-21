# Program 5 — Library Manager
"""
Now we'll create a small persistent library.

Store:
Book ID
Title
Author
Available"""

import json
import os

FILE_NAME = "data/library.json"


# Create data directory if it does not exist
os.makedirs("data", exist_ok=True)


def load_books():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Library file not found. Starting with empty library.")
        return []

    except json.JSONDecodeError:
        print("Library file is empty or contains invalid JSON.")
        return []

    except OSError as error:
        print(f"Unable to read library: {error}")
        return []


def save_books(books):

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(books, file, indent=4)

    except OSError as error:
        print(f"Unable to save library: {error}")


def add_book():

    books = load_books()

    # Book ID validation
    while True:

        book_id = input("Book ID: ").strip().upper()

        if not book_id:
            print("Book ID cannot be empty. Please try again.")
            continue

        # Check duplicate ID
        duplicate = False

        for book in books:

            if book.get("id") == book_id:
                duplicate = True
                break

        if duplicate:
            print("Book ID already exists. Please enter a unique ID.")
            continue

        break

    # Title validation
    while True:

        title = input("Title: ").strip()

        if not title:
            print("Title cannot be empty. Please try again.")
            continue

        title = title.title()
        break

    # Author validation
    while True:

        author = input("Author: ").strip()

        if not author:
            print("Author cannot be empty. Please try again.")
            continue

        author = author.title()
        break

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": False
    }

    books.append(book)

    save_books(books)

    print("Book added successfully.")


def view_books():

    books = load_books()

    if not books:
        print("\nNo books found.")
        return

    print("\n========== LIBRARY ==========")

    for number, book in enumerate(books, start=1):

        try:

            status = "Available" if book["available"] else "Borrowed"

            print(
                f'{number}. '
                f'{book["id"]} | '
                f'{book["title"]} | '
                f'{book["author"]} | '
                f'{status}'
            )

        except KeyError as error:

            print(
                f"Book #{number} is invalid. "
                f"Missing field: {error}"
            )

    print("=" * 30)


add_book()
view_books()

'''
User enters ID
      ↓
Does ID already exist?
   ↙           ↘
 YES            NO
  ↓              ↓
Reject        Accept
  ↓              ↓
Ask again     Create book

'''