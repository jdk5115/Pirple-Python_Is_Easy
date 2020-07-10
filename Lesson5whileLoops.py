
counter = 1
sum = 0
while(counter<=10):
    print(counter)
    sum = sum + counter
    counter += 1
    print(sum)

Letters = [ 'a','b','c','d','e']

Index = 4

while(Index<len(Letters)):
    print(Index)
    print(Letters[Index])
    Index += 1

height = 5000
velocity = 50

time = 0

while (height>0):
    height = height - velocity
    time += 1

print(height)
print(time)