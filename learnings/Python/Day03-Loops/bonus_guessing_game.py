# Bonus Project — Guessing Game
number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    else:
        print("Try again.")
