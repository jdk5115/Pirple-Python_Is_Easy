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

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("X", end=" ")
        elif card == len(House.hand)-1:
            print(House.hand[card])
        else:
            print(House.hand[card], end=" ")



cardDeck = createDeck()
print(cardDeck)
firstHand = [str(cardDeck.pop()), str(cardDeck.pop())]
secondHand = [str(cardDeck.pop()), str(cardDeck.pop())]

Player1 = Player(firstHand)
House = Player(secondHand)

print(Player1)
printHouse(House)
if Player1.hasBlackjack():
    if House.hasBlackjack():
        Player1.draw()
    else:
        Player1.win(True)
else:
    while(Player1.score < 21):
        action = input("Do you want another card? (y/n)")
        if action == "y":
            Player1.hit(str(cardDeck.pop()))
            print("Player 1 score: ", Player1)
            print("House score: ", House)
        else:
            break
    while(House.score < 17):
        print(House)
        House.hit(cardDeck.pop())

    if Player1.score > 21:
        if House.score > 21:
            Player1.draw()
        else:
            Player1.win(False)
    elif Player1.score > House.score:
        Player1.win(True)
    elif Player1.score == House.score:
        Player1.draw()
    else:
        if House.score > 21:
            Player1.win(True)
        else:
            Player1.win(False)


print(Player1.money)
print(Player1)
print(House)
