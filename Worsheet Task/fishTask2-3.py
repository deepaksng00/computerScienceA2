class Animal:
    def __init__(self, s, n):
        self.state = s
        self.size = n
    def feed(self):
        self.size = self.size + 1
        print('Fish fed')
        if self.size == 5:
            self.state = 'FISH'
    def getState(self):
        return self.state
    def getSize(self):
        return self.size

thisFish = Animal("Fish", 1)
print(thisFish.getState(),'is of size', thisFish.getSize())
while thisFish.getState() != 'FISH':
    thisFish.feed()
print('It is now a big', thisFish.getState())
