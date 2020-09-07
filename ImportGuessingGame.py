# Import Lesson - Guessing game

from random import randint

randVal = randint(0,100)

while(True):
    guess = int(input("What is your guess? "))
    if randVal == guess:
        break
    elif guess < randVal:
        print("Your guess was too low!")
    else:
        print("Your guess is too high!")

print("You've won!!! The correct guess was:", guess)

