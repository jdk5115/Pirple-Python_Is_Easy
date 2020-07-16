#tictactoe pirple


#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4
# 01234

def drawfield():
    for row in range(5):
        if row%2 == 0:
            for column in range(5):
                if column%2 == 0:
                    if column != 4:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-----")

player = 1

while(True):
    moveRow = int(input("Please enter the row."))
    moveColumn = int(input("Please enter the column."))
    if player == 1:
        # make move for player 1
    else:
        # make move for player two
