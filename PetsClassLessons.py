#Classes - Pets: Lessons A - D

class Pets:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful   

    #setters
    def setName(self, x):
        self.name = x

    def setAge(self, Age):
        self.age = Age

    def setHunger(self, hunger):
        self.hunger = hunger

    def setPlayful(self, playful):
        self.playful = playful
    
    def __str__(self):
        return (self.name + " is " + str(self.age) + " years old.")

# Pet1 = Pets("Fido", 43, False, True)

# print(Pet1.getName())
# print(Pet1.getPlayful())
# Pet1.setName("Snowball")
# print(Pet1.getName())
# print(Pet1.name)
# Pet1.name = "Jim"
# print(Pet1.name)
# print(Pet1)

class Dog(Pets):
    def __init__(self, name, age, hunger, playful, breed, favoriteToy):
        Pets.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favoriteToy = favoriteToy
    
    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.favoriteToy)
        else:
            return ("The dog doesn't want to play.")
    
class Cat(Pets):
    def __init__(self, name, age, hunger, playful, place):
        Pets.__init__(self, name, age, hunger, playful)
        self.favPlaceToSit = place
    
    def wantsToSit(self):
        if self.playful == True:
            print("The cat " + self.name + " wants to sit in their favortie place, the " + self.favPlaceToSit)
        else:
            print("The cat wants to play.")

class human:
    def __init__(self, name, pets):
        self.name = name
        self.pets = pets
    
    def hasPets(self):
        if len(self.pets) != 0:
            return "yes"
        else:
            return "no"

huskyDog = Dog("Bill", 5, False, False, "Husky", "Rope")

play = huskyDog.wantsToPlay()

print(play)

typicalCat = Cat("William", 17, False, True, "chair.")

typicalCat.wantsToSit()

print(typicalCat)
print(huskyDog)

yourAverageHuman = human("Alice", [huskyDog, typicalCat])

hasPets = yourAverageHuman.hasPets()

print(hasPets + " " + str(len(yourAverageHuman.pets)) + " pets.")

print(yourAverageHuman.pets[1])