#file input output pirple
# "r" - read, "w" - write, "a" - append, "r+"" - read and write
# file = open("filename","r",)
# file.close()

cities = ["London", "Paris", "Oshawa", "Tokyo", "LA"]

cityfile = open("cityplaces", "w", )

for spots in cities:
    cityfile.write(spots + "\n") #needs to be a string
    
cityfile.close()

cityfile = open("cityplaces", "r")

# wholefile = cityfile.read()
# print(wholefile)
# print("done")
# wholefile.close()
firstline = cityfile.readline()
print(firstline)
secondline = cityfile.readline()
print(secondline)
for line in cityfile:
    print(line, end="")
cityfile.close()

finalspot = "thailand"

cityfile = open("cityplaces", "a")
cityfile.write(finalspot)
cityfile.close()

cityfile = open("cityplaces", "r")
for line in cityfile:
    print(line, end="")
cityfile.close()

for i in range(5):
    with open("cityplaces" + str(i), "r") as cityfile:
        for line in cityfile:
            print(line)