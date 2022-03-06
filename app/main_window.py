from PyQt5.QtWidgets import *

from global_state import Global_State
from .gui_helper import Gui_Helper
from .style import main_page_box

from .auth.sign_up import Signup
from .auth.login import Login


class Main_window(QWidget):
    def __init__(self):
        super().__init__()
        self._width = Global_State.WIDTH * Global_State.APP_SIZE_FACTOR
        self._height = Global_State.HEIGHT * Global_State.APP_SIZE_FACTOR
        self.setGeometry(100, 100, self._width,  self._height)
        self.close_link = 'None'
        self.UI()

    def UI(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            style_function=main_page_box, width=self._width, height=self._height, direction=1)

        home_page = QLabel('Home page')
        sign_up_page = Signup(width=self._width, height=self._height)
        login_page = Login(width=self._width, height=self._height)
        self.page_system = QStackedWidget()

        self.page_system.addWidget(home_page)
        self.page_system.addWidget(sign_up_page.main_page_box)
        self.page_system.addWidget(login_page.main_page_box)

        self.main_page.addWidget(self.page_system)
        self.setLayout(self.main_page)
        self.show()

    def go_to_page(self, page_number):
        self.page_system.setCurrentIndex(page_number)
