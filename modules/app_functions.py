"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""


from main import *


class AppFunctions(MainWindow):
    """Change css of main application if QSS issues.

    Args:
        MainWindow (MainWindow): main window of application.
    """

    def set_theme_hack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #252e42;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 12px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 #32734d, stop:0.5 rgba(183, 93, 105, 0));
        background-color: #242e42;
        """
