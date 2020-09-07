#Import Guessing game #2
from time import perf_counter
from random import random

randVal = random() #random float 0.0 < N < 1.0
upper = 1.0
lower = 0.0
guess = 0.5
startTime = perf_counter()

while(True):
    guess = (upper + lower) / 2
    if guess == randVal:
        break
    elif guess < randVal:
        lower = guess
        print(guess)
        print("Too Low!")
    else:
        upper = guess
        print(guess)
        print("Too High!")

endTime = perf_counter()

print("Nailed it! The number was:", guess)
print("That took", endTime - startTime ,"seconds.")




