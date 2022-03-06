from .auth import Auth
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QLineEdit, QToolButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from utils.gui_helper import Gui_Helper
from utils.style import *
from utils.Global_state import Global_State


class Login(Auth):
    def __init__(self, width, height, page_system, send_message_to_server):
        super().__init__(width=width, height=height, page_system=page_system,
                         send_message_to_server=send_message_to_server)
        self.UI()

    def clear_login_fields(self):
        # Clear the fields of the singup and login #
        self.user_field.setText('')
        self.password_field.setText('')

    def login_to_server(self):
        credentials = {'username': self.user_field.text(),
                       'password': self.password_field.text()}
        self.send_message_to_server('11', 'guest', credentials)

    def UI(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            background, self.width(), self.height())

        self.login_Widgets()
        self.login_layouts()

    def login_layouts(self):
        ##### Create The Layouts #####
        self.main_page.setAlignment(Qt.AlignCenter)

        ### Login Layouts ###
        self.login_layout = QHBoxLayout()

        self.login_layout_box = QGroupBox()
        self.login_layout_box.setStyleSheet(login_layout_box())
        self.login_layout_box.setFixedSize(650, 450)
        self.login_layout_box.setLayout(self.login_layout)

        self.login_right_layout = QVBoxLayout()
        self.login_left_layout = QVBoxLayout()

        ### Create the right part ###
        self.title_section = QHBoxLayout()
        self.form_section = QVBoxLayout()
        self.bottom_section = QVBoxLayout()

        ### Create The Form ###
        self.username_layout = QHBoxLayout()
        self.username_layout.addWidget(self.user_icon)
        self.username_layout.addWidget(self.user_field)
        self.username_layout_box = QGroupBox()
        self.username_layout_box.setLayout(self.username_layout)
        self.username_layout_box.setAlignment(Qt.AlignHCenter)
        self.username_layout_box.setFixedSize(300, 40)
        self.username_layout_box.setStyleSheet(login_feild())

        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_icon)
        self.password_layout.addWidget(self.password_field)
        self.password_layout_box = QGroupBox()
        self.password_layout_box.setLayout(self.password_layout)
        self.password_layout_box.setAlignment(Qt.AlignHCenter)
        self.password_layout_box.setFixedSize(300, 40)
        self.password_layout_box.setStyleSheet(login_feild())

        ### Create the right part ###
        self.login_right_layout.addWidget(self.logo)

        ### Adding the nesting layouts ###
        # self.main_page.addWidget(self.login_layout_box)

        self.login_layout.addLayout(self.login_right_layout, 50)
        self.login_layout.addLayout(self.login_left_layout, 50)

        self.login_left_layout.addLayout(self.title_section, 20)
        self.login_left_layout.addLayout(self.form_section, 55)
        self.login_left_layout.addLayout(self.bottom_section, 25)

        self.form_section.addStretch()
        self.title_section.addWidget(self.title)
        self.form_section.addWidget(self.username_layout_box)
        self.form_section.addStretch()
        self.form_section.addWidget(self.password_layout_box)
        self.form_section.addStretch()
        self.form_section.addWidget(self.login_submit_button)
        self.form_section.addStretch()

        # self.bottom_section.addStretch()
        self.bottom_section.addWidget(self.forgot_password_label)
        self.bottom_section.addStretch()
        self.bottom_section.addWidget(self.create_user_label)
        self.bottom_section.addStretch()

        self.main_page.addWidget(self.login_layout_box)

    def login_Widgets(self):
        ##### Making the widgets for the app #####
        # self.main_page = QHBoxLayout()
        # self.main_page_box = QGroupBox('main page box')
        # self.main_page_box.setObjectName('main_page_box')
        # self.main_page_box.setStyleSheet(main_page_box())
        # self.main_page_box.setLayout(self.main_page)

        ### Title Section ###
        self.title = QLabel('Member Login')
        self.title.setStyleSheet(title())
        self.title.setAlignment(Qt.AlignCenter)

        ### Login Button ###
        self.login_submit_button = QPushButton('Login')
        self.login_submit_button.setFixedSize(300, 40)
        self.login_submit_button.setCursor(Qt.PointingHandCursor)
        self.login_submit_button.setStyleSheet(login_submit_button())
        self.login_submit_button.clicked.connect(self.login_to_server)

        ### Field Widgets ###
        self.user_icon = QToolButton()
        self.user_icon.setDisabled(True)
        self.user_icon.setStyleSheet(field_icon())
        self.user_icon.setIcon(QIcon("./User/assets/user-solid.svg"))
        self.user_field = QLineEdit()
        self.user_field.setFrame(False)
        self.user_field.setPlaceholderText('Username')
        self.user_field.setStyleSheet(login_field())

        self.password_icon = QToolButton()
        self.password_icon.setDisabled(True)
        self.password_icon.setStyleSheet(field_icon())
        self.password_icon.setIcon(QIcon("./User/assets/lock-solid.svg"))
        self.password_field = QLineEdit()
        self.password_field.setFrame(False)
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setPlaceholderText('Password')
        self.password_field.setStyleSheet(login_field())

        ### Bottom Widgets ###
        self.forgot_password_label = QPushButton('Forgot Password ?')
        self.forgot_password_label.setStyleSheet(bottom_label())
        self.forgot_password_label.setCursor(Qt.PointingHandCursor)

        self.create_user_label = QPushButton('Create new account =>')
        self.create_user_label.setStyleSheet(bottom_label())
        self.create_user_label.setCursor(Qt.PointingHandCursor)
        self.create_user_label.clicked.connect(lambda: self.go_to_page(0))
        self.create_user_label.clicked.connect(self.clear_login_fields)
        # self.create_user_label.mouseReleaseEvent = self.go_to_singup

        ### Left Part ###
        self.logo = self.make_singup_avatar()
