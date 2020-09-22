''' Project #2: Hangman


Details:
Have you ever played hangman? It's a children's game, normally played by kids when they're supposed to be doing homework instead. 
If you've never played here are the rules:
https://www.youtube.com/watch?v=cGOeiQfjYPk


For this assignment, we want to play hangman in 2-player mode. The game should start by prompting player 1 to pick a word. 
Then the screen should clear itself so that player 2 can't see the word
hint: print(chr(27) + "[2J") 
After the screen is clear, the "gallows" and the empty letter spaces should be drawn, and player 2 should be 
allowed to guess letters until they either win, or lose. As they choose correct letters, the letters should appear on the screen in 
place of the blank space (clear and redraw the whole screen). As they choose wrong letters, the "man" himself should come end up being 
drawn, piece by piece. How many guesses they get before losing is up to you (depending on how complicated of a man you want to draw).

Extra Credit:
Try finding a large list of dictionary words and embedding them in your application. When the game starts, instead of 
player 1 choosing the word to play with, the computer should pick a random word from the dictionary. This will allow you to play 
against the computer instead of only 2-player mode. When the game starts, the user should be prompted to choose between 1-player or 
2-player mode.'''
import tkinter as tk
import turtle as t
global lsWord, word, strikes

strikes = 0

#Allow player 1 to pick a word and then check for spaces and numbers.Save word as list - lsWord

while(True):
    word = input('Player 1, please pick a word less than 8 characters long.')
    if word.isalpha():
        if len(word) > 8:
            print('Please pick a word only 8 characters long.')
        else:
            global lsWord
            lsWord = []
            for x in word:
                lsWord.append(x)
            break
    elif " " in word:
        print('Please only use one word.')
    else:
        print("Please only use letters.")


def dashes():
    global lsWord
    t.penup()
    t.setx(-350)
    t.sety(-300)
    for i in range(len(lsWord)):
        t.pendown()
        t.pensize(5) 
        t.fd(50)
        t.penup()
        t.fd(30)
        t.pendown()
        t.penup()

def gallows():
    t.penup()
    t.setx(250)
    t.sety(-200)
    t.pendown()
    t.pensize(5)   
    t.lt(180)
    t.fd(100)
    t.lt(180)
    t.fd(200)
    t.lt(180)
    t.fd(100)
    t.rt(90)
    t.forward(300)
    t.lt(90)
    t.forward(200)
    t.lt(90)
    t.forward(50)

def head():
        t.penup()
        t.setx(50)
        t.sety(50)
        t.dot(50)
        t.penup()

def body():
        t.penup()
        t.setx(50)
        t.sety(50)
        t.down()
        t.pendown()
        t.pensize(5)
        t.forward(125)
        t.penup()

def leftLeg():
    t.penup()
    t.setx(50)
    t.sety(-75)
    t.down()
    t.pendown()
    t.rt(30)
    t.fd(50)
    t.penup()

def rightLeg():
    t.penup()
    t.setx(50)
    t.sety(-75)
    t.pendown()
    t.down()
    t.lt(60)
    t.fd(50)
    t.penup()

def leftArm():
    t.penup()
    t.setx(50)
    t.sety(-25)
    t.pendown()
    t.down()
    t.rt(150)    
    t.fd(50)
    t.penup()

def rightArm():
    t.penup()
    t.setx(50)
    t.sety(-25)
    t.pendown()
    t.down()
    t.rt(120)    
    t.fd(50)
    t.penup()

dashes()
gallows()
head()
body()
leftLeg()
rightLeg()
leftArm()
rightArm()

print(t.position())
print(lsWord)
# while(True):
#     for r in len(word):
#         guess = input('What letter do you want to guess?')


#Turtle

# word = str(input('word'))
# wordLen = len(word)
# lsWord = [word]

# t.circle(120, 180)  # draw a semicircle
# t.position()
# t.heading()

# t.write('string', font=("Arial", 36, "normal"))

# #draw spaces for word chosen
# for i in range(wordLen):
    
#     t.fd(30)
#     t.penup()
#     t.fd(30)
#     t.pendown()

t.mainloop()
