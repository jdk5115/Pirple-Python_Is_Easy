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
#[Column1 [row1, row 2, row3}, Column2[Row 1, row 2, row 3]...]]
currentfield = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while(True):
    moveRow = int(input("Please enter the row."))
    moveColumn = int(input("Please enter the column."))
    if player == 1:
        # make move for player 1
        currentfield[moveColumn][moveRow] = "X"
        player = 2
    else:
        # make move for player two
        currentfield[moveColumn][moveRow] = "O"
        player = 1
