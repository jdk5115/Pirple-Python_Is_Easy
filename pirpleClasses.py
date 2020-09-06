# Pirple Classes - Section 9

# class ClassName: 

#     def __init__(self):
#         self.Attribute = 0

#     def AnotherFuntion(self):
#         Action(s)

class Team:
    def __init__(self, Name, Origin):
        self.TeamName = Name
        self.TeamOrigin = Origin

    def defineTeamName(self, Name):
        self.TeamName = Name

    def defineteamorigin(self, Origin):
        self.TeamOrigin = Origin

Team1 = Team("Tigers", "Chicago")

Team2 = Team("Hawks","New York")

print(Team1.TeamName)

Team1.defineTeamName("Dolphins")

print(Team1.TeamName)

print(Team1.TeamOrigin)

Team1.defineteamorigin("CHICAGO")

print(Team1.TeamOrigin)
print(Team2.TeamName)
print(Team2.TeamOrigin)