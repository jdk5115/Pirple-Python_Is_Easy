#pirple activity 5 break and continue loops

patricipants = ["Jon", "Joe","Bill","Dan","Jamie"]

position = 1

# for x in patricipants:
#     if x == "Bill":
#         index = patricipants.index(x)
#         print(index)
#         break
#      print(x)    

# for i in range(len(patricipants)):
#     if patricipants[i] == "Joe":
#         print("half breaked")
#         break
# print("Not Breaked")

for i in range(10):
    if i%3 == 0:
        print(i)
        print("div by 3")
        continue
    print("not div by 3")