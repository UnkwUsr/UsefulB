from random import randint

class Task:
    def __init__(self):
        self.text = 0
        self.solution = 0

    def generateNew(self):
        a = randint(1, 50)
        b = randint(1, 50)

        self.text = str(a) + " * " + str(b) + " = ?"
        self.solution = a * b

    def checkAnswer(self, ans):
        if ans == str(self.solution):
            return True
        else:
            return False

    def getText(self):
        return self.text
