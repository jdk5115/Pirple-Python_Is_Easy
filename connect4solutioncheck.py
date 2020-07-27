
'''
How to check for solutions in connect 4:

Note that "up" and "dowm" are going to be in reverse order since we want the bottom to fill first.  
The bottom row will be row 0 and count up by one vertically.
Also, remmeber that the board fills from bottom to top.

I am going to start out checking for vertical solutions because I think that is the easiest  
because you never have to check up, only down.

'''
player = 1
#colHeight = {"col0":0,"col1":0,"col2":0,"col3":0,"col4":0,"col5":0,"col6":0}

# gameBoard = [["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],
#             ["","","","","",""],["","","","","",""],["","","","","",""]
#             ]

gameBoard = {
        "col0":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col1":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col2":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col3":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col4":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col5":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        "col6":{"0":0,"1":1,"2":"","3":"","4":"","5":"","colheight":0},
        }

while(True):
    colHeight = "colheight"
    columnSelection = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7. "))-1 #columns start on row 0 but player may not realize that.
    
    rowInput = gameBoard["col" + str(columnSelection)][str(colHeight)]
    print(rowInput)

    if player == 1:
        gameBoard["col" + str(columnSelection)][str(rowInput)] = "\u2B24'"
        print(gameBoard["col" + str(columnSelection)][str(rowInput)])
        gameBoard["col" + str(columnSelection)][str(colHeight)] += 1
        rowInput +=1
        player = 2
        print(gameBoard)
    else:
        gameBoard["col" + str(columnSelection)][("colheight")] = "\u25EF"
        playerSelection = gameBoard["col" + str(columnSelection)][colHeight]
        print(playerSelection)
        player = 1

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