# Deepak Singh
# Ex.4

highestTempValue = 0
highlowestTempValue = 0

monthlyAvg = [ ["January", 6, 3],
               ["February", 7, 3],
               ["March", 10, 4],
               ["April", 13, 6],
               ["May", 17, 9],
               ["June", 20, 12],
               ["July", 22, 14],
               ["August", 21, 14],
               ["September", 19, 12],
               ["October", 14, 9],
               ["November", 10, 6],
               ["December", 7, 3]  ]
highestTemps = []
lowestTemps = []

for i in monthlyAvg:
    month = i[0]
    avrgHigh = i[1]
    avrgLow = i[2]
    highestTemps.append((month, avrgHigh))
    lowestTemps.append((month, avrgLow))

for Key, Value in highestTemps:
    if Value > highestTempValue:
        highestTempValue = Value
        monthHighestName = Key

for Key, Value in lowestTemps:
    if Value >= highlowestTempValue:
        lowestTempValue = Value
        monthLowestName = Key
        


print(monthHighestName, 'has the highest average temperature in the list, with a temperature of', highestTempValue, 'C')
print('=========================================================================================')
print(monthLowestName, 'has the lowest average temperateure in the list, with a temperature of', lowestTempValue, 'C')
input('Press enter to quit')
quit()
