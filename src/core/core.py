from stats import Stats
from .tasks_importer import tasks

class UsefulB:
    def __init__(self, _ui):
        self.ui = _ui

        self.next_task_num = 0
        self.switchToNextTask()

        self.solved = True
        self.stat = Stats()

    def start(self):
        if self.solved:
            self.cur_task.generateNew()
            self.solved = False

        self.onStart()

        self.ui.setQuestionText(self.cur_task.getText())
        self.ui.setAnsChecker(lambda ans: self.checkAnswer(ans))
        # it will wait until problem is solved
        self.ui.show()


    def checkAnswer(self, ans):
        if self.cur_task.checkAnswer(ans):
            self.onGoodAns()

            self.ui.hide()

            self.solved = True
            self.switchToNextTask()

            return True
        else:
            self.onWrongAns(ans)

            return False


    def switchToNextTask(self):
        self.cur_task = tasks[self.next_task_num]
        self.next_task_num += 1
        if self.next_task_num >= len(tasks):
            self.next_task_num = 0


    def onStart(self):
        self.stat.log_solving(self.cur_task)
        self.ui.sendNotify(self.cur_task.getTextSolving())

    def onGoodAns(self):
        self.stat.log_good(self.cur_task)
        self.ui.sendNotify(self.cur_task.getTextGood())

    def onWrongAns(self, ans):
        self.stat.log_wrong(self.cur_task, ans)
        self.ui.sendNotify(self.cur_task.getTextWrong(ans))


