# Standard structure of a class

# class ClassName: 

#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFuntion(self):
#         Action(s)

class Team:
    def __init__(self, Name = "Name", Origin = "Origin"):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def defineTeamName(self, Name):
        self.TeamName = Name

    def defineteamorigin(self, Origin):
        self.TeamOrigin = Origin

# class InheritanceClassName(ParentClass):

#     def __init__(self, Input1, Input2):
#         ParentClass.__init__(self)
#         self.Attribute1 = Input1
#         self.Attribute2 = Input2
#         self.Attribute3 = 0

#     def AnotherMethod(self):
#         Action(s)

class Player(Team):

    def __init__(self, playerName, playerPoints, TeamName, TeamOrigin):
        Team.__init__(self, TeamName, TeamOrigin)
        self.playerName = playerName
        self.playerPoints = playerPoints
    
    def scoredPoint(self):
        self.playerPoints += 1
    
    def setName(self, Name):
        self.playerName = Name
    
    def __str__(self):
        return "Player has scored: " + str(self.playerPoints) + " points."

player1 = Player("Sid", 0, "Cows", "Polasky")

print(player1.playerName)
print(player1.playerPoints)
print(player1.TeamName)
print(player1.TeamOrigin)

player1.scoredPoint()
player1.setName("lee")
print(player1.playerPoints)
print(player1.playerName)
print(player1)