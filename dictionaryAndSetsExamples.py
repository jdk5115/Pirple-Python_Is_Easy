#examples of dictionaries and sets lesson Pirple

blackshoes = {42:2, 41:3, 40:4, 39:1, 38:0}

while (True):
    purchaseSize = int(input("What size do you want to buy?\n"))
    if purchaseSize < 0:
        break
    if purchaseSize in blackshoes:
        if blackshoes[purchaseSize] > 0:
            blackshoes[purchaseSize] -=1
            print(blackshoes)
        else:
            print("We do not have that size in stock, sorry :(")
    else:
        print("don't have that size sorry")
