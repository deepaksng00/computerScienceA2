# Deepak Singh
# Ex.2

import math

names = []

def inputNames():
    name = input('Enter as many names as you like, enter \"End\" when you want to stop: ')
    names.append(name)
    if name == "End":
        quit()
    print(names[0:math.ceil(len(names)/2)])
    inputNames()

inputNames()
