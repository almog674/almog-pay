from PyQt5.QtWidgets import QWidget, QLineEdit, QToolButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from utils.style import *
from utils.gui_helper import Gui_Helper


class Regular_Field:
    def __init__(self, width, height, icon_url, place_holder='', is_password=False):
        self.width = width
        self.height = height
        self.icon_url = icon_url
        self.place_holder = place_holder
        self.is_password = is_password
        self.UI()

    def get_text(self):
        return self.line_edit.text()

    def clear_field(self):
        self.line_edit.setText('')

    def UI(self):
        self.icon = QToolButton()
        self.icon.setDisabled(True)
        self.icon.setStyleSheet(field_icon())
        self.icon.setIcon(QIcon(self.icon_url))
        self.line_edit = QLineEdit()
        self.line_edit.setFrame(False)
        if self.is_password:
            self.line_edit.setEchoMode(QLineEdit.Password)
        self.line_edit.setPlaceholderText(self.place_holder)
        self.line_edit.setStyleSheet(login_field())

        field, self.field_box = Gui_Helper.make_layout_full(
            login_feild, self.width, self.height, direction=1)
        self.field_box.setAlignment(Qt.AlignHCenter)

        field.addWidget(self.icon)
        field.addWidget(self.line_edit)
