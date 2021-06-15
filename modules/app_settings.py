"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""


class Settings:
    ENABLE_CUSTOM_TITLE_BAR = True
    MENU_WIDTH = 240
    LEFT_BOX_WIDTH = 240
    RIGHT_BOX_WIDTH = 240
    TIME_ANIMATION = 500

    # BTNS LEFT AND RIGHT BOX COLORS
    BTN_LEFT_BOX_COLOR = "background-color: rgb(44, 49, 58);"
    BTN_RIGHT_BOX_COLOR = "background-color: rgb(44, 49, 58);"

    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(44, 49, 58), stop:0.5 rgba(44, 49, 58));
    background-color: rgb(44, 49, 58);
    """
