
'''
How to check for solutions in connect 4:

Note that "up" and "dowm" are going to be in reverse order since we want the bottom to fill first.  
The bottom row will be row 0 and count up by one vertically.
Also, remmeber that the board fills from bottom to top.

I am going to start out checking for vertical solutions because I think that is the easiest  
because you never have to check up, only down.

'''
player = 1
colHeight = "colheight"

gameBoard = {
        "col0":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col1":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col2":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col3":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col4":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col5":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col6":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        }
rowInput = 0
    
while(True):
    # columns start on row 0 but player may not realize that so making them 1-7 for user instead of 0-6.
    print("It is player", str(player) +"'s turn.")
    columnSelection = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7. "))-1 

    # Since the connect four board is filled from bottom to top, we are going to iterate on 'colheight' in each column, based on how many "chips" in col.
    # This will tell us what row (0-5) to put the next move
    rowInput = int(gameBoard["col" + str(columnSelection)][colHeight])
    if rowInput > 5:
        print("That column is full, please select another cloumn.")
    else:
        if player == 1:
            gameBoard["col" + str(columnSelection)][str(rowInput)] = "\u2B24'"
            print(gameBoard["col" + str(columnSelection)][str(rowInput)])
            gameBoard["col" + str(columnSelection)][colHeight] += 1
            rowInput +=1
            player = 2
            print(gameBoard)

        elif player == 2:
            gameBoard["col" + str(columnSelection)][str(rowInput)] = "\u25EF"
            print(gameBoard["col" + str(columnSelection)][str(rowInput)])
            gameBoard["col" + str(columnSelection)][colHeight] += 1
            rowInput += 1
            player = 1
            print(gameBoard)

print(u'\u2B24')
print(u'\u25EF')
print(gameBoard)

# playerSelection.append("X")
# happy = 2
# guy = gameBoard["col"+str(happy)]["colheight"]
# print(gameBoard["col"+str(happy)][str(guy)])
# gameBoard["col"+str(happy)]["colheight"]
# print(gameBoard[str(happy)]["h"+str(guy)])

# for i in gameBoard["col"+happy]:
    
# # while (True):

#     print("It is player", str(player) +"'s turn.")

#     print(gameBoard)
#     print(colHeight["col"+ str(columnSelection-1\)])
#     colHeight["col"+ str(columnSelection)] +=1
#     print(colHeight)
    # chipHeight.append(1)

#     if columnSelection > 7:
#         #
#         # Need a way to error proof this later
#         #
#         print("Please enter a column between one and 7.") 
#     else:
#         if rowHeight > 5:
#             print("That column is full. Please pick another column.")
#         else:
#                 if player == 1:
#                     colRow = gameBoard["col" + str(columnSelection)]["row"+ str(rowHeight)]
#                     print(colRow)
#                     rowHeight += 1
#                 else:

#                 if player %2 == 0:
#                     player = 1

#                 else:
#                     player = 2

#             colRow = gameBoard["col" + str(playerInput)]["row"+ str(rowHeight)]
#             print(colRow)
#             rowHeight += 1
#             if player %2 ==0:
#                 player = 2
#             else:
#                 player = 1

# print(gameBoard)



#colHeight = {"col0":0,"col1":0,"col2":0,"col3":0,"col4":0,"col5":0,"col6":0}

# gameBoard = [["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],
#             ["","","","","",""],["","","","","",""],["","","","","",""]
#             ]
