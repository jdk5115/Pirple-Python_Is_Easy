
gameBoard = {
        "col0":{"0":"","1":"x","2":"","3":"","4":"","5":"","colheight":0},
        "col1":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col2":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col3":{"0":"","1":"","2":"x","3":"","4":"","5":"","colheight":0},
        "col4":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col5":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        "col6":{"0":"","1":"","2":"","3":"","4":"","5":"","colheight":0},
        }

print(gameBoard["col0"][1])

# if columnSelection == 0:
    #     if gameBoard["col" + str(0)][str(rowInput)] == "X" and gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(0)][str(rowInput)] == "O" and gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()

    # elif columnSelection == 1:
    #     if gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(0)][str(rowInput)] == "X" and gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(0)][str(rowInput)] == "O" and gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()

    # elif columnSelection == 2:
    #     if gameBoard["col" + str(0)][str(rowInput)] == "X" and gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(0)][str(rowInput)] == "O" and gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()          

    # elif columnSelection == 3:
    #     if gameBoard["col" + str(0)][str(rowInput)] == "X" and gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X" and gameBoard["col" + str(6)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(0)][str(rowInput)] == "O" and gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O" and gameBoard["col" + str(6)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()

    # elif columnSelection == 4:
    #     if gameBoard["col" + str(1)][str(rowInput)] == "X" and gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X" and gameBoard["col" + str(6)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(1)][str(rowInput)] == "O" and gameBoard["col" + str(2)][str(rowInput)] == "0" and gameBoard["col" + str(3)][str(rowInput)] == "0" and gameBoard["col" + str(4)][str(rowInput)] == "0":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "0" and gameBoard["col" + str(3)][str(rowInput)] == "0" and gameBoard["col" + str(4)][str(rowInput)] == "0" and gameBoard["col" + str(5)][str(rowInput)] == "0":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "0" and gameBoard["col" + str(4)][str(rowInput)] == "0" and gameBoard["col" + str(5)][str(rowInput)] == "0" and gameBoard["col" + str(6)][str(rowInput)] == "0":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()

    # elif columnSelection == 5:
    #     if gameBoard["col" + str(2)][str(rowInput)] == "X" and gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X" and gameBoard["col" + str(6)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(2)][str(rowInput)] == "O" and gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O" and gameBoard["col" + str(6)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()

    # elif columnSelection == 6:
    #     if gameBoard["col" + str(3)][str(rowInput)] == "X" and gameBoard["col" + str(4)][str(rowInput)] == "X" and gameBoard["col" + str(5)][str(rowInput)] == "X" and gameBoard["col" + str(6)][str(rowInput)] == "X":
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit()
    #     if gameBoard["col" + str(3)][str(rowInput)] == "O" and gameBoard["col" + str(4)][str(rowInput)] == "O" and gameBoard["col" + str(5)][str(rowInput)] == "O" and gameBoard["col" + str(6)][str(rowInput)] == "O":
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    # else:
    #     print("nah") 

# try:
    #     if (gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "X" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "X"):
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit() 
    #     if (gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" and gameBoard["col" + str(col+3)][str(rowInput+3)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput+2)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput+1)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-3)][str(rowInput-3)] == "O" and gameBoard["col" + str(col-2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col-1)][str(rowInput-1)] == "O"):
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit()
    #         # right to left
    #     if (gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col-2)][str(rowInput+2)] == "X" and gameBoard["col" + str(col-3)][str(rowInput+3)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col-2)][str(rowInput+2)] == "X" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "X" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput-2)] == "X" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "X" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "X" and gameBoard["col" + str(col+2)][str(rowInput-2)] == "X" and gameBoard["col" + str(col+3)][str(rowInput-3)] == "X"):
    #         print("Player 1 is the winner!")
    #         func1(6,8)
    #         exit() 
    #     if (gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col-2)][str(rowInput+2)] == "O" and gameBoard["col" + str(col-3)][str(rowInput+3)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col-2)][str(rowInput+2)] == "O" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col-1)][str(rowInput+1)] == "O" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput-2)] == "O" or
    #         gameBoard["col" + str(col)][str(rowInput)] == "O" and gameBoard["col" + str(col+1)][str(rowInput-1)] == "O" and gameBoard["col" + str(col+2)][str(rowInput-2)] == "O" and gameBoard["col" + str(col+3)][str(rowInput-3)] == "O"):
    #         print("Player 2 is the winner!")
    #         func1(6,8)
    #         exit() 
    # except KeyError:
    #     print("nah")

