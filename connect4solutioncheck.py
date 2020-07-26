
'''
How to check for solutions in connect 4:

Note that "up" and "dowm" are going to be in reverse order since we want the bottom to fill first.  
The bottom row will be row 0 and count up by one vertically.
Also, remmeber that the board fills from bottom to top.

I am going to start out checking for vertical solutions because I think that is the easiest  
because you never have to check up, only down.

'''
player = 1
rowHeight = 0

while (True):

    # gameBoard = {
    #     "col0":{"row0":"0,0","row1":"0,1","row2":"0,2","row3":"0,3","row4":"0,4","row5":"0,5"},
    #     "col1":{"row0":"1,0","row1":"1,1","row2":"1,2","row3":"1,3","row4":"1,4","row5":"1,5"},
    #     "col2":{"row0":"2,0","row1":"2,1","row2":"2,2","row3":"2,3","row4":"2,4","row5":"2,5"},
    #     "col3":{"row0":"3,0","row1":"3,1","row2":"3,2","row3":"3,3","row4":"3,4","row5":"3,5"},
    #     "col4":{"row0":"4,0","row1":"4,1","row2":"4,2","row3":"4,3","row4":"4,4","row5":"4,5"},
    #     "col5":{"row0":"5,0","row1":"5,1","row2":"5,2","row3":"5,3","row4":"5,4","row5":"5,5"},
    #     "col6":{"row0":"6,0","row1":"6,1","row2":"6,2","row3":"6,3","row4":"6,4","row5":"6,5"},
    #     }

    gameboard = [["","","","","",""],["","","","","",""],["","","","","",""],["","","","","",""],
                ["","","","","",""],["","","","","",""],["","","","","",""]
                ]

    print("It is player", str(player) +"'s turn.")
    playerInput = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7."))
    playerInput -= 1 #columns start on row 0 but player may not realize that.
    playerSelection = gameboard[playerInput][rowHeight]]

    if playerInput <= 7:
        if rowHeight > 5:
            print("That column is full. Please pick another column.")
            playerInput = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7."))
            playerInput -= 1 
            if rowHeight > 5:
                print("you blew it.")
                break
            else:
                if player == 1:
                    colRow = gameBoard["col" + str(playerInput)]["row"+ str(rowHeight)]
                    print(colRow)
                    rowHeight += 1
                else:

                if player %2 == 0:
                    player = 1

                else:
                    player = 2
        else:
            colRow = gameBoard["col" + str(playerInput)]["row"+ str(rowHeight)]
            print(colRow)
            rowHeight += 1
            if player %2 ==0:
                player = 2
            else:
                player = 1
    else:
        print("Please enter a column between one and 7.")
        continue
print(gameBoard)