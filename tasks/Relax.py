TASK_NAME = "Relax"
CONFIG = {
        # config format: float, minutes
        "idling_time": 5.0
        }

class Task:
    def __init__(self):
        CONFIG["idling_time"] = int(CONFIG["idling_time"] * 60)

    def generateNew(self):
        self.time = itime()
        self.skipped = False

    def checkAnswer(self, ans):
        if (itime() - self.time) >= CONFIG["idling_time"]:
            return True
        elif ans == "skip":
            self.skipped = True
            return True
        else:
            return False

    def getText(self):
        return "Relax for " + str(CONFIG["idling_time"]) + " seconds"

    # For stats:
    def getName(self):
        return TASK_NAME
    def getTextSolving(self):
        return "Relaxing..."
    def getTextWrong(self, ans):
        return str(CONFIG["idling_time"] - (itime() - self.time)) + " seconds remain. If you want abort relaxation - type 'skip'"
    def getTextGood(self):
        if self.skipped:
            return "Relaxation skipped"
        else:
            return "Relaxed for " + str(itime() - self.time) + " seconds. Feel fresh!"

from time import time
def itime():
    return int(time())

