from stats import Stats
from .tasks_importer import tasks

class UsefulB:
    def __init__(self):
        self.t = list(tasks.values())[0].Task()
        self.solved = True
        self.stat = Stats()

    def getQuestion(self):
        if self.solved:
            self.t.generateNew()
            self.solved = False

        self.stat.log_solving(self.t)
        return self.t.getText()

    def checkAnswer(self, ans):
        if self.t.checkAnswer(ans):
            self.stat.log_good(self.t)
            self.solved = True

            return True
        else:
            self.stat.log_wrong(self.t, ans)

            return False

