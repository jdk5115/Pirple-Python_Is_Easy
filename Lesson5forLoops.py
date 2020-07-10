#Loops - Pirple homework 5

word = "Hellow"

Letters = []

for w in word:
    # print(w)
    # if w == "e":
        # print("What a funny letter")

    
    Letters.append(w)

# print(Letters)

Numbers = [1,2,3,4,5]

# for l in Numbers:
#     if l%2 == 0:

#         print(l)


# # print(word)
Numbers = []

#stopping value is not inclusive
for num in range(1,10,2):
    Numbers.append(num)
    print(num)

print(Numbers)