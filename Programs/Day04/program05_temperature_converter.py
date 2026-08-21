def line():
    print("-" * 34)

# Program 5 — Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


line()
print("Program 5 — Temperature Converter")
line()
while True:
    line()
    print("Welcome to Temperature Converter Menu!")
    line()
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        temperature = float(input("Enter the temperature: "))
        print("Celsius to Fahrenheit:", celsius_to_fahrenheit(temperature))
    elif choice == "2":
        temperature = float(input("Enter the temperature: "))
        print("Fahrenheit to Celsius:", fahrenheit_to_celsius(temperature))
    elif choice == "3":
        print("Exiting the program.")
        line()
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")