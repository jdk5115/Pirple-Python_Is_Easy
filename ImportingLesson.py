# follow along lesson with importing

import random

#random.seed(1)

randInt = random.randint(0,100) #random from start <= N <= end. Includes 0 and 100
print(randInt)

randFloat = random.random() #0.0 <= N <= 1.0
print(randFloat)

trueRand = randFloat*randInt
print(trueRand)

randUniform = random.uniform(1,11) # start <= N <= end
print(randUniform)