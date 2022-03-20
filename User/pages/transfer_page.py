from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from utils.Global_state import Global_State
from utils.gui_helper import Gui_Helper
from utils.style import *

from components.message_button import Message_button
from components.regular_field import Regular_Field


class Transfer_Page(QWidget):
    def __init__(self, width, height, send_function, update_function):
        super().__init__()
        self.type = type
        self.width = width
        self.height = height
        self.send_function = send_function
        self.update_function = update_function
        self.UI()

    def submit(self, event=None):
        amount = self.amount_field.get_text()
        description = self.description_area.toPlainText()
        reciever = self.reciever_field.get_text()

        # Check for validation
        if len(reciever) == 0:
            return Gui_Helper.make_message_box('Please specify user to send the money', 'Error')
        if not amount.isnumeric():
            return Gui_Helper.make_message_box('The amount of data have to be numerical', 'Error')
        amount = round(int(amount), 1)
        if amount > 1500:
            return Gui_Helper.make_message_box('The maximum is 1,500$', 'Error')

        # Send the message to the server
        data = {'amount': amount, 'description': description}
        self.send_function(23, Global_State.user['username'],
                           data, reciever=reciever)

        # Clear the fields & update the homepage
        self.amount_field.clear_field()
        self.reciever_field.clear_field()
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

        self.description_area = QPlainTextEdit()
        self.description_area.setFixedSize(185, 100)

        self.reciever_field = Regular_Field(
            185, 40, 'User\\assets\\user-solid.svg', 'Name')

        self.amount_field = Regular_Field(
            185, 40, 'User\\assets\extract.svg', 'Amount Of money')

        self.left_section.addWidget(self.title, alignment=Qt.AlignCenter)
        self.left_section.addWidget(
            self.reciever_field.field_box, alignment=Qt.AlignCenter)
        self.left_section.addWidget(
            self.amount_field.field_box, alignment=Qt.AlignCenter)

        self.left_section.addWidget(
            self.description_area, alignment=Qt.AlignCenter)
        self.left_section.addWidget(
            self.max_amount_label, alignment=Qt.AlignCenter)
        self.left_section.addWidget(
            self.submit_button, alignment=Qt.AlignCenter)

        self.main_page.addWidget(self.left_section_box)

    def create_widgets(self):
        # Create the title
        self.title = QLabel('Transfer Money')
        self.title.setStyleSheet(title())

        # Create the Text
        self.max_amount_label = QLabel('Max amount: 1,500$')
        self.max_amount_label.setStyleSheet(big_text())

        # create the button
        self.submit_button = Message_button(
            'Submit', 'User\\assets\\arrow-right-icon.svg', self.submit)
