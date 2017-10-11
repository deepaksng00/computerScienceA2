def feed(state, size):
    size += 1
    print('Fish fed')
    if size == 5:
        state = 'FISH'

thisFishState = 'Fish'
thisFishSize = 1
print(thisFishState, 'is of size', thisFishSize)
while thisFishState != 'FISH':
    feed(thisFishState, thisFishSize)
print('It is now a big', thisFishState)
