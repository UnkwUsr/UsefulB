from datetime import datetime

from config import config_get
from pathlib import Path
STAT_PATH = config_get("Stats", "file_path", str(Path.home() / ".config//usefulB/stats"))

class Stats:
    def __init__(self):
        time = datetime.now().strftime('%m-%d %H:%M:%S')
        from os.path import isfile
        newline = "\n" if isfile(STAT_PATH) else ""
        self.write(newline + "--- Started at " + time + " ---", False)

    def log_solving(self, task):
        txt = self.construct_task_name(task)
        # tag 'processing'
        txt += "[~] "
        txt += task.getTextSolving()
        self.write(txt)

    def log_wrong(self, task, ans):
        txt = self.construct_task_name(task)
        # tag 'wrong'
        txt += "[-] "
        txt += task.getTextWrong(ans)
        self.write(txt)

    def log_good(self, task):
        txt = self.construct_task_name(task)
        # tag 'good'
        txt += "[+] "
        txt += task.getTextGood()
        self.write(txt)

    def construct_task_name(self, task):
        return "[" + task.getName() + "] "

    def write(self, txt, with_time=True):
        time = ""
        if with_time:
            time = datetime.now().strftime('%H:%M:%S') + " "

        if STAT_PATH != "":
            with open(STAT_PATH, 'a') as file:
                file.write(time + txt + "\n")

