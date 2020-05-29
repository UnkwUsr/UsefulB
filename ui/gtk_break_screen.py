import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

GLADE_FILE = "ui/gtk_break_screen.glade"

class GtkBreakScreen:
    def __init__(self, question_text, checkAnswer_callback):
        self.checkAnswer_callback = checkAnswer_callback

        builder = Gtk.Builder()
        builder.add_from_file(GLADE_FILE)
        self.win = builder.get_object("main_window")

        self.answer_area = builder.get_object("answer_area")
        self.question_label = builder.get_object("question_label")
        answer_history = builder.get_object("entry_history")

        self.initHistory(answer_history)

        builder.connect_signals({
            "enter_pressed": self.signal_enter_pressed_handler,
            "win_delete_event": self.signal_delete_event_handler
            })

        self.setAnnoying()
        self.setQuestionText(question_text)

        self.count_wrongs = 0
    def initHistory(self, answer_history):
        self.answer_area.set_completion(answer_history)
        answer_history.set_match_func(lambda a, b, c: True)

        self.histoy_list_store = Gtk.ListStore(str)

        answer_history.set_model(self.histoy_list_store)
        answer_history.set_text_column(0)
        answer_history.set_minimum_key_length(0)


    def start(self):
        self.win.show_all()
        Gtk.main()

    def signal_delete_event_handler(self, a, b):
        print("You cant kill me... Just solve task")
        return True

    def signal_enter_pressed_handler(self, a):
        if self.checkAnswer_callback(a.get_text()):
            self.win.destroy()
            Gtk.main_quit()
        else:
            self.count_wrongs += 1

            self.histoy_list_store.prepend([a.get_text()])

            a.set_text("Wrong answer![" + str(self.count_wrongs) + "]")
            # select from start to end
            a.select_region(0, -1)

    def setAnnoying(self):
        self.win.set_keep_above(True)
        self.win.stick()

        gdk_w = self.win.get_screen()
        self.win.resize(gdk_w.width(), gdk_w.height())

        self.win.set_decorated(False)
        self.win.fullscreen()

    def setQuestionText(self, new_text):
        self.question_label.set_text(new_text)


