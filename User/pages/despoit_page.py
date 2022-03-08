from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from utils.gui_helper import Gui_Helper
from utils.style import *

from components.option_menu import Option_Menu
from components.message_button import Message_button


class Despoit_page(QWidget):
    def __init__(self, width, height, send_function, option_menu, type):
        super().__init__()
        self.type = type
        self.width = width
        self.height = height
        self.send_function = send_function
        self.option_menu = option_menu
        self.option_width = 200
        self.make_type()
        self.UI()

    def make_type(self):
        if self.type == 'despoit':
            self.title_text = 'Despoit'
            self.message_code = 21
        else:
            self.title_text = 'Extract'
            self.message_code = 22

    def UI(self):
        self.create_widgets()
        self.create_layouts()

    def create_layouts(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            background, self.width, self.height, direction=1)

        # Create the left part
        left_section_width = self.width - self.option_width
        card_height = self.height * 0.5

        self.left_section, self.left_section_box = Gui_Helper.make_layout_full(
            homepage_background, left_section_width, self.height)
        self.left_section.setAlignment(Qt.AlignCenter)

        # Create the card
        self.card, self.card_box = Gui_Helper.make_layout_full(
            login_layout_box, left_section_width * 0.9, card_height)

        card_top, card_top_box = Gui_Helper.make_layout_full(
            homepage_card_top, left_section_width * 0.9, card_height * 0.2)
        card_top.setAlignment(Qt.AlignCenter)
        card_bottom, card_bottom_box = Gui_Helper.make_layout_full(
            regular, width=left_section_width * 0.9, height=card_height * 0.8, direction=1)
        card_top.setAlignment(Qt.AlignHCenter)

        card_top.addWidget(self.title)

        self.card.addWidget(card_top_box)
        self.card.addWidget(card_bottom_box)

        self.left_section.addWidget(self.card_box)

        self.main_page.addWidget(self.left_section_box)
        self.main_page.addWidget(self.option_menu.main_layout_box)

    def create_widgets(self):
        # Create the title
        self.title = QLabel(self.title_text)
        self.title.setStyleSheet(big_text())

        # Create the form

        # create the button
        self.submit_button = Message_button(
            'Submit', 'User\\assets\\arrow-right-icon.svg', lambda x: print(1))
