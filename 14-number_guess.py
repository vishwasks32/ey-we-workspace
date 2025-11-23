#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com
# Number guess game
# Ask user to enter integer between 1,10
# Set the value for a number 
# Guess the number in  guesses
from random import randint

MIN_VAL = 1
MAX_VAL = 10
MAX_GUESSES = 3

def random_guess():
    return randint(MIN_VAL, MAX_VAL)

def main():
    # Do setup
    # assume a random number
    assumed_number = random_guess()

    # set the number of guess = 3
    # Start the loop
    for chance in range(MAX_GUESSES):
        guess_value = int(input('Enter any guess Number between 1 & 10: '))
        if guess_value == assumed_number:
            print(f"You Won")
            return 0
        else:
            print("Wrong Guess")
    
    print("You Lost the game")

if __name__ == '__main__':
    main()