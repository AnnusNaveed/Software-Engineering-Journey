# Program 1 — Notes Manager
"""Objective
Create a simple application that permanently stores notes.

Concepts
input()
Functions
with open()
Append
Read
File persistence"""

FILE_NAME = "data/notes.txt"


def add_note():
    note = input("Enter Your Note :").strip().title()

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully.")


def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
            return

        print("\n========== NOTES ==========")

        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note.strip()}")

    except FileNotFoundError:
        print("There is no note !")


add_note()
view_notes()
