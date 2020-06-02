from time import sleep
from ui.gtk_break_screen import GtkBreakScreen, sendNotify
from core import UsefulB


INTERVAL = 60 * 15
PREPARING_TIME = 3

a = UsefulB()

while True:
    sleep(INTERVAL - PREPARING_TIME)
    sendNotify("Get ready for a break after " +
            str(PREPARING_TIME) + " seconds", PREPARING_TIME)
    sleep(PREPARING_TIME)

    text = a.getQuestion()

    br = GtkBreakScreen(text, lambda ans: a.checkAnswer(ans))
    # this will be wait for task solved
    br.start()

