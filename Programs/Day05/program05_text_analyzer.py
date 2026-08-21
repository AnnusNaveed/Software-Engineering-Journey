def line():
    print("-" * 32)

# Program 5 — Text Analyzer
line()
print("Program 5 — Text Analyzer")
line()

text = input("Enter Text: ")
print("\n------ Analysis ------")
print("Characters :", len(text))
print("Words :", len(text.split()))
print("Uppercase :", text.upper())
print("Lowercase :", text.lower())