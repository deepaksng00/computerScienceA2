class car:
    def __init__(self, s, n):
        self.mileage = 0
        self.registration = s
        self.make = n
        self.dateOfInspection = ''
    def getReg(self):
        return self.registration

    def getMake(self):
        return self.make

    def getMileage(self):
        return self.mileage

    def getDateOfInspection(self):
        return self.dateofinspection

    def setDateOfInspection(self, mileage, dateofinspection):
        self.mileage = mileage
        self.dateOfInspection = dateofinspection

car1 = car("DAS", "BMW")
print(car1.getReg)

    
