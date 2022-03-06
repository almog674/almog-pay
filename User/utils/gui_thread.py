from PyQt5.QtCore import pyqtSignal, QThread


class Gui_Thread(QThread):
    make_message_box = pyqtSignal(bool)
    go_to_main = pyqtSignal(bool)

    def make_message_box_func(self):
        self.make_message_box.emit(True)

    def go_to_main_func(self):
        self.go_to_main.emit(True)
