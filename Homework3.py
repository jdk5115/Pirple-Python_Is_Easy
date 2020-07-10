#Homework 3 Pirple If statements

def func1 (x,y,z):
    if int(x) == int(y) or int(x) == int(z) or int(y) == int(z) :
        result = True
    else:
        result = False
    return result

print(func1(1,2,"2"))
