from random import randint

TASK_NAME = "MathProblem"

from config import config_get
# config format: int
MIN_VAL = int(config_get(TASK_NAME, "min_number", 1))
# config format: int
MAX_VAL = int(config_get(TASK_NAME, "max_number", 50))

class Task:
    def __init__(self):
        self.text = 0
        self.solution = 0

    def generateNew(self):
        a = randint(MIN_VAL, MAX_VAL)
        b = randint(MIN_VAL, MAX_VAL)

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
        return TASK_NAME
    def getTextSolving(self):
        return "Solving " + self.getText()
    def getTextWrong(self, ans):
        return ans + " is wrong answer!"
    def getTextGood(self):
        return "Good job:D"

