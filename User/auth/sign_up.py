from .auth import Auth

from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QLineEdit, QToolButton
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap
from utils.gui_helper import Gui_Helper
from utils.style import *
from utils.Global_state import Global_State
import random


class Signup(Auth):
    def __init__(self, width, height, page_system, send_message_to_server):
        super().__init__(width=width, height=height, page_system=page_system,
                         send_message_to_server=send_message_to_server)
        self.UI()

    #################### Sing Up Page #####################
    def UI(self):
        self.main_page, self.main_page_box = Gui_Helper.make_layout_full(
            background, self.width(), self.height())

        self.sing_up_Widgets()
        self.sing_up_layouts()

    def signup_to_server(self):
        username = self.singup_username_line_edit.text()
        email = self.singup_email_line_edit.text()
        password = self.singup_password_line_edit.text()
        credentials = {'username': username,
                       'email': email,
                       'password': self.password_hasher.hash_password(username, password)}

        # Validate the password
        error, message = self.validate_password(username, password)
        if error:
            return Gui_Helper.make_message_box(message, 'critical')
        self.send_message_to_server('12', 'guest', credentials)

    def validate_password(self, username, password):
        if len(password) > 32:
            return True, "password is too long"
        if len(password) < 8:
            return True, "Please provide a password with at least 8 characters"
        if username == password:
            return True, "The username and the password cannot be identical"
        return False, None

    def make_singup_mini_profile(self):
        profile = QLabel('Profile')
        profile.setPixmap(QPixmap('./User/assets/headphone_image.png'))
        profile.setAlignment(Qt.AlignHCenter)
        profile.setFixedSize(100, 100)
        return profile

    def clear_signup_fields(self):
        self.singup_username_line_edit.setText('')
        self.singup_email_line_edit.setText('')
        self.singup_password_line_edit.setText('')
        self.singup_prepasswprd_line_edit .setText('')

    def sing_up_Widgets(self):
        ### Right Side Widget ###
        self.sing_up_title = QLabel('Create New User')
        self.sing_up_title.setAlignment(Qt.AlignHCenter)
        self.sing_up_title.setStyleSheet(title())

        self.sing_up_username_field = QHBoxLayout()
        self.sing_up_username_field_box = QGroupBox()
        self.sing_up_username_field_box.setStyleSheet(login_feild())
        self.sing_up_username_field_box.setFixedSize(300, 40)
        self.sing_up_username_field_box.setLayout(self.sing_up_username_field)

        self.sing_up_email_field = QHBoxLayout()
        self.sing_up_email_field_box = QGroupBox()
        self.sing_up_email_field_box.setStyleSheet(login_feild())
        self.sing_up_email_field_box.setFixedSize(300, 40)
        self.sing_up_email_field_box.setLayout(self.sing_up_email_field)

        self.sing_up_password_field = QHBoxLayout()
        self.sing_up_password_field_box = QGroupBox()
        self.sing_up_password_field_box.setStyleSheet(login_feild())
        self.sing_up_password_field_box.setFixedSize(300, 40)
        self.sing_up_password_field_box.setLayout(self.sing_up_password_field)

        self.sing_up_pre_password_field = QHBoxLayout()
        self.sing_up_pre_password_field_box = QGroupBox()
        self.sing_up_pre_password_field_box.setStyleSheet(login_feild())
        self.sing_up_pre_password_field_box.setFixedSize(300, 40)
        self.sing_up_pre_password_field_box.setLayout(
            self.sing_up_pre_password_field)

        self.sing_up_authentication = QPushButton('Sing Up')
        self.sing_up_authentication.setCursor(Qt.PointingHandCursor)
        self.sing_up_authentication.setFixedSize(300, 40)
        self.sing_up_authentication.clicked.connect(self.signup_to_server)
        self.sing_up_authentication.setStyleSheet(login_submit_button())

        self.sing_up_return_button = QPushButton(
            'Already have a user? go to login')
        self.sing_up_return_button.setCursor(Qt.PointingHandCursor)
        self.sing_up_return_button.setStyleSheet(bottom_label())
        self.sing_up_return_button.clicked.connect(lambda: self.go_to_page(1))
        self.sing_up_return_button.clicked.connect(self.clear_signup_fields)

        ### Sing Up Fields Widgets ###
        self.singup_username_line_edit = QLineEdit()
        self.singup_username_line_edit.setPlaceholderText('Username')
        self.singup_username_line_edit.setStyleSheet(login_field())
        self.singup_username_icon = QToolButton()
        self.singup_username_icon.setStyleSheet(field_icon())
        self.singup_username_icon.setDisabled(True)
        self.singup_username_icon.setIcon(
            QIcon('./User/assets/user-solid.svg'))

        self.singup_email_line_edit = QLineEdit()
        self.singup_email_line_edit.setPlaceholderText('Email')
        self.singup_email_line_edit.setStyleSheet(login_field())
        self.singup_email_icon = QToolButton()
        self.singup_email_icon.setStyleSheet(field_icon())
        self.singup_email_icon.setDisabled(True)
        self.singup_email_icon.setIcon(QIcon('./User/assets/email-icon.svg'))

        self.singup_password_line_edit = QLineEdit()
        self.singup_password_line_edit.setPlaceholderText('password')
        self.singup_password_line_edit.setEchoMode(QLineEdit.Password)
        self.singup_password_line_edit.setStyleSheet(login_field())
        self.singup_password_icon = QToolButton()
        self.singup_password_icon.setStyleSheet(field_icon())
        self.singup_password_icon.setDisabled(True)
        self.singup_password_icon.setIcon(
            QIcon('./User/assets/lock-solid.svg'))

        self.singup_prepasswprd_line_edit = QLineEdit()
        self.singup_prepasswprd_line_edit.setPlaceholderText(
            'Validate Password')
        self.singup_prepasswprd_line_edit.setStyleSheet(login_field())
        self.singup_prepasswprd_line_edit.setEchoMode(QLineEdit.Password)
        self.singup_prepasswprd_icon = QToolButton()
        self.singup_prepasswprd_icon.setStyleSheet(field_icon())
        self.singup_prepasswprd_icon.setDisabled(True)
        self.singup_prepasswprd_icon.setIcon(
            QIcon('./User/assets/lock-solid.svg'))

        ### Left Side Widgets ###
        self.singup_avatar = self.make_singup_avatar()

    def sing_up_layouts(self):
        ##### Sing Up Layouts #####
        self.singup_layout = QHBoxLayout()
        self.main_page.setAlignment(Qt.AlignCenter)

        self.singup_layout_box = QGroupBox()
        self.singup_layout_box.setStyleSheet(login_layout_box())
        self.singup_layout_box.setFixedSize(650, 450)
        self.singup_layout_box.setLayout(self.singup_layout)

        self.sing_up_left = QVBoxLayout()
        self.sing_up_right = QVBoxLayout()

        ### Create The Right Part ###
        self.sing_up_title_section = QVBoxLayout()
        self.sing_up_form_section = QVBoxLayout()
        self.sing_up_bottom_section = QVBoxLayout()

        ### Create The Left Part ###
        self.sing_up_left.addWidget(self.singup_avatar)

        ### Create The Fields ###

        ### Adding the nested Layouts ###
        self.main_page.addWidget(self.singup_layout_box)

        self.singup_layout.addLayout(self.sing_up_left, 50)
        self.singup_layout.addLayout(self.sing_up_right, 50)

        self.sing_up_right.addLayout(self.sing_up_title_section, 20)
        self.sing_up_right.addLayout(self.sing_up_form_section, 60)
        self.sing_up_right.addLayout(self.sing_up_bottom_section, 20)

        # Right Part #
        self.sing_up_title_section.addStretch()
        self.sing_up_title_section.addWidget(self.sing_up_title)
        self.sing_up_title_section.addStretch()

        self.sing_up_form_section.addStretch()
        self.sing_up_form_section.addWidget(self.sing_up_username_field_box)
        self.sing_up_form_section.addStretch()
        self.sing_up_form_section.addWidget(self.sing_up_email_field_box)
        self.sing_up_form_section.addStretch()
        self.sing_up_form_section.addWidget(self.sing_up_password_field_box)
        self.sing_up_form_section.addStretch()
        self.sing_up_form_section.addWidget(
            self.sing_up_pre_password_field_box)
        self.sing_up_form_section.addStretch()
        self.sing_up_form_section.addWidget(self.sing_up_authentication)
        self.sing_up_right.addStretch()

        self.sing_up_bottom_section.addStretch()
        self.sing_up_bottom_section.addWidget(self.sing_up_return_button)
        self.sing_up_bottom_section.addStretch()

        self.sing_up_username_field.addWidget(self.singup_username_icon)
        self.sing_up_username_field.addWidget(self.singup_username_line_edit)

        self.sing_up_email_field.addWidget(self.singup_email_icon)
        self.sing_up_email_field.addWidget(self.singup_email_line_edit)

        self.sing_up_password_field.addWidget(self.singup_password_icon)
        self.sing_up_password_field.addWidget(self.singup_password_line_edit)

        self.sing_up_pre_password_field.addWidget(self.singup_prepasswprd_icon)
        self.sing_up_pre_password_field.addWidget(
            self.singup_prepasswprd_line_edit)

        self.main_page.addWidget(self.singup_layout_box)
