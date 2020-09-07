# follow along lesson with importing

import random as r #as r = as a nickname so you don't have to re-write random
#random.seed(1)

randInt = r.randint(0,100) #random from start <= N <= end. Includes 0 and 100
print(randInt)

randFloat = r.random() #0.0 <= N <= 1.0
print(randFloat)

trueRand = randFloat*randInt
print(trueRand)

randUniform = r.uniform(1,11123) # start <= N <= end
print(randUniform)

