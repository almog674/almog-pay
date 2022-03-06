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
