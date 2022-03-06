from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from utils.style import regular, regular_text
from utils.gui_helper import Gui_Helper
from utils.style import background


class Option_Menu(QWidget):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.UI()

    def UI(self):
        self.main_layout, self.main_layout_box = Gui_Helper.make_layout_full(
            background, self.width, self.height, direction=0)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.main_layout.setSpacing(0)

        self.create_title(self.main_layout)
        self.create_option('option 1', 'User\\assets\\email-icon.svg')
        self.create_option('option 2', 'User\\assets\\email-icon.svg')
        self.create_option('option 3', 'User\\assets\\user-icon.svg')
        self.create_option('option 4', 'User\\assets\\lock-icon.svg')

    def create_title(self, layout):
        title_layout, title_layout_box = Gui_Helper.make_layout_full(
            background, self.width, 75, direction=0)
        title_layout.setAlignment(Qt.AlignCenter)

        title = QLabel('Option Menu')
        title.setStyleSheet(regular_text())
        title_layout.addWidget(title)
        layout.addWidget(title_layout_box)

    def create_option(self, text, icon, function=lambda x: print(1)):
        option_layout, option_layout_box = Gui_Helper.make_layout_full(
            regular, self.width, 75, direction=1)

        option_label = QLabel(text)
        option_label.setStyleSheet(regular_text())
        option_icon = Gui_Helper.make_icon(
            self=self, url=icon, width=25, height=25)

        option_layout_box.setCursor(Qt.PointingHandCursor)

        option_layout.addStretch(3)
        option_layout.addWidget(option_label)
        option_layout.addStretch(1)
        option_layout.addWidget(option_icon)
        option_layout.addStretch(3)

        option_layout_box.mouseReleaseEvent = function
        option_label.mouseReleaseEvent = function
        option_icon.mouseReleaseEvent = function

        self.main_layout.addWidget(option_layout_box)
