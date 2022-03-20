from tkinter import Label
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap

from utils.gui_helper import Gui_Helper
from utils.style import *
from utils.Global_state import Global_State

from components.option_menu import Option_Menu
from components.event_box import Event_box


class Home_Page(QWidget):
    def __init__(self, width, height, option_menu):
        super().__init__()
        self.width = width
        self.height = height
        self.option_menu = option_menu
        self.option_width = 200

        self.UI()

    def update_page(self):
        self.title.setText(f'Account state: {Global_State.user["username"]}')
        self.card_title.setText(
            f'Current Balance: {Global_State.user["account_balance"]}$')
        self.high_label.setText(
            f'All time high: {Global_State.user["all_time_high"]}$')
        self.low_label.setText(
            f'All time low: {Global_State.user["all_time_low"]}$')
        self.frame_label.setText(
            f'Frame: {Global_State.user["frame"]}$')
        self.max_payment_label.setText(
            f'Max Payment: 1,500$')

        # self.update_events()

    def UI(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            homepage_title, self.width, self.height, direction=1)

        self.create_Widgets()
        self.create_layouts()

    def create_middle_card(self, section_width):
        card_height = self.height * 0.45
        self.middle_card, self.middle_card_box = Gui_Helper.make_layout_full(
            login_layout_box, section_width * 0.9, card_height)

        card_top, card_top_box = Gui_Helper.make_layout_full(
            homepage_card_top, section_width * 0.9, card_height * 0.2)
        card_top.setAlignment(Qt.AlignCenter)
        card_bottom, card_bottom_box = Gui_Helper.make_layout_full(
            regular, width=section_width * 0.9, height=card_height * 0.8, direction=1)

        self.high_label = QLabel(
            f'All time high: {Global_State.user["all_time_high"]}$')
        self.low_label = QLabel(
            f'All time Low: {Global_State.user["all_time_low"]}$')
        self.frame_label = QLabel(
            f'Frame: {Global_State.user["frame"]}$')
        self.max_payment_label = QLabel(
            f'Max Payment: 1,500$')

        self.high_label.setStyleSheet(big_text())
        self.low_label.setStyleSheet(big_text())
        self.frame_label.setStyleSheet(big_text())
        self.max_payment_label.setStyleSheet(big_text())

        card_bottom_left, card_bottom_left_box = Gui_Helper.make_layout_full(
            regular, section_width * 0.45, card_height * 0.4)
        card_bottom_left.setAlignment(Qt.AlignHCenter)
        card_bottom_right, card_bottom_right_box = Gui_Helper.make_layout_full(
            regular, section_width * 0.45, card_height * 0.4)
        card_bottom_right.setAlignment(Qt.AlignHCenter)

        self.card_title = QLabel(
            f'Current Balance: {Global_State.user["account_balance"]}$')
        self.card_title.setStyleSheet(big_text())

        card_top.addWidget(self.card_title)

        card_bottom_left.addStretch(1)
        card_bottom_left.addWidget(self.high_label)
        card_bottom_left.addStretch(3)
        card_bottom_left.addWidget(self.frame_label)
        card_bottom_left.addStretch(1)

        card_bottom_right.addStretch(1)
        card_bottom_right.addWidget(self.low_label)
        card_bottom_right.addStretch(3)
        card_bottom_right.addWidget(self.max_payment_label)
        card_bottom_right.addStretch(1)

        card_bottom.addWidget(card_bottom_left_box)
        card_bottom.addWidget(card_bottom_right_box)

        self.middle_card.addWidget(card_top_box)
        self.middle_card.addWidget(card_bottom_box)
        self.middle_section.addWidget(self.middle_card_box)

    def create_events(self, section_width):
        events_height = self.height

        self.events, self.events_box = Gui_Helper.make_layout_full(
            login_layout_box, section_width * 0.9, events_height)
        events_top, events_top_box = Gui_Helper.make_layout_full(
            homepage_card_top, section_width * 0.9, events_height * 0.1)
        events_top.setAlignment(Qt.AlignCenter)

        events_title = QLabel(
            f'Recent Events')
        self.card_title.setStyleSheet(big_text())

        events_top.addWidget(events_title)

        self.events_bottom, events_bottom_box = Gui_Helper.make_layout_full(
            regular, width=section_width * 0.9, height=events_height * 0.9)

        self.events.addWidget(events_top_box)
        self.events.addWidget(events_bottom_box)
        self.bottom_section.addWidget(self.events_box)

    def fill_events(self):
        for event in Global_State.user['actions'][2:]:
            event_box = Event_box(self.section_width * 0.9, 60,
                                  event['date'], event['time'], event['description'],
                                  event['action_type'], event['amount'])
            self.events_bottom.addWidget(event_box.event_layout_box)

    def update_events(self, event=None):
        Gui_Helper.clearLayout(self=Gui_Helper, layout=self.events_bottom)
        self.fill_events()

    def create_Widgets(self):
        # Top part
        self.title = QLabel(f'Account state: {Global_State.user["username"]}')

    def create_layouts(self):
        ##### Create the left side #####
        self.section_width = self.width - self.option_width
        self.left_section, self.left_section_box = Gui_Helper.make_layout_full(
            homepage_background, self.section_width, self.height * 2.1)
        self.left_section_scroll = Gui_Helper.make_layout_scrollable(
            self=self, layout=self.left_section_box, vertical=True)
        self.left_section_scroll.setStyleSheet(chat_main_scroll())
        self.left_section_scroll.resize(0, 0)

        ## Top Part ##
        self.top_section, self.top_section_box = Gui_Helper.make_layout_full(
            regular, self.section_width, self.height * 0.15)
        self.top_section.setAlignment(Qt.AlignCenter)

        ## Middle Part ##
        self.middle_section, self.middle_section_box = Gui_Helper.make_layout_full(
            regular, self.section_width, self.height * 0.6)
        self.middle_section.setAlignment(Qt.AlignCenter)
        self.create_middle_card(self.section_width)

        ## Bottom Part ##
        self.bottom_section, self.bottom_section_box = Gui_Helper.make_layout_full(
            regular, self.section_width, self.height * 1.2)
        self.bottom_section.setAlignment(Qt.AlignCenter)

        self.create_events(self.section_width)

        self.reload_button = Gui_Helper.make_icon(
            self, 'User\\assets\\reload.svg', 30, 30, 'white')
        self.reload_button.move(30, 30)
        self.reload_button.mouseReleaseEvent = self.update_events

        self.left_section.addWidget(self.top_section_box)
        self.left_section.addWidget(self.middle_section_box)
        self.left_section.addWidget(self.bottom_section_box)

        self.top_section.addWidget(self.title)
        self.top_section.addWidget(self.reload_button)

        self.main_page.addWidget(self.left_section_scroll)
        self.main_page.addWidget(self.option_menu.main_layout_box)
