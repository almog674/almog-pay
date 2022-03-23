import sys
import time
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from utils.Global_state import Global_State
from utils.gui_helper import Gui_Helper
from utils.style import main_page_box
from utils.gui_thread import Gui_Thread

from auth.login import Login
from auth.sign_up import Signup
from pages.home_page import Home_Page
from pages.despoit_page import Despoit_page
from pages.transfer_page import Transfer_Page

from components.option_menu import Option_Menu

from basic_client import Client


class Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.user = Client()
        self.messages_thread = threading.Thread(target=self.check_new_messages)
        self.messages_thread.start()
        self.message_info = ['New message', 'information']

        # Initialize gui thread
        self.gui_thread = Gui_Thread()
        self.gui_thread.make_message_box.connect(lambda: Gui_Helper.make_message_box(
            self.message_info[0], self.message_info[1]))
        self.UI()

    def check_new_messages(self):
        while True:
            if len(self.user.new_messages) > 0:
                message = self.user.new_messages[0]
                if "[SERVER_ENCRYPT]" in message:
                    plain_message = self.user.decrypt_message(message)
                    message_sender, message_text, message_type, message_date, message_time = plain_message.split(
                        "/")
                else:
                    message_sender, message_text, message_type, message_date, message_time = message.split(
                        "/")

                # message_text = self.user.check_dictionary(message_text)
                if message_type == 'ERROR':
                    self.message_info[1] = 'critical'
                    self.message_info[0] = f'{message_sender}: {message_text}'
                    self.gui_thread.make_message_box_func()
                elif 'LOGIN' in message_type:
                    Global_State.user = eval(message_text)
                    self.go_to_home_page()
                elif 'USER' in message_type:
                    Global_State.user = eval(message_text)
                elif 'SUCCESS' in message_type:
                    self.message_info[1] = 'message'
                    self.message_info[0] = f'{message_sender}: {message_text}'
                    self.gui_thread.make_message_box_func()
                    if Global_State.user['username'] != 'guest':
                        self.home_page.update_page()
                elif message_type == 'user_info':
                    Global_State.user = message

                elif message_type == '[KEYS]':
                    message_text = eval(message_text)
                    self.user.get_keys(message_text)

                self.user.new_messages.remove(message)
            else:
                time.sleep(0.25)

    def UI(self):
        # initialize main widgets
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            style_function=main_page_box, width=Global_State.WIDTH, height=Global_State.HEIGHT, direction=1)
        self.page_system = QStackedWidget()

        option_menu_one = Option_Menu(
            200, Global_State.HEIGHT, (self.go_to_home_page, self.go_to_page, self.logout, Home_Page.update_events))

        # Initialize the pages
        sign_up_page = Signup(Global_State.WIDTH,
                              Global_State.HEIGHT, self.page_system, self.user.send_message_to_server)
        login_page = Login(Global_State.WIDTH,
                           Global_State.HEIGHT, self.page_system, self.user.send_message_to_server)
        self.home_page = Home_Page(Global_State.WIDTH,
                                   Global_State.HEIGHT, option_menu_one)
        self.despoit_page = Despoit_page(
            300, 250, self.user.send_message_to_server, self.go_to_home_page, type='despoit')
        self.extract_page = Despoit_page(
            300, 250, self.user.send_message_to_server, self.go_to_home_page, type='extract')
        self.transfer_page = Transfer_Page(
            300, 400, self.user.send_message_to_server, self.go_to_home_page)

        # Add the pages to the page system
        self.page_system.addWidget(sign_up_page.main_page_box)
        self.page_system.addWidget(login_page.main_page_box)
        self.page_system.addWidget(self.home_page.main_page_box)
        # self.page_system.addWidget(self.despoit_page.main_page_box)

        self.main_page.addWidget(self.page_system)

        # show the app
        self.setLayout(self.main_page)
        self.show()

    def go_to_page(self, number):
        if number == 3:
            self.despoit_page.show()
        if number == 4:
            self.extract_page.show()
        if number == 5:
            self.transfer_page.show()
        self.page_system.setCurrentIndex(number)

    def go_to_home_page(self):
        self.home_page.update_page()
        self.go_to_page(2)

    def logout(self):
        self.go_to_page(0)
        self.home_page.clear_events()
        Global_State.user = {'username': 'guest', 'email': "guest@gmail.com",
                             'account_balance': '123', 'all_time_high': '1',
                             'all_time_low': '1', 'frame': '1',
                             'actions': []}


def main():
    App = QApplication(sys.argv)
    main_window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
