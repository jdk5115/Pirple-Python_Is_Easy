# from Importing Lesson file
# from random import * allows you to not use random keyword like below

#from random import random, uniform #to import only a couple functions

import random as r
# randInt = randint(0,100) #random from start <= N <= end. Includes 0 and 100
# print(randInt)

# randFloat = random() #0.0 <= N <= 1.0
# print(randFloat)

# randUniform = uniform(1,123) # start <= N <= end
# print(randUniform)

simpleList = [1, 3, 5, 7, 11]
pickElement = r.choice(simpleList)
print(pickElement)
r.shuffle(simpleList)
print(simpleList)

