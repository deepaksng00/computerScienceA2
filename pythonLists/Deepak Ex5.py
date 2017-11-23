# Deepak Singh
# Ex.5a, b, c, d

import random

topScores = [('AAA01', 135),
             ('BBB01', 87),
             ('CCC01', 188),
             ('DDD01', 109)]

def __init__():
    found = False
    userID_input = input('Please enter your Used ID: ')
    if userID_input == 'xxx':
        quit()
    else:
        core(userID_input, found)
        
def core(userID_input, found):
    for Key, Value in topScores:
        if Key == userID_input:
            found = True
    if found == False:
        topScores.append((userID_input, 0))
    userScore = random.randint(50, 200)
    for Key, Value in topScores:
        if Key == userID_input:
            if Value < userScore:
                indexValue = (topScores.index((Key, Value)))
                topScores[(indexValue)] = (Key, userScore)
    print(topScores)
    __init__()

__init__()


    
