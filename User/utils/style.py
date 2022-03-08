# Main Window
def main_page_box():
    return """
    QGroupBox {
        background-color: blue;
    }"""
# Main Window


# auth
def background():
    return """
        QWidget {
            background: Qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));
        }
    """


def main_page_box():
    return """
        QGroupBox {
            padding: 0;
            margin: 0;
            background-color: aqua;
        }
    """


def login_layout_box():
    return """
    QGroupBox {
        background-color: #fff;
        border: none;
        border-radius: 20px;
    }
    """


def title():
    return """
        QLabel {
            font-size: 25px;
            background-color: transparent;
            font: bold;
            font-family: Verdana, Tahoma, sans-serif;
            letter-spacing: 1.5px;
        }
        """


def login_feild():
    return """
    QGroupBox {
        background-color: #e5e5e5;
    }
    """


def login_submit_button():
    return """
    QPushButton {
        background-color: #1fcc44;
        color: white;
        font-size: 20px;
        border: none;
        border-radius: 20px;
    }
    """


def field_icon():
    return """
    QToolButton {
        background-color: transparent;
        color: #ddd;
    }
    """


def login_field():
    return """
    QLineEdit {
        background-color: transparent;
        color: #141414;
        border: none;
        font-size: 16px;
    }
    """


def bottom_label():
    return """
    QPushButton {
        background-color: transparent;
        border: none;
        outline: none;
    }
    """


def main_icon():
    return """
    QLabel {
         background-color: transparent;

    }
    """


def song_background():
    return """
    QLabel {
         border: 6px solid #1ED760;
         border-radius: 15px;
    }
    QPixmap {
        border-radius: 15px;
    }
    """


def sing_up_left():
    return """
    QGroupBox {
        background-color: #5ff4ee;
    }
    """


def sing_up_field():
    return """
    QGroupBox {
        background-color: transparent;
    }
    """


def singup_avatar():
    return """
    QLabel {
        background-color: transparent;
    }
    """
# auth


# homepage
def homepage_background():
    return """
    QGroupBox {
        background-color:  #446491;
    }
    """


def homepage_title():
    return """
        QLabel {
            font-size: 25px;
            background-color: transparent;
            font: bold;
            font-family: Verdana, Tahoma, sans-serif;
            letter-spacing: 1.5px;}
        """


def homepage_card_top():
    return """
    QGroupBox {
        background-color:  transparent;
        border: 2px solid black;
    }
    """


def regular():
    return """
    QGroupBox {
        background-color:  transparent;
        border: none;
    }
    """


def regular_text():
    return """
    QLabel {
        font-size: 16px;
        background-color: transparent;
        font-family: arial;
    }"""


def big_text():
    return """
    QLabel {
        font-size: 20px;
        font: bold;
        background-color: transparent;
        font-family: arial;
    }"""

# homepage

# option menu


def option_menu_background():
    return """
    QGroupBox {
        background-color: #eee;
        }
        """


def option_bar_text():
    return """
    QLabel {
        font-size: 16px;
        background-color: transparent;
        font-family: arial;
        color: black;
    }"""

# option menu


# scroll bar
def chat_main_scroll():
    return """
    QScrollBar {
        background-color: black;
    }
 QScrollBar:vertical
 {
     background-color: #2A2929;
     width: 20px;
     margin: 15px 3px 15px 3px;
     border: 1px transparent #2A2929;
     border-radius: 7px;
 }

 QScrollBar::handle:vertical
 {
     background-color: #d6afff;
     min-height: 5px;
     border-radius: 7px;
 }

 QScrollBar::sub-line:vertical
 {
     margin: 3px 0px 3px 0px;
     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }

 QScrollBar::add-line:vertical
 {
     margin: 3px 0px 3px 0px;
     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
 {

     border-image: url(:/qss_icons/rc/up_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: top;
     subcontrol-origin: margin;
 }


 QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
 {
     border-image: url(:/qss_icons/rc/down_arrow.png);
     height: 10px;
     width: 10px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
 }

 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
 {
     background: none;
 }


 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
 {
     background: none;
 }
"""
# scroll bar
