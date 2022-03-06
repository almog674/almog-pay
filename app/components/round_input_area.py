from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ..gui_helper import Gui_Helper
from ..style import *


class Round_Input_Area():
    types_map = {'user': ["assets/user-solid.svg", 'Username'], 'email': ['assets\email-icon.svg', 'Email'],
                 'password': ['assets\lock-solid.svg', 'Password'], 'password_confirm': ['assets\lock-solid.svg', 'Password Again']}

    def __init__(self, width, height, style_function=login_field, icon_function=field_icon, type='user', focus_number=-1):
        self.width = width
        self.height = height
        self.style_function = style_function
        self.icon_fucntion = icon_function
        self.type = type
        self.focus_number = focus_number

    def UI(self):
        self.input_icon = QToolButton()
        self.input_icon.setDisabled(True)
        self.input_icon.setStyleSheet(self.style_function())
        self.input_icon.setIcon(QIcon(self.types_map[self.type][0]))
        self.input_field = QLineEdit()
        self.input_field.setFrame(False)
        self.input_field.setPlaceholderText(self.types_map[self.type][1])
        self.input_field.setStyleSheet(self.icon_fucntion)

        self.input_layout, self.input_layout_box = Gui_Helper.make_layout_full(
            login_feild, self.width, self.height, direction=1)
        self.input_layout_box.setAlignment(Qt.AlignHCenter)
        self.input_layout.addWidget(self.user_icon)
        self.input_layout.addWidget(self.user_field)
