from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from utils.gui_helper import Gui_Helper
from utils.style import regular, background, regular_text


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

    def create_time_date(self, layout):
        self.date_label = QLabel(self.date)
        self.date_label.setStyleSheet(regular_text)  # change with paragraph

        self.time_label = QLabel(self.time)
        self.time_label.setStyleSheet(regular_text)  # change with paragraph

        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)

    def create_description(self, layout):
        self.description_label = QLabel(self.description)
        self.description_label.setFixedWidth(self.width * 0.55)
        self.description_label.setStyleSheet(
            regular_text)  # change with paragraph

        layout.setAlignment(Qt.alignCenter)
        layout.addWidget(self.description_label)

    def create_event_name(self, layout):
        self.event_name_label = QLabel(self.event_name)
        self.event_name_label.setStyleSheet(
            regular_text)  # change with paragraph

        layout.setAlignment(Qt.alignCenter)
        layout.addWidget(self.event_name_label)

    def create_amount(self, layout):
        self.event_amount_label = QLabel(self.event_name)
        color = '#ff0000'
        if self.name == 'despoit' or 'Recieve' in self.name:
            color == '#00ff00'

        self.event_amount_label.setStyleSheet(
            f"background-color: transparent; color: {color}, font-size: 12px;")

        layout.setAlignment(Qt.alignCenter)
        layout.addWidget(self.event_name_label)

    def UI(self):
        # Create main layout
        event_layout, event_layout_box = Gui_Helper.make_layout_full(
            background, self.width, self.height, direction=1)

        # Seperate to left, middle left, middle_right & right
        event_layout_right, event_layout_right_box = Gui_Helper.make_layout_full(
            background, self.width * 0.1, self.height)
        event_layout_middle_right, event_layout_middle_right_box = Gui_Helper.make_layout_full(
            background, self.width * 0.55, self.height)
        event_layout_middle_left, event_layout_middle_left_box = Gui_Helper.make_layout_full(
            background, self.width * 0.15, self.height)
        event_layout_left, event_layout_left_box = Gui_Helper.make_layout_full(
            background, self.width * 0.20, self.height)

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
