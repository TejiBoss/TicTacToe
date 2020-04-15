class GamePlayer:

    def __init__(self, name):
        self.name = name
        self.letter = ' '

    def __repr__(self):
        return '<'+self.name + " is playing with letter " + self.letter+'>'

    def getMove(self):
        move = " "
        while move not in "1 2 3 4 5 6 7 8 9".split():
            move = input(self.name + " What is your next move? (1-9) ")
        return int(move)

    def setLetter(self, letter):
        self.letter = letter

    def getLetter(self):
        return self.letter

    def getName(self):
        return self.name
