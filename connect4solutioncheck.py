
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
    
    col0 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col1 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col2 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col3 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col4 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col5 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}
    col6 = {"row0":"","row1":"","row2":"","row3":"","row4":"","row5":""}

    nestedD = {"col0":{"row0":"0,0","row1":"0,1","row2":"0,2","row3":"0,3","row4":"0,4","row5":"0,5"},"col1":{"row0":"1,0","row1":"1,1","row2":"1,2","row3":"1,3","row4":"1,4","row5":"1,5"}}

    print("It is player", str(player) +"'s turn.")
    playerInput = int(input("Which column do you want to place your chip? Choose 1, 2, 3, 4, 5, 6 or 7."))
    playerInput -= 1 #columns start on row 0 but player may not realize that.


    colRow = nestedD["col" + str(playerInput)]["row"+ str(rowHeight)]
    print(colRow)
    rowHeight += 1
    if player %2 ==0:
        player = 2
    else:
        player = 1