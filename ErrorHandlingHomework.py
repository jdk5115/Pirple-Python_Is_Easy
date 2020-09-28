'''Details:
 
As you've been completing the past homework assignments and projects, you've undoubtedly run into errors a few times, and noticed that if you pass 
certain types of variables to your functions, they will throw exceptions. Now's your time to go back and make those functions better (bullet-proof them).

For this assignment you can choose any of the homeworks or projects you've done so far. Pick a function that you know is particularly problematic and 
add try/except/finally cases to it so that it can handle the errors more gracefully.
'''
input1 = input('Please enter whole numbers.')
input2 = input('Please enter only letters.')

x = 0
y = 0

def func1(input1,input2):
    try:
        print(input1.isnumeric())
    except:
        print('That was not a number ')
    finally:
        print('Good job')

    try:
        print(input2.isalpha())
    except:
        print('That was not a letter')
    finally:
        print('see ya')

list1 = ["3",345,"hey", "what?", "wd-40",555.78,"not what I was thinking, more like 4.3", 99, 101.1, ",.';=-",True]
list2 = ["7",38,"word", "Yeah.", "10-4 good buddy",556404016184904615,"yeah, more like 40", -59, 12, "[]\}{]}}]",False]

for i in range(10):
    func1(list1[x],list2[y])
    print(list1[x])
    print(list2[y], "\n")
    x += 1
    y += 1
