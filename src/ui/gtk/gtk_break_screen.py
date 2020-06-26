import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init("UsefulB")

from pathlib import Path
GLADE_FILE = str(Path(__file__).parent / "gtk_break_screen.glade")


class GtkBreakScreen:
    def __init__(self):
        self.buildUI()
        self.setAnnoying()

    def buildUI(self):
        builder = Gtk.Builder()
        builder.add_from_file(GLADE_FILE)
        self.win = builder.get_object("main_window")

        self.answer_area = builder.get_object("answer_area")
        self.question_label = builder.get_object("question_label")
        answer_history = builder.get_object("entry_history")

        builder.connect_signals({
            "enter_pressed": self.signal_enter_pressed_handler,
            "win_delete_event": self.signal_delete_event_handler
            })

        self.initHistory(answer_history)

    def initHistory(self, answer_history):
        self.answer_area.set_completion(answer_history)
        answer_history.set_match_func(lambda a, b, c: True)

        self.histoy_list_store = Gtk.ListStore(str)

        answer_history.set_model(self.histoy_list_store)
        answer_history.set_text_column(0)
        answer_history.set_minimum_key_length(0)

    def setAnnoying(self):
        self.win.set_keep_above(True)
        self.win.stick()

        gdk_w = self.win.get_screen()
        self.win.resize(gdk_w.width(), gdk_w.height())

        self.win.set_decorated(False)
        self.win.fullscreen()


    def show(self):
        self.win.show_all()
        Gtk.main()

    def hide(self):
        self.win.hide()
        Gtk.main_quit()


    def signal_delete_event_handler(self, a, b):
        self.sendNotify("You can't kill me. Keep solving task")
        return True

    def signal_enter_pressed_handler(self, a):
        entered_ans = a.get_text()
        a.set_text("")

        ans_res = self.checkAnswer_callback(entered_ans)

        # update answers history
        if not ans_res:
            self.histoy_list_store.prepend([entered_ans])


    def setQuestionText(self, new_text):
        self.question_label.set_text(new_text)

    def setAnsChecker(self, func):
        self.checkAnswer_callback = func


    def sendNotify(self, text, time=3):
        noti = Notify.Notification.new("UsefulB", text)
        noti.set_timeout(time * 1000)
        noti.show()

