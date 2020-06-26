TASK_NAME = "Relax"

from config import config_get
# config format: float, minutes
IDLING_TIME = int(float(config_get(TASK_NAME, "idling_time", 5.0)) * 60)

class Task:
    def __init__(self):
        pass

    def generateNew(self):
        self.time = itime()
        self.skipped = False

    def checkAnswer(self, ans):
        if (itime() - self.time) >= IDLING_TIME:
            return True
        elif ans == "skip":
            self.skipped = True
            return True
        else:
            return False

    def getText(self):
        return "Relax for " + str(IDLING_TIME) + " seconds"

    # For stats:
    def getName(self):
        return TASK_NAME
    def getTextSolving(self):
        return "Relaxing..."
    def getTextWrong(self, ans):
        return str(IDLING_TIME - (itime() - self.time)) + " seconds remain. If you want abort relaxation - type 'skip'"
    def getTextGood(self):
        if self.skipped:
            return "Relaxation skipped"
        else:
            return "Relaxed for " + str(itime() - self.time) + " seconds. Feel fresh!"

from time import time
def itime():
    return int(time())

