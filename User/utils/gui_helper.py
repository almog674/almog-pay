from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTimer, QSize, QThread, pyqtSignal, QMargins, QEvent
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QImage, QColor, QLinearGradient
import time


class Gui_Helper(QWidget):
    def make_layout_full(style_function, width=None, height=None, margin=True, direction=0):
        if direction == 0:
            layout = QVBoxLayout()
        elif direction == 1:
            layout = QHBoxLayout()
        elif direction == 2:
            layout = QFormLayout()
        elif direction == 3:
            layout = QGridLayout()
        box = QGroupBox()
        box.setFlat(True)
        if width:
            box.setFixedWidth(width)
        if height:
            box.setFixedHeight(height)
        if margin:
            layout.setContentsMargins(QMargins(0, 0, 0, 0))
            layout.setSpacing(0)
        box.setStyleSheet(style_function())
        box.setLayout(layout)
        return (layout, box)

    def make_picture(self, url, width, height):
        label = QLabel()
        pixmap = QPixmap(url)
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        return label, pixmap

    def clearLayout(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if isinstance(item, QWidgetItem):
                item.widget().close()
            else:
                self.clearLayout(item.layout())

            # remove the item from layout
            layout.removeItem(item)

    def make_icon(self, url, width, height, color='Black'):
        icon_container = QLabel()
        icon_container.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap(url)
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio)
        icon_container.setPixmap(pixmap)
        mask = pixmap.createMaskFromColor(QColor(color), Qt.MaskOutColor)
        pixmap.fill(QColor(color))
        pixmap.setMask(mask)
        return icon_container

    def add_shadow(self, widget, x, y, blur):
        shadow = QGraphicsDropShadowEffect()
        shadow.setYOffset(y)
        shadow.setXOffset(x)
        shadow.setBlurRadius(blur)
        widget.setGraphicsEffect(shadow)
        return widget

    def make_message_box(text, message_type='message'):
        msg = QMessageBox()
        if message_type == 'message':
            message_type = QMessageBox.Information
        else:
            message_type = QMessageBox.Critical
        msg.setIcon(message_type)
        msg.setText(text)
        msg.setFixedSize(200, 200)
        msg.exec_()

    def make_layout_scrollable(self, layout, vertical=False, horizontal=False, height=False, frameStyle=0):
        scroll = QScrollArea()
        if not vertical:
            scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        if not horizontal:
            scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        if height:
            scroll.setFixedHeight(height)
        scroll.setWidgetResizable(True)
        scroll.setContentsMargins(0, 0, 0, 0)
        scroll.setFrameStyle(frameStyle)
        scroll.setWidget(layout)
        return scroll
