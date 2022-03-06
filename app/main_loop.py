import sys
from PyQt5.QtWidgets import QApplication

from .main_window import Main_window
from global_state import Global_State


def scene_generator(scene, go_to_function):
    if Global_State.NEED_TUNING:
        # If not tuned -> quit the application
        sys.exit()
    elif (not Global_State.PLAYER) or (not Global_State.TOKEN):
        # If not player & token -> go to login
        go_to_function(1)
    elif type(scene) == int:
        # If type ia int -> go to the number
        go_to_function(scene)
    else:
        # Generate the number
        number = 0
        if scene == 'home':
            number = 0
        elif scene == 'signup':
            number = 1
        elif scene == 'login':
            number = 2
        elif scene == 'search':
            number = 3
        else:
            print(f'There is no scene "{scene}"')
            return
        go_to_function(number)


def run_app(scene=0):
    App = QApplication(sys.argv)
    main_window = Main_window()
    scene_generator(scene, main_window.go_to_page)
    main_window.show()
    print('Show the app')
    App.exec_()
