# number guessing game
computer_number = 7
user_number = int(input("Guess a number between 1 and 10: "))
if user_number == computer_number:
    print("You guessed it right!")
else:
    print("Sorry, the correct number was", computer_number)
