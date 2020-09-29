'''
Everyone has their favorite card game. What's yours? For this assignment, choose a card game (other than Blackjack), 
and turn it into a Python program. It doesn't matter if it's a 1-player game, or a 2 player game, or more! 
That's totally up to you. A few requirements:

It's got to be a card game (no board games, etc)
When the game starts up, you should ask for the players' names. And after they enter their names, your game should 
refer to them by name only. ("It's John's turn" instead of "It's player 1's turn). 
At any point during the game, someone should be able to type "--help" to be taken to a screen where they can read the 
rules of the game and instructions for how to play. After they're done reading, they should be able to type "--resume" 
to go back to the game and pick up where they left off.



Extra Credit:

Want to make this much much harder on yourself? Okay, you asked for it!

For extra credit, allow 2 players to play on two different computers that are on the same network. Two people should be 
able to start identical versions of your program, and enter the internal IP address of the user on the network who they 
want to play against. The two applications should communicate with each other, across the network using simple HTTP requests. 
Try this library to send requests:

http://docs.python-requests.org/en/master/
http://docs.python-requests.org/en/master/user/quickstart/

And try Flask to receive them:

http://flask.pocoo.org/

The 2-player game should only start if one person has challenged the other (by entering their internal IP address), and the 2nd 
person has accepted the challenge. The exact flow of the challenge mechanism is up to you.


thirty-one? https://playingcarddecks.com/blogs/how-to-play/thirty-one-game-rules



Card Game Rules
Thirty One, is a casino type card game for 2 or more people and is played with a standard 52 playing card deck. In Thirty One, 
Aces are worth 11 points, face cards are worth 10 points and numbered cards are worth their pip value. The objective of the game is to have a hand 
equal to or as close to 31 as possible.

Set Up
The dealer shuffles the deck and passes out three cards to each player. The remaining deck forms the stock and the dealer then flips one card over to form a 
discard pile. 

How to Play
The player to the left of the dealer begins gameplay. When it is their turn, players choose to either pick a card from the stock or from the discard pile 
and then they must discard one of their cards, all in an attempt to get a hand as close or equal to 31.

Only cards of the same suit count as points. For example, if a player has an Aces of Spades, an 8 of Spades, and a King of Hearts, the player’s hand is 
worth 19.

When a player is comfortable with their hand, they knock on the table. All other players then have one more draw to try and improve their hand. 
The player with the lowest hand loses for that round. Each player starts with 4 points and whoever loses all their points first, loses.
If the player who knocks has the lowest hand, they give up 2 points rather than 1. When a player loses 4 times, they are out of the game. 
The last player standing wins the game.  

'''

from random import shuffle

global deck, x, y
def createDeck():
    global deck, x, y
    deck = []
    faceValues = ["A","K","Q","J"]
    suit = [" Hearts"," Spades"," Diamonds"," Clubs"]
    x  = 0
    y = 0

    for c in range(4):
        for card in range (2,11):
            deck.append(str(card) + str(suit[x]))
        x+=1
    x = 0
    for c in range(4):
        for card in faceValues:
            deck.append(str(faceValues[y]) + str(suit[x]))
            y += 1
        x += 1
        y = 0

    shuffle(deck)
    return deck
createDeck()
print(deck)
print(len(deck))

class Player:
    def __init__(self, hand = [], points = 4):
        self.hand = hand
        self.points = points

    def __str__(self): #allows us to call print(Player)
        currentHand = "" #self.hand = ["A", "10"] -> "A 10"
        for card in self.hand:
            currentHand += str(card) + " "

        finalStatus = currentHand + "score: " + str(self.score)
        # A 10 score: 21
        return finalStatus

    def draw(self):
        self.money += self.bet
        self.bet = 0
    
    def setScore(self):
        self.score = 0
        faceCardDict = {"A":11,"K":10,"Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,
                        "6":6,"5":5,"4":4,"3":3,"2":2}

        aceCounter = 0
        for card in self.hand:
            self.score += faceCardDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def win(self, result):
        if result == True: 
            if self.score == 21 and len(self.hand) == 2:
                self.money += int(2.5*self.bet)

            else:
                self.money += 2*self.bet

            self.bet = 0
        else:
            self.bet = 0

    def printHouse(self, House):
        for card in range(len(House.hand)):
            if card == 0:
                print("X", end=" ")
            elif card == len(House.hand)-1:
                print(House.hand[card])
            else:
                print(House.hand[card], end=" ")
