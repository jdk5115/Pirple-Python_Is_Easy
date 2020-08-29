import sys
from termcolor import colored, cprint

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
print_yellow_dot = lambda x: cprint(x, 'yellow',end="")
print_red_dot = lambda x: cprint(x, 'red',end="")

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

# this function draws grid
# multiplying rows and columns by 2 to account for lines. 
# number of rows and columns will be actual boxes to place red and yellow circles
# Note - red and yellow dots don't render well on half a screen for some reason?  Used cprint
def func1(row,column):
    print("----------------------")
    row = row*2
    column = (column*2)
    for r in range(0,row+1):
        if r%2 == 0:
            for c in range(0,column+1):
                if c%2 == 1:
                    if c < column - 1:
                        print(" |", end="")
                    elif c == column - 1:
                        if c < 8:
                            square = gameBoard["col" + str(int((c)/2))][str(int((r)/2))]
                            if square == "":
                                print(" |")
                            else:
                                print(gameBoard["col" + str(int((c)/2))][str(int((r)/2))])
                else:
                    if c/2 <= 6:
                        square = gameBoard["col" + str(int((c)/2))][str(int((r)/2))]
                        if c == 0:
                            print("|", end="")
                        if square == "":
                            print(" ", end = "")
                        else:
                            if square == "X":
                                print_yellow_dot(u'\u2B24')
                            elif square == "O":
                                print_red_dot(u'\u2B24')

        else:
            if r == row-1:
                break
            else:
                print("\n")
                print("-"*(column+6))
    print("\n----------------------")

def checkForWinner(col): 
    #Vertical Checks
    if gameBoard["col" + str(col)][colHeight] > 3:
        if gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col)][str(rowInput-1)] == "X" and gameBoard["col" + str(col)][str(rowInput-2)] == "X" and gameBoard["col" + str(col)][str(rowInput-3)]== "X":
            print ("Player 1 is the winner!")
            exit()
        elif gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col)][str(rowInput-1)] == "O" and gameBoard["col" + str(col)][str(rowInput-2)] == "O" and gameBoard["col" + str(col)][str(rowInput-3)]== "O":
            print("Player 2 is the winner!")
            exit()

    # Horizontal Checks Definitely a way simplier way to do this through loops but it took me a while to come up with this, so I'm going to leave it for now.
    for col in range (7):
        # checks for player 1
        if gameBoard["col" + str(0)][str(rowInput)] == "X" and gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X":
            print("Player 1 is the winner!")
            func1(6,8)
            exit()
        elif gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X":
            print("Player 1 is the winner!")
            func1(6,8)
            exit()
        elif gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X":
            print("Player 1 is the winner!")
            func1(6,8)
            exit()       
        elif gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X" and gameBoard["col" + str(6)][str(rowInput)] == "X":
            print("Player 1 is the winner!")
            func1(6,8)
            exit() 
        #player 2
        if gameBoard["col" + str(0)][str(rowInput)] == "O" and gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O":
            print("Player 2 is the winner!")
            func1(6,8)
            exit()
        elif gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O":
            print("Player 2 is the winner!")
            func1(6,8)
            exit()
        elif gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O":
            print("Player 2 is the winner!")
            func1(6,8)
            exit()       
        elif gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O" and gameBoard["col" + str(6)][str(rowInput)] == "O":
            print("Player 2 is the winner!")
            func1(6,8)
            exit()   

    # Diagional checks
    # 4 different ways for columns and rows to be arranged (left to right bottom to top, left to right top to bottom and right to left for both versions too)  
    for col in range (7):
        # left bottom to top
        if (gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X"):
            print("Player 1 is the winner!")
            func1(6,8)
            exit() 
        if (gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O"):
            print("Player 2 is the winner!")
            func1(6,8)
            exit()
        # left bottom to top
        if (gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" or
            gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X"):
            print("Player 1 is the winner!")
            func1(6,8)
            exit() 
        if (gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" or
            gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O"):
            print("Player 2 is the winner!")
            func1(6,8)
            exit()

    
# This loop will initiate the game and continue to alternate turns between players until someone wins.
while(True):
    # columns start on row 0 but player may not realize that so making them 1-7 for user instead of 0-6.
    print("It is player", str(player) +"'s turn.")
    columnSelection = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7. "))-1 

    # Since the connect four board is filled from bottom to top, we are going to iterate on 'colheight' in each column, based on how many "chips" in col.
    # This will tell us what row (0-5) to put the next move
    rowInput = int(gameBoard["col" + str(columnSelection)][colHeight])

    if rowInput > 5:
        print("That column is full, please select another cloumn.")

    elif columnSelection >= 7 or columnSelection < 0:
        print("Please select an appropriate column number.")

    else:
        if player == 1:
            gameBoard["col" + str(columnSelection)][str(rowInput)] = 'X'
            gameBoard["col" + str(columnSelection)][colHeight] += 1
            checkForWinner(columnSelection)
            rowInput +=1
            player = 2
            print(gameBoard)   

        elif player == 2:
            gameBoard["col" + str(columnSelection)][str(rowInput)] = 'O'   
            gameBoard["col" + str(columnSelection)][colHeight] += 1       
            checkForWinner(columnSelection)
            rowInput += 1
            player = 1
            print(gameBoard)
    func1(6,8)

# Check for winner
# Going to do this in 4 section - horizontal, vertical, diagonal right and diagonal left
'''Possible winning combinations: 
    Vertical: 21 solutions [Every Column A-F (7)] [3 winning possibilities per column (1-4, 2-5, 3-6)]
    Horizontal: 24 solutions [Every Row 1-6] [4 winning possibilities per row (A-D, B-E, C-G, D-F]
    Diagonal - Left to Right: 12 solutions - starting from top to bottom [[A-D (1-4, 2-5, 3-6)], [B-E (1-4, 2-5, 3-6)], [C-F (1-4, 2-5, 3-6)], [D-G (1-4, 2-5, 3-6)]]
    Diagonal - Right to Left: 12 solutions - starting from top to bottom [[G-D (1-4, 2-5, 3-6)], [F-C (1-4, 2-5, 3-6)], [E-B (1-4, 2-5, 3-6)], [D-A (1-4, 2-5, 3-6)]]
'''

                
            

    # I am going to try and group the columns together here since they will all need one of the same column combinations 1-4, 2-5, 3-5, 4-7
    # Horizontal

    # Diagonal Right

    # Diagonal Left

