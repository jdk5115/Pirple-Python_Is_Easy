#pirple I/O participant data

participantNumber = 2
participantData = []
registeredparticipants = 0
outputFile = open("participantData.txt","w")

while(registeredparticipants < participantNumber):
    tempPartData = []
    name = input("Please enter your name: ")
    tempPartData.append(name)
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    age = int(input("Please enter your age: "))
    tempPartData.append(age)
    print(tempPartData)
    participantData.append(tempPartData)
    print(participantData)

    registeredparticipants += 1

for participant in participantData:
    #the line below is to loop through the nested list
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")
    outputFile.write(" \n")

outputFile.close()