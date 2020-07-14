#input and output pirple

# name = input("please enter your name: ")
# print(name)

# age = int(input("please enter your age: "))
# print(str(age) + "4")

scores = []

for i in range(5):
    score = float(input("Please input your score " + str(i+1) + ": "))
    scores.append(score)
    print("The score you entered was:\n", score)

print(scores)