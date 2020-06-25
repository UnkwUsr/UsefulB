from stats import Stats
from .tasks_importer import tasks

class UsefulB:
    def __init__(self):
        self.next_task_num = 0
        self.switchToNextTask()

        self.solved = True
        self.stat = Stats()

    def getQuestion(self):
        if self.solved:
            self.cur_task.generateNew()
            self.solved = False

        self.stat.log_solving(self.cur_task)
        return self.cur_task.getText()

    def checkAnswer(self, ans):
        if self.cur_task.checkAnswer(ans):
            self.stat.log_good(self.cur_task)
            self.solved = True

            self.switchToNextTask()

            return True
        else:
            self.stat.log_wrong(self.cur_task, ans)

            return False

    def switchToNextTask(self):
        self.cur_task = tasks[self.next_task_num]
        self.next_task_num += 1
        if self.next_task_num >= len(tasks):
            self.next_task_num = 0
