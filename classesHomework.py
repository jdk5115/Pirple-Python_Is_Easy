'''Homework Assignment #9: Classes

Details:
xCreate a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
xThe class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
xNext an inheritance classes from Vehicle called "Cars".
xThe Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  
xIt should have another method called "Stop" that sets the value of isDriving to false.
xSwitching isDriving from true to false should increment the "TripsSinceMaintenance" counter. 
xAnd when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
xAdd a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
xCreate 3 different cars, using your Cars class, and drive them all a different number of times. 
xThen print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

Extra Credit:
Create a Planes class that is also an inheritance class from Vehicle. Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), 
but different in one respect: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), 
and an error message should be printed saying that the plane can't fly until it's repaired.'''

class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance
    
    def setMake(self, x):
        self.make = x

    def setModel(self, x):
        self.model = x

    def setYear(self, x):
        self.year = x

    def setWeight(self, x):
        self.weight = x

    def setneedsMaintenance(self, x):
        self.needsMaintenance = x

    def settripsSinceMaintenance(self, x):
        self.tripsSinceMaintenance = x

class Cars(Vehicle):
    def __init__(self, isDriving, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True
    
    def Repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False
    
    def __str__(self):
        return "Make and model " + str(self.make) + " - " + str(self.model) + "\nYear: " + str(self.year) + "\nWeight: " + str(self.weight) + "\nDoes this vehicle need maintenance? " + str(self.needsMaintenance) + " \nHow many trips since the last maintenance? " + str(self.tripsSinceMaintenance) + "\n\n"

car1 = Cars(False,"Chevy", "Corvette", "2005", 1985)
car2 = Cars(False, "Ford", "F-150", "2018", 2989)
car3 = Cars(False, "Tesla", "X P100D", "2020", 1587)


for x in range (150):
    Cars.Drive(car1)
    Cars.Stop(car1)

print(str(car1))

for x in range (84):
    Cars.Drive(car2)
    Cars.Stop(car2)

print(str(car2))

for x in range (240):
    Cars.Drive(car3)
    Cars.Stop(car3)

print(str(car3))
