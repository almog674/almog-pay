from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from utils.Global_state import Global_State
from utils.gui_helper import Gui_Helper
from utils.style import *

from components.message_button import Message_button
from components.regular_field import Regular_Field


class Despoit_page(QWidget):
    def __init__(self, width, height, send_function, update_function, type):
        super().__init__()
        self.type = type
        self.width = width
        self.height = height
        self.send_function = send_function
        self.update_function = update_function
        self.make_type()
        self.UI()

    def make_type(self):
        if self.type == 'despoit':
            self.title_text = 'Despoit'
            self.message_code = 21
        else:
            self.title_text = 'Extract'
            self.message_code = 22

    def submit(self, event=None):
        amount = self.amount_field.line_edit.text()
        if not amount.isnumeric():
            return Gui_Helper.make_message_box('The amount of data have to be numerical', 'Error')
        amount = round(int(amount), 1)
        if amount > 1500:
            return Gui_Helper.make_message_box('The maximum is 1,500$', 'Error')
        self.send_function(self.message_code, Global_State.user['username'],
                           amount, reciever='[SERVER]')
        self.amount_field.line_edit.setText('')
        self.update_function()

    def UI(self):
        self.create_widgets()
        self.create_layouts()

        self.setLayout(self.main_page)

    def create_layouts(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            background, self.width, self.height, direction=1)

        # Create the left part
        self.left_section, self.left_section_box = Gui_Helper.make_layout_full(
            homepage_background, self.width, self.height)
        self.left_section_box.setAlignment(Qt.AlignVCenter)

        self.amount_field = Regular_Field(
            185, 40, 'User\\assets\extract.svg', 'Amount Of money')

        self.left_section.addStretch(2)
        self.left_section.addWidget(self.title, alignment=Qt.AlignCenter)
        self.left_section.addStretch(4)
        self.left_section.addWidget(
            self.amount_field.field_box, alignment=Qt.AlignCenter)
        self.left_section.addStretch(2)
        self.left_section.addWidget(
            self.max_amount_label, alignment=Qt.AlignCenter)
        self.left_section.addStretch(6)
        self.left_section.addWidget(
            self.submit_button, alignment=Qt.AlignCenter)
        self.left_section.addStretch(2)

        self.main_page.addWidget(self.left_section_box)

    def create_widgets(self):
        # Create the title
        self.title = QLabel(self.title_text)
        self.title.setStyleSheet(title())

        # Create the Text
        self.max_amount_label = QLabel('Max amount: 1,500$')
        self.max_amount_label.setStyleSheet(big_text())

        # create the button
        self.submit_button = Message_button(
            'Submit', 'User\\assets\\arrow-right-icon.svg', self.submit)
