#pirple I/O participant data

# participantNumber = 5
# participantData = []
# registeredparticipants = 0
# outputFile = open("participantData.txt","w")

# while(registeredparticipants < participantNumber):
#     tempPartData = []
#     name = input("Please enter your name: ")
#     tempPartData.append(name)
#     country = input("Please enter your country of origin: ")
#     tempPartData.append(country)
#     age = int(input("Please enter your age: "))
#     tempPartData.append(age)
#     print(tempPartData)
#     participantData.append(tempPartData)
#     print(participantData)

#     registeredparticipants += 1

# for participant in participantData:
#     #the line below is to loop through the nested list
#     for data in participant:
#         outputFile.write(str(data))
#         outputFile.write(" ")
#     outputFile.write(" \n")

# outputFile.close()

inputFile = open("participantData.txt","r")

inputList = []

for line in inputFile:
    tempParticipant = line.strip("\n").split()
    inputList.append(tempParticipant)
    print(inputList)
        # "Line 1: Jon U.S. 35 \n".strip(\n) => Jon U.S. 35
        # "Line 1: Jon U.S. 35 \n".split() => ["Jon", "U.S.", "35"]

Age = {}
for part in inputList:
    tempAge = int(part[-1]) #int 35
    if tempAge in Age:
        Age [tempAge] += 1
    else:
        Age[tempAge] = 1

print(Age)

Countries = {}
for part in inputList:
    tempCountry = part[1] #int 35
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1
print("Countries that attended",Countries)

oldest = 0
youngest = 100
mostOccuringAge = 0
counter = 0

for tempAge in Age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge < youngest:
        youngest = tempAge
    if Age[tempAge]>counter:
        counter = Age[tempAge]
        mostOccuringAge = tempAge


print(oldest)
print(youngest)
print("Most Occuring age is:",mostOccuringAge,"with",counter,"participants.")


inputFile.close()
