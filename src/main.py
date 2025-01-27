# this block should be first if We want
# has section 'Main' on top of config file
from config import config_get
# config format: float, minutes
INTERVAL = int(float(config_get("Main", "break_interval", 15.0)) * 60)
# config format: int, seconds
PREPARING_TIME = int(config_get("Main", "preparing_time", 3))
if(PREPARING_TIME > INTERVAL):
    exit("[ERROR] preparing_time can't be greater than break_interval")
if(PREPARING_TIME < 0):
    exit("[ERROR] preparing_time can't be negative number")

from time import sleep
from ui.gtk.gtk_break_screen import GtkBreakScreen
from core.core import UsefulB

ui = GtkBreakScreen()
cor = UsefulB(ui)

while True:
    sleep(INTERVAL - PREPARING_TIME)
    if(PREPARING_TIME != 0):
        ui.sendNotify("Get ready for a break after " +
                str(PREPARING_TIME) + " seconds", PREPARING_TIME)
        sleep(PREPARING_TIME)

    # it will wait until problem is solved
    cor.start()

