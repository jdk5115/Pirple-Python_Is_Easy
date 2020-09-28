#tictactoe pirple


#  | |  0
# ----- 1
#  | |  2
# ----- 3
#  | |  4
# 01234

def drawfield(field):
    for row in range(16):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(15):
                            #0 => 0, 2 => 1, 4 => 2
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != 4:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")

player = 1
#[Column1 [row1, row 2, row3}, Column2[Row 1, row 2, row 3]...]]
currentfield = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],]
drawfield(currentfield)
# print(currentfield)

while(True):
    print("Players turn: ", player)
    moveRow = int(input("Please enter the row."))
    moveColumn = int(input("Please enter the column."))
    try:
        isnum(moveRow)
        
    except:

    if player == 1:
        # make move for player 1
        if currentfield[moveColumn][moveRow] == " ":
            currentfield[moveColumn][moveRow] = "X"
            player = 2
    else:
        # make move for player two
        if currentfield[moveColumn][moveRow] == " ":
            currentfield[moveColumn][moveRow] = "O"
            player = 1
    drawfield(currentfield)
    print(currentfield)
