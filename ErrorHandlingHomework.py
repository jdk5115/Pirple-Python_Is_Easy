'''Details:
 
As you've been completing the past homework assignments and projects, you've undoubtedly run into errors a few times, and noticed that if you pass 
certain types of variables to your functions, they will throw exceptions. Now's your time to go back and make those functions better (bullet-proof them).

For this assignment you can choose any of the homeworks or projects you've done so far. Pick a function that you know is particularly problematic and 
add try/except/finally cases to it so that it can handle the errors more gracefully.
'''
input1 = input('Please enter whole numbers.')
input2 = input('Please enter only letters.')

def func1(input1,input2):

    try:
        print(input1.isnumeric())
    except:
        print('\nThat was not a number ')
    finally:
        print('Good job')

    try:
        print(input2.isalpha())
    except:
        print('\nThat was not a letter')
    finally:
        print('see ya')



func1(input1, input2)