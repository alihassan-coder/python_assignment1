# 17. Write a program that continues to ask for a number until the correct number is guessed.

import random

correct_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == correct_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
