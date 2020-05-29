from time import sleep
from ui.gtk_break_screen import GtkBreakScreen
from core import UsefulB


a = UsefulB()

while True:
    text = a.getQuestion()

    br = GtkBreakScreen(text, lambda ans: a.checkAnswer(ans))
    br.start()

    # after BreakScreen finished => task solved
    sleep(10)
