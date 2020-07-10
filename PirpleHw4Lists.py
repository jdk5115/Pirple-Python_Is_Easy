#Hw4 pirple lists

myUniqueList = []

myLeftovers = []

def listMaker(x):
        if x in myUniqueList:
            myLeftovers.append(x)
            return False
        else:
            myUniqueList.append(x)
            return True

''' Add unique and non-unique values.  
    Not sure how to do an entire list element by element yet
    When I try to include a list, it looks at the whole list as a single
    element and marks it as unique. How would I do that?'''

listMaker(12)
listMaker(92)
listMaker(12)
listMaker(707)
listMaker(12.34)
listMaker(12)
listMaker(97772)
listMaker(1342)
listMaker(70.7)
listMaker(1234)
listMaker(97772)

print("my Unique list =", myUniqueList)
print("my Leftovers =", myLeftovers)
