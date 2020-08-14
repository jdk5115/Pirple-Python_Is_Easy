#Homework 4 Lists - Pirple

#TestList = ["element1","element2","element3"]
#TestList = [0,1,2]

Scores = [70,[1,2,3],67.5,90,80]

# #print(Scores[2:5])
print(Scores)
# Scores[0] = 75
# Scores[1] = [1,2,3]

print(Scores[1][2])

Scores.append(83)
print(Scores)

Scores.extend([83,212,425,635])
print(Scores)

Scores.extend(range(1,102))
print(Scores)