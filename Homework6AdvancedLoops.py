#homewrok # 6 pirple - advanced loops

''' I wrote this function so that the rows and columns of "boxes" on the board 
    would be equal to the inputs, instead of counting the lines like the example.
    I didn't want to just copy the example and swap their numbers for my variables.
    Hope that's ok.  Thanks'''


def func1(row,column):
    if row > 9 or column > 90 or row < 3 or column < 3:
        print("Please enter a row number more than 3 but less than 10 and a column number more than 3 but less than 91. Any smaller than that and you can't win and any bigger than that and it won't fit inside the screen!")
    else:

        # multiplying rows and columns by 2 to account for lines. 
        # number of rows and columns will be actual boxes to places x's and o's

        row = row*2
        column = (column*2)
        for r in range(row + 1):
            if r%2 == 0:
                for c in range(column):
                    if c%2 == 1:
                        if c < column-1:
                            print("|", end="")
                        elif c == column-1:
                            print("|")
                    else:
                        if c <= column:
                            print(" ",end="")
                        elif c == column:
                            print(" ")
            else:
                if r == row-1:
                    break
                else:
                    print(" " + "-"*(column-1))


func1(6,8)