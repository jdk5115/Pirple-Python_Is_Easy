# Project #1: Connect 4

'''
Details:
 
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company. In this project, your task is create a Connect 4 game in Python. 
Before you get started, please watch this video on the rules of Connect 4: https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward. You'll want to draw the board, and allow two players to take turns 
placing their pieces on the board (but as you learned above, they can only do so by choosing a column, not a row). The first player to get 4 across or 
diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.

Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package like termcolor into your project. 
We're going to cover importing later in the course, but try and see if you can figure it out on your own. Or you might be able to find unicode 
characters to use instead, depending on what your system supports. Here's a hint: print(u'\u2B24')
'''

#This is the process I am taking to figure out how I will do this.

'''

Assuming a 7 wide x 6 high board:
       A B C D E F G
       _ _ _ _ _ _ _
    1 |_|_|_|_|_|_|_|
    2 |_|_|_|_|_|_|_|
    3 |_|_|_|_|_|_|_|
    4 |_|_|_|_|_|_|_|
    5 |_|_|_|_|_|_|_|
    6 |_|_|_|_|_|_|_|

Possible winning combinations: 
    Vertical: 21 solutions [Every Column A-F (7)] [3 winning possibilities per column (1-4, 2-5, 3-6)]
    Horizontal: 24 solutions [Every Row 1-6] [4 winning possibilities per row (A-D, B-E, C-G, D-F]
    Diagional - Left to Right: 12 solutions - starting from top to bottom [[A-D (1-4, 2-5, 3-6)], [B-E (1-4, 2-5, 3-6)], [C-F (1-4, 2-5, 3-6)], [D-G (1-4, 2-5, 3-6)]]
    Diagional - Right to Left: 12 solutions - starting from top to bottom [[G-D (1-4, 2-5, 3-6)], [F-C (1-4, 2-5, 3-6)], [E-B (1-4, 2-5, 3-6)], [D-A (1-4, 2-5, 3-6)]]

In total there are 69 possible winning combinations. nice.


1. Initialize the grid
2. Assign players (maybe pick colors?) and establish turns
3. Gather input (column # or letter)
4. Check column for other "dots"
5. Redraw board with latest move
6. Check to see if that was the winning move
7. Announce winner and end game (if applicable)
7b. Next player move

Going to do everything but #6 since that will take the most time. I thought that if I save it for last, I may come up with something clever.

'''
#Going to re-use a lot of the code we've already learned from tic-tac-toe lesson.

def drawfield(field):
    for row in range(7):
        if row%2 == 0:
            practicalRow = int(row/2)
            for column in range(15):
                            #0 => 0, 2 => 1, 4 => 2
                if column%2 == 0:
                    practicalColumn = int(column/2)
                    if column != 14:
                        print(field[practicalColumn][practicalRow], end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                    print("|", end="")
        else:
            print("-----")

player = 1
#[Column1 [row1, row 2, row3, row4...}, Column2[Row 1, row 2, row 3]...]] 7 columns 6 rows
currentfield = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],]
drawfield(currentfield)
# print(currentfield)

while(True):
    print("Players turn: ", player)
    moveRow = int(input("Please enter the row."))
    moveColumn = int(input("Please enter the column."))
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