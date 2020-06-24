from random import randint

from config import config_get
# need for create entries in config file on startup
config_get("Task1", "min_number", 1)
config_get("Task1", "max_number", 50)

class Task:
    def __init__(self):
        self.text = 0
        self.solution = 0

    def generateNew(self):
        min_val = int(config_get("Task1", "min_number", 1))
        max_val = int(config_get("Task1", "max_number", 50))
        a = randint(min_val, max_val)
        b = randint(min_val, max_val)

        self.text = str(a) + " * " + str(b) + " = ?"
        self.solution = a * b

    def checkAnswer(self, ans):
        if ans == str(self.solution):
            return True
        else:
            return False

    def getText(self):
        return self.text

    # For stats:
    def getName(self):
        return "MathProblem"
    def getTextSolving(self):
        return "Solving " + self.getText()
    def getTextWrong(self, ans):
        return ans + " is wrong answer!"
    def getTextGood(self):
        return "Good job:D"

