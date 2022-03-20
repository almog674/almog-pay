from ctypes import alignment
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from utils.gui_helper import Gui_Helper
from utils.style import regular, event_background, regular_text, amount_style_red, amount_style_green, paragraph


class Event_box(QWidget):
    def __init__(self, width, height, date, time, description, name, amount):
        super().__init__()
        self.width = width
        self.height = height
        self.date = date
        self.time = time
        self.description = description
        self.name = name
        self.amount = amount
        self.UI()

    def create_time_date(self, layout):
        self.date_label = QLabel(self.date)
        self.date_label.setStyleSheet(paragraph())  # change with paragraph

        self.time_label = QLabel(self.time)
        self.time_label.setStyleSheet(paragraph())  # change with paragraph

        layout.addWidget(self.date_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.time_label, alignment=Qt.AlignCenter)

    def create_description(self, layout):
        self.description_label = QLabel(self.description)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setWordWrap(True)
        self.description_label.setFixedWidth(self.width * 0.55)
        self.description_label.setStyleSheet(
            paragraph())  # change with paragraph

        print(self.description_label.text())

        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.description_label, alignment=Qt.AlignCenter)

    def create_event_name(self, layout):
        self.event_name_label = QLabel(self.name)
        self.event_name_label.setWordWrap(True)
        self.event_name_label.setStyleSheet(
            paragraph())  # change with paragraph

        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.event_name_label)

    def create_amount(self, layout):
        self.event_amount_label = QLabel(f"{str(self.amount)}$")
        self.event_amount_label.setWordWrap(True)
        if self.name == 'despoit' or 'Recieve' in self.name:
            self.event_amount_label.setStyleSheet(amount_style_green())
        else:
            self.event_amount_label.setStyleSheet(amount_style_red())

        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.event_amount_label)

    def UI(self):
        # Create main layout
        event_layout, self.event_layout_box = Gui_Helper.make_layout_full(
            event_background, self.width, self.height, direction=1)

        # Seperate to left, middle left, middle_right & right
        event_layout_right, event_layout_right_box = Gui_Helper.make_layout_full(
            regular, self.width * 0.15, self.height)
        event_layout_middle_right, event_layout_middle_right_box = Gui_Helper.make_layout_full(
            regular, self.width * 0.55, self.height)
        event_layout_middle_left, event_layout_middle_left_box = Gui_Helper.make_layout_full(
            regular, self.width * 0.15, self.height)
        event_layout_left, event_layout_left_box = Gui_Helper.make_layout_full(
            regular, self.width * 0.15, self.height)

        # Create the timedate part
        self.create_time_date(event_layout_right)

        # Create the description part
        self.create_description(event_layout_middle_right)

        # Create the events_name
        self.create_event_name(event_layout_middle_left)

        # Create the amount with green or red
        self.create_amount(event_layout_left)

        event_layout.addWidget(event_layout_right_box)
        event_layout.addWidget(event_layout_middle_right_box)
        event_layout.addWidget(event_layout_middle_left_box)
        event_layout.addWidget(event_layout_left_box)
