from email import message
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from utils.gui_helper import Gui_Helper
from utils.style import *
from utils.Global_state import Global_State
import random
import change_path

from hash import Hash_Function


class Auth(QWidget):
    def __init__(self, width, height, page_system, send_message_to_server):
        super().__init__()
        self.page_system = page_system
        self.send_message_to_server = send_message_to_server
        self.password_hasher = Hash_Function()
        self.setFixedSize(width, height)
        self.setStyleSheet(background())
        self.create_image()

    #################### Dealing With Multiple Pages #####################

    def insert_page(self, widget, index=-1):
        self.page_system.insertWidget(index, widget)

    def go_to_page(self, number):
        self.page_system.setCurrentIndex(number)
    #################### Dealing With Multiple Pages #####################

    #################### Logistic Functions #####################
    def make_singup_avatar(self):
        number = random.randint(1, 6)
        label = QLabel()
        image = QPixmap(f'./User/assets/undraw_{number}.svg')
        image = image.scaled(350, 350, Qt.KeepAspectRatio)
        label.setPixmap(image)
        label.setStyleSheet(singup_avatar())
        return label

    def create_image(self):
        image_width = self.width()
        image_height = self.height() - Global_State.HEIGHT + 75
        guitar_picture = QLabel()
        pixmap = QPixmap('assets\\background-1.jpg')
        pixmap = pixmap.scaled(image_width, image_height)
        guitar_picture.setPixmap(pixmap)
        return guitar_picture

    #################### Logistic Functions #####################
