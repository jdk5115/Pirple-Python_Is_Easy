#Importing Lesson 3 - Time Library 

import time
currentTime = time.perf_counter()

print("hello")
print("world")

pastTime = time.perf_counter()
print(pastTime - currentTime)
print("1")
time.sleep(5) #seconds
print("2")

for i in range(1,11):
    print(i)
    time.sleep(1)