from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from utils.style import regular, regular_text, background, option_menu_background, option_bar_text
from utils.gui_helper import Gui_Helper
from .option import Option


class Option_Menu(QWidget):
    def __init__(self, width, height, functions):
        super().__init__()
        self.width = width
        self.height = height
        self.functions = functions
        self.UI()

    def UI(self):
        self.main_layout, self.main_layout_box = Gui_Helper.make_layout_full(
            option_menu_background, self.width, self.height, direction=0)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setSpacing(0)

        self.create_title(self.main_layout)
        option_one = Option(
            'Homepage', 'User\\assets\\home.svg', lambda x: self.functions[0](), self.width)
        option_two = Option(
            'Despoit', 'User\\assets\\despoit.svg', lambda x: self.functions[1](3), self.width)
        option_three = Option(
            'Extract', 'User\\assets\\extract.svg', lambda x: self.functions[1](4), self.width)
        option_four = Option(
            'Transfer', 'User\\assets\\transfer.svg', lambda x: self.functions[1](5), self.width)
        option_five = Option(
            'Inbox', 'User\\assets\\inbox.svg', lambda x: self.functions[1](6), self.width)
        option_six = Option(
            'Logout', 'User\\assets\\logout.svg', lambda x: self.functions[2](), self.width)
        self.main_layout.addWidget(option_one)
        self.main_layout.addWidget(option_two)
        self.main_layout.addWidget(option_three)
        self.main_layout.addWidget(option_four)
        self.main_layout.addWidget(option_five)
        self.main_layout.addWidget(option_six)

    def create_title(self, layout):
        title_layout, title_layout_box = Gui_Helper.make_layout_full(
            option_bar_text, self.width, 75, direction=0)
        title_layout.setAlignment(Qt.AlignCenter)

        title = QLabel('Option Menu')
        title.setStyleSheet(regular_text())
        title_layout.addWidget(title)
        layout.addWidget(title_layout_box)
