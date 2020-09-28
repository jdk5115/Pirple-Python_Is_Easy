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
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self): #allows us to call print(Player)
        currentHand = "" #self.hand = ["A", "10"] -> "A 10"
        for card in self.hand:
            currentHand += str(card) + " "

        finalStatus = currentHand + "score: " + str(self.score)
        # A 10 score: 21
        return finalStatus
    
    def setScore(self):
        self.score = 0
        faceCardDict = {"A":11, "K":10,"Q":10,"J":10, "10":10,"9":9,"8":8,"7":7,
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

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result == True: 
            if self.score == 21 and len(self.hand) == 2:
                self.money += int(2.5*self.bet)

            else:
                self.money += 2*self.bet

            self.bet = 0
        else:
            self.bet = 0

Player1 = Player(["3","7"])
print(Player1)
#Player1.hit("K")
Player1.hit("A")
Player1.hit("A")
print(Player1)
Player1.betMoney(20)
print(Player1.money, Player1.bet)
Player1.win(True)
print(Player1.money, Player1.bet)
Player1.play(["A","K"])
print(Player1)
Player1.betMoney(20)
Player1.win(True)
print(Player1.money, Player1.bet)
