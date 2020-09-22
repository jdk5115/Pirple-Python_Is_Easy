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

word = [input('Pick a word')]

print(word)

# while(True):
#     for r in len(word):
#         guess = input('What letter do you want to guess?')


