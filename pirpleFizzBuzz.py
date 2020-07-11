#fizzbuzz loops pirple hw #5
prime = []
for i in range(1,100):
    if i == 1:
        print(i)    
    elif i > 3 and i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i > 3 and i%3 == 0 and i%5 != 0:
        print("fizz")
    elif i > 5 and i %5 == 0 and i%3 != 0:
        print("buzz")
    elif i > 2 and i%2 == 0:
        print(i)
    elif i != 1 and (i == 7 or i%7 != 0):
        print("prime")
        prime.append(i)

#extra credit check
print(prime)

