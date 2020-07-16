#file input output pirple
# "r" - read, "w" - write, "a" - append, "r+"" - read and write
# file = open("filename","r",)
# file.close()

cities = ["London", "Paris", "Oshawa", "Tokyo", "LA"]

cityfile = open("cityplaces", "w", )

for spots in cities:
    cityfile.write(spots + " \n") #needs to be a string
    
cityfile.close()

cityfile = open("cityplaces", "r")

# wholefile = cityfile.read()
# print(wholefile)
# print("done")
# wholefile.close()

for line in cityfile:
    print(line, end="hey now ")