# Program 3 — Personal Diary
"""Objective:
Create a diary where every entry is permanently stored.
Use a text file."""

import os

FILE_NAME = "data/diary.txt"


# Create data directory if it does not exist
os.makedirs("data", exist_ok=True)


def write_entry():

    try:
        entry = input("Write today's diary entry: ").strip()

        if not entry:
            print("Diary entry cannot be empty.")
            return

        with open(FILE_NAME, "a") as file:
            file.write(entry + "\n")

        print("Diary entry saved successfully.")

    except OSError as error:
        print(f"Unable to save diary entry: {error}")


def read_diary():

    try:
        with open(FILE_NAME, "r") as file:
            entries = file.readlines()

        if not entries:
            print("No diary entries found.")
            return

        print("\n========== DIARY ==========")

        for number, entry in enumerate(entries, start=1):
            print(f"{number}. {entry.strip()}")

        print("=" * 28)

    except FileNotFoundError:
        print("No diary entries found.")

    except OSError as error:
        print(f"Unable to read diary: {error}")


write_entry()
read_diary()

"""
What makes this robust?

                 DIARY PROGRAM
                       │
             ┌─────────┴─────────┐
             │                   │
        write_entry()       read_diary()
             │                   │
       Empty input?        File exists?
        /       \           /       \
      YES       NO         NO        YES
       │         │         │          │
     Reject     Save     Message    Read
                 │                    │
             OSError?              OSError?
                 │                    │
               Handle              Handle
"""
