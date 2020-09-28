from random import shuffle

global deck
def createDeck():
    global deck
    deck = []
    faceValues = ["A","K","Q","J"]

    for i in range(4):
        for card in range (2,11):
            deck.append(card)
        
        for card in faceValues:
            deck.append(card)
    shuffle(deck)
    return deck

cardDeck = createDeck()

print(cardDeck)

class Player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = 0
        self.money = money

    def __str__(self): #allows us to call print(Player)
        currentHand = "" #self.hand = ["A", "10"] -> "A 10"
        for card in self.hand:
            currentHand += str(card) + " "

        finalStatus = currentHand + "score: " + str(self.score)
        # A 10 score: 21
        return finalStatus
    
    def setScore():



