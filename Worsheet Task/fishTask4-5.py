# Deepak Singh 13PEA
# Computer Science Homework Task 4-5
# Object Orientated Programming (OOP)
# COMP 3

class Car:
    def __init__(self, registration, make):
        self.mileage = 0
        self.registration = registration
        self.make = make
        self.dateOfInspection = "10/11/2018"
    def getRegistration(self):
        return self.registration
    def getMileage(self):
        return self.mileage
    def getMake(self):
        return self.make
    def getDateOfInpection(self):
        return self.dateOfInspection
    def setInspectionData(self, mileage, dateofinspection):
        self.mileage = mileage
        self.dateOfInspection = dateofinspection
        return '{} {}'.format(self.mileage, self.dateOfInspection)

car1 = Car("VMXA 11D", "BMW")
print(car1.getRegistration())
print(car1.getMileage())
print(car1.getMake())
print(car1.setInspectionData("100000", "10/11/2018"))
        
