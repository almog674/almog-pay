from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMargins

from utils.gui_helper import Gui_Helper
from utils.style import option_bar_text, regular


class Option(QWidget):
    def __init__(self, name, icon, function, width):
        super().__init__()
        self.name = name
        self.icon = icon
        self.function = function
        self.width = width
        self.UI()

    def UI(self):
        self.opacity_effect_full = QGraphicsOpacityEffect()
        self.opacity_effect_full.setOpacity(1)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)

        self.setStyleSheet('''
            background-color: transparent;
        ''')
        self.installEventFilter(self)
        self.setFixedHeight(60)
        self.setFixedWidth(self.width)
        self.setCursor(Qt.PointingHandCursor)

        self.main_layout, self.main_layout_box = Gui_Helper.make_layout_full(
            regular, self.width, self.height(), direction=1)
        self.main_layout.setContentsMargins(QMargins(0, 0, 0, 0))
        self.main_layout.setSpacing(0)

        self.text = QLabel(self.name)
        self.text.setStyleSheet(option_bar_text())
        self.text.setFixedWidth(self.width - 50)
        self.icon = Gui_Helper.make_icon(
            self=self, url=self.icon, width=35, height=35, color='white')
        self.icon.setFixedHeight(self.height())
        self.icon.setFixedHeight(50)
        self.icon.setAlignment(Qt.AlignCenter)

        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.main_layout.addStretch(2)
        self.main_layout.addWidget(self.icon)
        self.main_layout.addStretch(1)

        self.setLayout(self.main_layout)
        self.mouseReleaseEvent = self.function
        self.show()

    def eventFilter(self, obj, event):
        if obj == self and event.type() == 10:
            self.onHovered()
        elif obj == self and event.type() == 11:
            self.offHovered()
        return super().eventFilter(obj, event)
        # return super(Widget, self).eventFilter(obj, event)

    def onHovered(self):
        self.text.setStyleSheet(
            '''color: white; font-size: 18px; background-color: rgb(255, 0, 142);''')
        # self.setGraphicsEffect(self.opacity_effect)
        self.main_layout_box.setStyleSheet('''
            background-color: rgb(255, 0, 142);
        ''')

    def offHovered(self):
        self.text.setStyleSheet(option_bar_text())
        # self.setGraphicsEffect(self.opacity_effect_full)
        self.main_layout_box.setStyleSheet(regular())
