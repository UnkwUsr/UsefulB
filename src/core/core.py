from .tasks_importer import tasks

class UsefulB:
    def __init__(self):
        self.t = list(tasks.values())[0].Task()
        self.solved = True

    def getQuestion(self):
        if self.solved:
            self.t.generateNew()
            self.solved = False

        return self.t.getText()

    def checkAnswer(self, ans):
        if self.t.checkAnswer(ans):
            print("Good job:D")
            self.solved = True

            return True
        else:
            print("Wrong answer!")

            return False

