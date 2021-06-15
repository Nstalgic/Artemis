# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainiLsvOE.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph import PlotWidget

from .resources_rc import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1309, 950)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(
            u"QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            '	font: 10pt "Segoe UI";\n'
            "}\n"
            "\n"
            "TreeView{\n"
            "    borderwidth: 0;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Tooltip */\n"
            "QToolTip {\n"
            "	color: #ffffff;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(255, 121, 198);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Bg App */\n"
            "#bgApp {	\n"
            "	background-color: rgb(72,115,165);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Left Menu */\n"
            "#leftMenuBg {	\n"
            "	background-color: rgb(33, 37, 43)"
            ";\n"
            "}\n"
            "#topLogo {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	\n"
            "	background-position: centered;\n"
            "	background-repeat: no-repeat;\n"
            "}\n"
            '#titleLeftApp { font: 63 12pt "Segoe UI Semibold"; }\n'
            '#titleLeftDescription { font: 8pt "Segoe UI"; color: rgb(189, 147, 249); }\n'
            "\n"
            "/* MENUS */\n"
            "#topMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 12px solid transparent;\n"
            "	background-color: transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#topMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#topMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton {	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 9px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#bot"
            "tomMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#bottomMenu .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "\n"
            "/* Toggle Button */\n"
            "#toggleButton {\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 20px solid transparent;\n"
            "	background-color: rgb(37, 41, 48);\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "	color: rgb(113, 126, 149);\n"
            "}\n"
            "#toggleButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#toggleButton:pressed {\n"
            "	background-color: rgb(189, 147, 249);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "\n"
            "\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Extra Tab */\n"
            "#extraLeftBox {	\n"
            "	background-color: rgb(44, 49, 58);\n"
            "}\n"
            "#extraTopBg{	\n"
            "	background-color: rgb(189, 147, 249)\n"
            "}\n"
            "\n"
            "/* Icon */\n"
            "#extraIcon {\n"
            "	background-position: cen"
            "ter;\n"
            "	background-repeat: no-repeat;\n"
            "	background-image: url(:/icons/images/icons/icon_settings.png);\n"
            "}\n"
            "\n"
            "/* Label */\n"
            "#extraLabel { color: rgb(255, 255, 255); }\n"
            "\n"
            "/* Btn Close */\n"
            "#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  }\n"
            "#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; }\n"
            "#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid;  }\n"
            "\n"
            "/* Extra Content */\n"
            "#extraContent{\n"
            "	border-top: 3px solid rgb(40, 44, 52);\n"
            "}\n"
            "\n"
            "/* Extra Top Menus */\n"
            "#extraTopMenu .QPushButton {\n"
            "background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 22px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#extraTopMenu .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#extraTopMenu .QPushButton:pressed {	\n"
            "	background-color: rgb"
            "(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Content App */\n"
            "#contentTopBg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "\n"
            "/* Top Buttons */\n"
            "#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;   }\n"
            "#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid;  }\n"
            "#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; }\n"
            "\n"
            "/* Theme Settings */\n"
            "#extraRightBox { background-color: rgb(44, 49, 58); }\n"
            "#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottomBar { background-color: rgb(44, 49, 58); }\n"
            "#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* CONTENT SETTINGS */\n"
            "/* MENUS */\n"
            "#contentSettings .QPushButton {"
            "	\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 12px solid transparent;\n"
            "	background-color:transparent;\n"
            "	text-align: left;\n"
            "	padding-left: 44px;\n"
            "}\n"
            "#contentSettings .QPushButton:hover {\n"
            "	background-color: rgb(40, 44, 52);\n"
            "}\n"
            "#contentSettings .QPushButton:pressed {	\n"
            "	background-color: rgb(189, 147, 249);\n"
            "	color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "QTableWidget */\n"
            "QTableWidget {	\n"
            "	background-color: transparent;\n"
            "	padding: 10px;\n"
            "	border-radius: 5px;\n"
            "	gridline-color: rgb(44, 49, 58);\n"
            "	border-bottom: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item{\n"
            "	border-color: rgb(44, 49, 60);\n"
            "	padding-left: 5px;\n"
            "	padding-right: 5px;\n"
            "	gridline-color: rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::item:selected{\n"
            "	background-color: rgb(189, 147, 249);\n"
            "}\n"
            "QHeaderView::section{"
            "\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	max-width: 30px;\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	border-style: none;\n"
            "    border-bottom: 1px solid rgb(44, 49, 60);\n"
            "    border-right: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "QTableWidget::horizontalHeader {	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    border: 1px solid rgb(33, 37, 43);\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 3px;\n"
            "	border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 1px solid rgb(44, 49, 60);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            ""
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radiu"
            "s: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px"
            " 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* ////////////////////////////////////////////////////////////////////////////////////"
            "/////////////\n"
            "CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "RadioButton */\n"
            "QRadioButton::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "}\n"
            "QRadioButton::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "    background: 3px solid rgb(94, 106, 130);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "}\n"
            "\n"
            "/* /"
            "////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "ComboBox */\n"
            "QComboBox{\n"
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding: 5px;\n"
            "	padding-left: 10px;\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subcontrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "QComboBox QAbstractItemView {\n"
            "	color: rgb(255, 121, 198);	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	padding: 10px;\n"
            "	selection-background-color: rgb(39, 44, 54);\n"
            "}\n"
            "\n"
            "/* ///////////////////////////////////"
            "//////////////////////////////////////////////////////////////\n"
            "Sliders */\n"
            "QSlider::groove:horizontal {\n"
            "    border-radius: 5px;\n"
            "    height: 10px;\n"
            "	margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:horizontal:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "    border: none;\n"
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:horizontal:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:horizontal:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "QSlider::groove:vertical {\n"
            "    border-radius: 5px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QSlider::groove:vertical:hover {\n"
            "	background-color: rgb(55, 62, 76);\n"
            "}\n"
            "QSlider::handle:vertical {\n"
            "    background-color: rgb(189, 147, 249);\n"
            "	border: none;\n"
            ""
            "    height: 10px;\n"
            "    width: 10px;\n"
            "    margin: 0px;\n"
            "	border-radius: 5px;\n"
            "}\n"
            "QSlider::handle:vertical:hover {\n"
            "    background-color: rgb(195, 155, 255);\n"
            "}\n"
            "QSlider::handle:vertical:pressed {\n"
            "    background-color: rgb(255, 121, 198);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "CommandLinkButton */\n"
            "QCommandLinkButton {	\n"
            "	color: rgb(255, 121, 198);\n"
            "	border-radius: 5px;\n"
            "	padding: 5px;\n"
            "	color: rgb(255, 170, 255);\n"
            "}\n"
            "QCommandLinkButton:hover {	\n"
            "	color: rgb(255, 170, 255);\n"
            "	background-color: rgb(44, 49, 60);\n"
            "}\n"
            "QCommandLinkButton:pressed {	\n"
            "	color: rgb(189, 147, 249);\n"
            "	background-color: rgb(52, 58, 71);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Button */\n"
            "#pagesContainer QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59"
            ", 72);\n"
            "}\n"
            "#pagesContainer QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pagesContainer QPushButton:pressed {	\n"
            "	background-color: rgb(72, 115, 165);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}\n"
            "\n"
            ""
        )
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(0, 0, 1306, 947))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgApp.sizePolicy().hasHeightForWidth())
        self.bgApp.setSizePolicy(sizePolicy)
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(40, 0))
        self.leftMenuBg.setMaximumSize(QSize(40, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.topMenu)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u'font: 10pt "Montserrat";\n' "font-weight: bold;")
        self.label_15.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_15)

        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-home.png);"
        )

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_history = QPushButton(self.topMenu)
        self.btn_history.setObjectName(u"btn_history")
        sizePolicy1.setHeightForWidth(self.btn_history.sizePolicy().hasHeightForWidth())
        self.btn_history.setSizePolicy(sizePolicy1)
        self.btn_history.setMinimumSize(QSize(0, 45))
        self.btn_history.setFont(font)
        self.btn_history.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_history.setLayoutDirection(Qt.LeftToRight)
        self.btn_history.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-history.png);"
        )

        self.verticalLayout_8.addWidget(self.btn_history)

        self.btn_performance = QPushButton(self.topMenu)
        self.btn_performance.setObjectName(u"btn_performance")
        sizePolicy1.setHeightForWidth(
            self.btn_performance.sizePolicy().hasHeightForWidth()
        )
        self.btn_performance.setSizePolicy(sizePolicy1)
        self.btn_performance.setMinimumSize(QSize(0, 45))
        self.btn_performance.setFont(font)
        self.btn_performance.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_performance.setLayoutDirection(Qt.LeftToRight)
        self.btn_performance.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-chart-line.png);"
        )

        self.verticalLayout_8.addWidget(self.btn_performance)

        self.btn_guide = QPushButton(self.topMenu)
        self.btn_guide.setObjectName(u"btn_guide")
        self.btn_guide.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_guide.sizePolicy().hasHeightForWidth())
        self.btn_guide.setSizePolicy(sizePolicy1)
        self.btn_guide.setMinimumSize(QSize(0, 45))
        self.btn_guide.setFont(font)
        self.btn_guide.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_guide.setLayoutDirection(Qt.LeftToRight)
        self.btn_guide.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-notes.png);"
        )

        self.verticalLayout_8.addWidget(self.btn_guide)

        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.bottomMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.btn_settings.sizePolicy().hasHeightForWidth()
        )
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(
            u"background-image: url(:/icons/images/icons/icon_settings.png);"
        )

        self.verticalLayout_9.addWidget(self.btn_settings)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setStyleSheet(u"")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        sizePolicy.setHeightForWidth(self.contentTopBg.sizePolicy().hasHeightForWidth())
        self.contentTopBg.setSizePolicy(sizePolicy)
        self.contentTopBg.setMinimumSize(QSize(0, 28))
        self.contentTopBg.setMaximumSize(QSize(16777202, 28))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy.setHeightForWidth(
            self.titleRightInfo.sizePolicy().hasHeightForWidth()
        )
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet(u'font: 10pt "Roboto Mono";\n' "")
        self.titleRightInfo.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.titleRightInfo.setIndent(0)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(
            u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setEnabled(True)
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(
            u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(
            u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setStyleSheet(u"")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u'background-color: "#242e42";')
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"QFrame {\n" 'background-color:"#2f3b52";\n' "}")
        self.bench_frame_bars = QFrame(self.home)
        self.bench_frame_bars.setObjectName(u"bench_frame_bars")
        self.bench_frame_bars.setGeometry(QRect(50, 460, 561, 381))
        self.bench_frame_bars.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_bars.setFrameShape(QFrame.NoFrame)
        self.bench_frame_bars.setFrameShadow(QFrame.Raised)
        self.benchBar_15 = QProgressBar(self.bench_frame_bars)
        self.benchBar_15.setObjectName(u"benchBar_15")
        self.benchBar_15.setGeometry(QRect(40, 316, 475, 16))
        self.benchBar_15.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_15.setValue(100)
        self.benchBar_15.setAlignment(Qt.AlignCenter)
        self.benchBar_5 = QProgressBar(self.bench_frame_bars)
        self.benchBar_5.setObjectName(u"benchBar_5")
        self.benchBar_5.setGeometry(QRect(40, 148, 475, 16))
        self.benchBar_5.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_5.setValue(100)
        self.benchBar_5.setAlignment(Qt.AlignCenter)
        self.benchBar_6 = QProgressBar(self.bench_frame_bars)
        self.benchBar_6.setObjectName(u"benchBar_6")
        self.benchBar_6.setGeometry(QRect(40, 168, 475, 16))
        self.benchBar_6.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_6.setValue(100)
        self.benchBar_6.setAlignment(Qt.AlignCenter)
        self.progressBar_54 = QProgressBar(self.bench_frame_bars)
        self.progressBar_54.setObjectName(u"progressBar_54")
        self.progressBar_54.setGeometry(QRect(530, 70, 8, 41))
        self.progressBar_54.setStyleSheet(
            u"QProgressBar::chunk {background-color:#f1c232;}"
        )
        self.progressBar_54.setValue(100)
        self.progressBar_54.setAlignment(Qt.AlignCenter)
        self.progressBar_54.setTextVisible(False)
        self.progressBar_54.setOrientation(Qt.Vertical)
        self.progressBar_51 = QProgressBar(self.bench_frame_bars)
        self.progressBar_51.setObjectName(u"progressBar_51")
        self.progressBar_51.setGeometry(QRect(530, 120, 8, 41))
        self.progressBar_51.setStyleSheet(
            u"QProgressBar::chunk {background-color:#e06666;}"
        )
        self.progressBar_51.setValue(100)
        self.progressBar_51.setAlignment(Qt.AlignCenter)
        self.progressBar_51.setTextVisible(False)
        self.progressBar_51.setOrientation(Qt.Vertical)
        self.progressBar_51.setInvertedAppearance(False)
        self.progressBar_39 = QProgressBar(self.bench_frame_bars)
        self.progressBar_39.setObjectName(u"progressBar_39")
        self.progressBar_39.setGeometry(QRect(530, 320, 8, 41))
        self.progressBar_39.setStyleSheet(
            u"QProgressBar::chunk {background-color: #674ea7;}"
        )
        self.progressBar_39.setValue(100)
        self.progressBar_39.setAlignment(Qt.AlignCenter)
        self.progressBar_39.setTextVisible(False)
        self.progressBar_39.setOrientation(Qt.Vertical)
        self.progressBar_39.setInvertedAppearance(False)
        self.progressBar_31 = QProgressBar(self.bench_frame_bars)
        self.progressBar_31.setObjectName(u"progressBar_31")
        self.progressBar_31.setGeometry(QRect(520, 220, 8, 41))
        self.progressBar_31.setStyleSheet(
            u"QProgressBar::chunk {background-color: #3c78d8;}"
        )
        self.progressBar_31.setValue(100)
        self.progressBar_31.setAlignment(Qt.AlignCenter)
        self.progressBar_31.setTextVisible(False)
        self.progressBar_31.setOrientation(Qt.Vertical)
        self.progressBar_31.setInvertedAppearance(False)
        self.benchBar_3 = QProgressBar(self.bench_frame_bars)
        self.benchBar_3.setObjectName(u"benchBar_3")
        self.benchBar_3.setGeometry(QRect(40, 116, 475, 16))
        self.benchBar_3.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_3.setValue(100)
        self.benchBar_3.setAlignment(Qt.AlignCenter)
        self.benchBar_4 = QProgressBar(self.bench_frame_bars)
        self.benchBar_4.setObjectName(u"benchBar_4")
        self.benchBar_4.setGeometry(QRect(40, 132, 475, 16))
        self.benchBar_4.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_4.setValue(100)
        self.benchBar_4.setAlignment(Qt.AlignCenter)
        self.progressBar_47 = QProgressBar(self.bench_frame_bars)
        self.progressBar_47.setObjectName(u"progressBar_47")
        self.progressBar_47.setGeometry(QRect(520, 120, 8, 41))
        self.progressBar_47.setStyleSheet(
            u"QProgressBar::chunk {background-color:#e06666;}"
        )
        self.progressBar_47.setValue(100)
        self.progressBar_47.setAlignment(Qt.AlignCenter)
        self.progressBar_47.setTextVisible(False)
        self.progressBar_47.setOrientation(Qt.Vertical)
        self.progressBar_47.setInvertedAppearance(False)
        self.benchmark_label = QLabel(self.bench_frame_bars)
        self.benchmark_label.setObjectName(u"benchmark_label")
        self.benchmark_label.setGeometry(QRect(1, 1, 559, 20))
        self.benchmark_label.setMinimumSize(QSize(0, 2))
        self.benchmark_label.setStyleSheet(u"background-color:#315e73")
        self.benchmark_label.setIndent(10)
        self.benchBar_8 = QProgressBar(self.bench_frame_bars)
        self.benchBar_8.setObjectName(u"benchBar_8")
        self.benchBar_8.setGeometry(QRect(40, 200, 475, 16))
        self.benchBar_8.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_8.setValue(100)
        self.benchBar_8.setAlignment(Qt.AlignCenter)
        self.progressBar_26 = QProgressBar(self.bench_frame_bars)
        self.progressBar_26.setObjectName(u"progressBar_26")
        self.progressBar_26.setGeometry(QRect(10, 269, 4, 91))
        self.progressBar_26.setStyleSheet(
            u"QProgressBar::chunk {background-color: #351c75;}"
        )
        self.progressBar_26.setValue(100)
        self.progressBar_26.setAlignment(Qt.AlignCenter)
        self.progressBar_26.setTextVisible(False)
        self.progressBar_26.setOrientation(Qt.Vertical)
        self.progressBar_28 = QProgressBar(self.bench_frame_bars)
        self.progressBar_28.setObjectName(u"progressBar_28")
        self.progressBar_28.setGeometry(QRect(10, 69, 4, 91))
        self.progressBar_28.setStyleSheet(
            u"QProgressBar::chunk {background-color: #cc0000;}"
        )
        self.progressBar_28.setValue(100)
        self.progressBar_28.setAlignment(Qt.AlignCenter)
        self.progressBar_28.setTextVisible(False)
        self.progressBar_28.setOrientation(Qt.Vertical)
        self.progressBar_37 = QProgressBar(self.bench_frame_bars)
        self.progressBar_37.setObjectName(u"progressBar_37")
        self.progressBar_37.setGeometry(QRect(520, 320, 8, 41))
        self.progressBar_37.setStyleSheet(
            u"QProgressBar::chunk {background-color: #674ea7;}"
        )
        self.progressBar_37.setValue(100)
        self.progressBar_37.setAlignment(Qt.AlignCenter)
        self.progressBar_37.setTextVisible(False)
        self.progressBar_37.setOrientation(Qt.Vertical)
        self.progressBar_37.setInvertedAppearance(False)
        self.progressBar_38 = QProgressBar(self.bench_frame_bars)
        self.progressBar_38.setObjectName(u"progressBar_38")
        self.progressBar_38.setGeometry(QRect(520, 270, 8, 41))
        self.progressBar_38.setStyleSheet(
            u"QProgressBar::chunk {background-color: #a64d79;}"
        )
        self.progressBar_38.setValue(100)
        self.progressBar_38.setAlignment(Qt.AlignCenter)
        self.progressBar_38.setTextVisible(False)
        self.progressBar_38.setOrientation(Qt.Vertical)
        self.benchBar_1 = QProgressBar(self.bench_frame_bars)
        self.benchBar_1.setObjectName(u"benchBar_1")
        self.benchBar_1.setGeometry(QRect(40, 84, 475, 16))
        self.benchBar_1.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_1.setValue(100)
        self.benchBar_1.setAlignment(Qt.AlignCenter)
        self.benchBar_11 = QProgressBar(self.bench_frame_bars)
        self.benchBar_11.setObjectName(u"benchBar_11")
        self.benchBar_11.setGeometry(QRect(40, 248, 475, 16))
        self.benchBar_11.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_11.setValue(100)
        self.benchBar_11.setAlignment(Qt.AlignCenter)
        self.progressBar_41 = QProgressBar(self.bench_frame_bars)
        self.progressBar_41.setObjectName(u"progressBar_41")
        self.progressBar_41.setGeometry(QRect(540, 320, 8, 41))
        self.progressBar_41.setStyleSheet(
            u"QProgressBar::chunk {background-color: #674ea7;}"
        )
        self.progressBar_41.setValue(100)
        self.progressBar_41.setAlignment(Qt.AlignCenter)
        self.progressBar_41.setTextVisible(False)
        self.progressBar_41.setOrientation(Qt.Vertical)
        self.progressBar_41.setInvertedAppearance(False)
        self.benchBar_16 = QProgressBar(self.bench_frame_bars)
        self.benchBar_16.setObjectName(u"benchBar_16")
        self.benchBar_16.setGeometry(QRect(40, 332, 475, 16))
        self.benchBar_16.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_16.setValue(100)
        self.benchBar_16.setAlignment(Qt.AlignCenter)
        self.progressBar_32 = QProgressBar(self.bench_frame_bars)
        self.progressBar_32.setObjectName(u"progressBar_32")
        self.progressBar_32.setGeometry(QRect(520, 170, 8, 41))
        self.progressBar_32.setStyleSheet(
            u"QProgressBar::chunk {background-color: #45818e;}"
        )
        self.progressBar_32.setValue(100)
        self.progressBar_32.setAlignment(Qt.AlignCenter)
        self.progressBar_32.setTextVisible(False)
        self.progressBar_32.setOrientation(Qt.Vertical)
        self.progressBar_53 = QProgressBar(self.bench_frame_bars)
        self.progressBar_53.setObjectName(u"progressBar_53")
        self.progressBar_53.setGeometry(QRect(520, 70, 8, 41))
        self.progressBar_53.setStyleSheet(
            u"QProgressBar::chunk {background-color:#f1c232;}"
        )
        self.progressBar_53.setValue(100)
        self.progressBar_53.setAlignment(Qt.AlignCenter)
        self.progressBar_53.setTextVisible(False)
        self.progressBar_53.setOrientation(Qt.Vertical)
        self.benchBar_13 = QProgressBar(self.bench_frame_bars)
        self.benchBar_13.setObjectName(u"benchBar_13")
        self.benchBar_13.setGeometry(QRect(40, 284, 475, 16))
        self.benchBar_13.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_13.setValue(100)
        self.benchBar_13.setAlignment(Qt.AlignCenter)
        self.progressBar_52 = QProgressBar(self.bench_frame_bars)
        self.progressBar_52.setObjectName(u"progressBar_52")
        self.progressBar_52.setGeometry(QRect(540, 70, 8, 41))
        self.progressBar_52.setStyleSheet(
            u"QProgressBar::chunk {background-color:#f1c232;}"
        )
        self.progressBar_52.setValue(100)
        self.progressBar_52.setAlignment(Qt.AlignCenter)
        self.progressBar_52.setTextVisible(False)
        self.progressBar_52.setOrientation(Qt.Vertical)
        self.progressBar_36 = QProgressBar(self.bench_frame_bars)
        self.progressBar_36.setObjectName(u"progressBar_36")
        self.progressBar_36.setGeometry(QRect(540, 170, 8, 41))
        self.progressBar_36.setStyleSheet(
            u"QProgressBar::chunk {background-color: #45818e;}"
        )
        self.progressBar_36.setValue(100)
        self.progressBar_36.setAlignment(Qt.AlignCenter)
        self.progressBar_36.setTextVisible(False)
        self.progressBar_36.setOrientation(Qt.Vertical)
        self.progressBar_33 = QProgressBar(self.bench_frame_bars)
        self.progressBar_33.setObjectName(u"progressBar_33")
        self.progressBar_33.setGeometry(QRect(530, 220, 8, 41))
        self.progressBar_33.setStyleSheet(
            u"QProgressBar::chunk {background-color: #3c78d8;}"
        )
        self.progressBar_33.setValue(100)
        self.progressBar_33.setAlignment(Qt.AlignCenter)
        self.progressBar_33.setTextVisible(False)
        self.progressBar_33.setOrientation(Qt.Vertical)
        self.progressBar_33.setInvertedAppearance(False)
        self.progressBar_27 = QProgressBar(self.bench_frame_bars)
        self.progressBar_27.setObjectName(u"progressBar_27")
        self.progressBar_27.setGeometry(QRect(10, 169, 4, 91))
        self.progressBar_27.setStyleSheet(
            u"QProgressBar::chunk {background-color: #1155cc;}"
        )
        self.progressBar_27.setValue(100)
        self.progressBar_27.setAlignment(Qt.AlignCenter)
        self.progressBar_27.setTextVisible(False)
        self.progressBar_27.setOrientation(Qt.Vertical)
        self.benchBar_7 = QProgressBar(self.bench_frame_bars)
        self.benchBar_7.setObjectName(u"benchBar_7")
        self.benchBar_7.setGeometry(QRect(40, 184, 475, 16))
        self.benchBar_7.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_7.setValue(100)
        self.benchBar_7.setAlignment(Qt.AlignCenter)
        self.benchBar_12 = QProgressBar(self.bench_frame_bars)
        self.benchBar_12.setObjectName(u"benchBar_12")
        self.benchBar_12.setGeometry(QRect(40, 268, 475, 16))
        self.benchBar_12.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_12.setValue(100)
        self.benchBar_12.setAlignment(Qt.AlignCenter)
        self.benchBar_0 = QProgressBar(self.bench_frame_bars)
        self.benchBar_0.setObjectName(u"benchBar_0")
        self.benchBar_0.setGeometry(QRect(40, 68, 475, 16))
        self.benchBar_0.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_0.setValue(100)
        self.benchBar_0.setAlignment(Qt.AlignCenter)
        self.progressBar_40 = QProgressBar(self.bench_frame_bars)
        self.progressBar_40.setObjectName(u"progressBar_40")
        self.progressBar_40.setGeometry(QRect(530, 270, 8, 41))
        self.progressBar_40.setStyleSheet(
            u"QProgressBar::chunk {background-color: #a64d79;}"
        )
        self.progressBar_40.setValue(100)
        self.progressBar_40.setAlignment(Qt.AlignCenter)
        self.progressBar_40.setTextVisible(False)
        self.progressBar_40.setOrientation(Qt.Vertical)
        self.benchBar_2 = QProgressBar(self.bench_frame_bars)
        self.benchBar_2.setObjectName(u"benchBar_2")
        self.benchBar_2.setGeometry(QRect(40, 100, 475, 16))
        self.benchBar_2.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_2.setValue(100)
        self.benchBar_2.setAlignment(Qt.AlignCenter)
        self.benchBar_10 = QProgressBar(self.bench_frame_bars)
        self.benchBar_10.setObjectName(u"benchBar_10")
        self.benchBar_10.setGeometry(QRect(40, 232, 475, 16))
        self.benchBar_10.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_10.setValue(100)
        self.benchBar_10.setAlignment(Qt.AlignCenter)
        self.progressBar_35 = QProgressBar(self.bench_frame_bars)
        self.progressBar_35.setObjectName(u"progressBar_35")
        self.progressBar_35.setGeometry(QRect(540, 220, 8, 41))
        self.progressBar_35.setStyleSheet(
            u"QProgressBar::chunk {background-color: #3c78d8;}"
        )
        self.progressBar_35.setValue(100)
        self.progressBar_35.setAlignment(Qt.AlignCenter)
        self.progressBar_35.setTextVisible(False)
        self.progressBar_35.setOrientation(Qt.Vertical)
        self.progressBar_35.setInvertedAppearance(False)
        self.progressBar_42 = QProgressBar(self.bench_frame_bars)
        self.progressBar_42.setObjectName(u"progressBar_42")
        self.progressBar_42.setGeometry(QRect(540, 270, 8, 41))
        self.progressBar_42.setStyleSheet(
            u"QProgressBar::chunk {background-color: #a64d79;}"
        )
        self.progressBar_42.setValue(100)
        self.progressBar_42.setAlignment(Qt.AlignCenter)
        self.progressBar_42.setTextVisible(False)
        self.progressBar_42.setOrientation(Qt.Vertical)
        self.progressBar_34 = QProgressBar(self.bench_frame_bars)
        self.progressBar_34.setObjectName(u"progressBar_34")
        self.progressBar_34.setGeometry(QRect(530, 170, 8, 41))
        self.progressBar_34.setStyleSheet(
            u"QProgressBar::chunk {background-color: #45818e;}"
        )
        self.progressBar_34.setValue(100)
        self.progressBar_34.setAlignment(Qt.AlignCenter)
        self.progressBar_34.setTextVisible(False)
        self.progressBar_34.setOrientation(Qt.Vertical)
        self.progressBar_55 = QProgressBar(self.bench_frame_bars)
        self.progressBar_55.setObjectName(u"progressBar_55")
        self.progressBar_55.setGeometry(QRect(540, 120, 8, 41))
        self.progressBar_55.setStyleSheet(
            u"QProgressBar::chunk {background-color:#e06666;}"
        )
        self.progressBar_55.setValue(100)
        self.progressBar_55.setAlignment(Qt.AlignCenter)
        self.progressBar_55.setTextVisible(False)
        self.progressBar_55.setOrientation(Qt.Vertical)
        self.progressBar_55.setInvertedAppearance(False)
        self.benchBar_9 = QProgressBar(self.bench_frame_bars)
        self.benchBar_9.setObjectName(u"benchBar_9")
        self.benchBar_9.setGeometry(QRect(40, 216, 475, 16))
        self.benchBar_9.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_9.setValue(100)
        self.benchBar_9.setAlignment(Qt.AlignCenter)
        self.benchBar_17 = QProgressBar(self.bench_frame_bars)
        self.benchBar_17.setObjectName(u"benchBar_17")
        self.benchBar_17.setGeometry(QRect(40, 348, 475, 16))
        self.benchBar_17.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_17.setValue(100)
        self.benchBar_17.setAlignment(Qt.AlignCenter)
        self.benchBar_14 = QProgressBar(self.bench_frame_bars)
        self.benchBar_14.setObjectName(u"benchBar_14")
        self.benchBar_14.setGeometry(QRect(40, 300, 475, 16))
        self.benchBar_14.setStyleSheet(
            u"QProgressBar::chunk {background-color: #00b7c2; border :1px solid black;}"
        )
        self.benchBar_14.setValue(100)
        self.benchBar_14.setAlignment(Qt.AlignCenter)
        self.rank_label = QLabel(self.bench_frame_bars)
        self.rank_label.setObjectName(u"rank_label")
        self.rank_label.setGeometry(QRect(1, 19, 559, 41))
        self.rank_label.setStyleSheet(u"font: 63 30pt 'Segoe UI Semibold'")
        self.rank_label.setAlignment(Qt.AlignCenter)
        self.benchRankBar_0 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_0.setObjectName(u"benchRankBar_0")
        self.benchRankBar_0.setGeometry(QRect(20, 68, 16, 16))
        self.benchRankBar_0.setStyleSheet(u"")
        self.benchRankBar_0.setMaximum(1)
        self.benchRankBar_0.setValue(1)
        self.benchRankBar_0.setTextVisible(False)
        self.benchRankBar_1 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_1.setObjectName(u"benchRankBar_1")
        self.benchRankBar_1.setGeometry(QRect(20, 84, 16, 16))
        self.benchRankBar_1.setMaximum(1)
        self.benchRankBar_1.setValue(1)
        self.benchRankBar_1.setTextVisible(False)
        self.benchRankBar_2 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_2.setObjectName(u"benchRankBar_2")
        self.benchRankBar_2.setGeometry(QRect(20, 100, 16, 16))
        self.benchRankBar_2.setMaximum(1)
        self.benchRankBar_2.setValue(1)
        self.benchRankBar_2.setTextVisible(False)
        self.benchRankBar_3 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_3.setObjectName(u"benchRankBar_3")
        self.benchRankBar_3.setGeometry(QRect(20, 116, 16, 16))
        self.benchRankBar_3.setMaximum(1)
        self.benchRankBar_3.setValue(1)
        self.benchRankBar_3.setTextVisible(False)
        self.benchRankBar_4 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_4.setObjectName(u"benchRankBar_4")
        self.benchRankBar_4.setGeometry(QRect(20, 132, 16, 16))
        self.benchRankBar_4.setMaximum(1)
        self.benchRankBar_4.setValue(1)
        self.benchRankBar_4.setTextVisible(False)
        self.benchRankBar_5 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_5.setObjectName(u"benchRankBar_5")
        self.benchRankBar_5.setGeometry(QRect(20, 148, 16, 16))
        self.benchRankBar_5.setMaximum(1)
        self.benchRankBar_5.setValue(1)
        self.benchRankBar_5.setTextVisible(False)
        self.benchRankBar_6 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_6.setObjectName(u"benchRankBar_6")
        self.benchRankBar_6.setGeometry(QRect(20, 168, 16, 16))
        self.benchRankBar_6.setMaximum(1)
        self.benchRankBar_6.setValue(1)
        self.benchRankBar_6.setTextVisible(False)
        self.benchRankBar_7 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_7.setObjectName(u"benchRankBar_7")
        self.benchRankBar_7.setGeometry(QRect(20, 184, 16, 16))
        self.benchRankBar_7.setMaximum(1)
        self.benchRankBar_7.setValue(1)
        self.benchRankBar_7.setTextVisible(False)
        self.benchRankBar_8 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_8.setObjectName(u"benchRankBar_8")
        self.benchRankBar_8.setGeometry(QRect(20, 200, 16, 16))
        self.benchRankBar_8.setMaximum(1)
        self.benchRankBar_8.setValue(1)
        self.benchRankBar_8.setTextVisible(False)
        self.benchRankBar_9 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_9.setObjectName(u"benchRankBar_9")
        self.benchRankBar_9.setGeometry(QRect(20, 216, 16, 16))
        self.benchRankBar_9.setMaximum(1)
        self.benchRankBar_9.setValue(1)
        self.benchRankBar_9.setTextVisible(False)
        self.benchRankBar_10 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_10.setObjectName(u"benchRankBar_10")
        self.benchRankBar_10.setGeometry(QRect(20, 232, 16, 16))
        self.benchRankBar_10.setMaximum(1)
        self.benchRankBar_10.setValue(1)
        self.benchRankBar_10.setTextVisible(False)
        self.benchRankBar_11 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_11.setObjectName(u"benchRankBar_11")
        self.benchRankBar_11.setGeometry(QRect(20, 248, 16, 16))
        self.benchRankBar_11.setMaximum(1)
        self.benchRankBar_11.setValue(1)
        self.benchRankBar_11.setTextVisible(False)
        self.benchRankBar_12 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_12.setObjectName(u"benchRankBar_12")
        self.benchRankBar_12.setGeometry(QRect(20, 268, 16, 16))
        self.benchRankBar_12.setMaximum(1)
        self.benchRankBar_12.setValue(1)
        self.benchRankBar_12.setTextVisible(False)
        self.benchRankBar_13 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_13.setObjectName(u"benchRankBar_13")
        self.benchRankBar_13.setGeometry(QRect(20, 284, 16, 16))
        self.benchRankBar_13.setMaximum(1)
        self.benchRankBar_13.setValue(1)
        self.benchRankBar_13.setTextVisible(False)
        self.benchRankBar_14 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_14.setObjectName(u"benchRankBar_14")
        self.benchRankBar_14.setGeometry(QRect(20, 300, 16, 16))
        self.benchRankBar_14.setMaximum(1)
        self.benchRankBar_14.setValue(1)
        self.benchRankBar_14.setTextVisible(False)
        self.benchRankBar_15 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_15.setObjectName(u"benchRankBar_15")
        self.benchRankBar_15.setGeometry(QRect(20, 316, 16, 16))
        self.benchRankBar_15.setMaximum(1)
        self.benchRankBar_15.setValue(1)
        self.benchRankBar_15.setTextVisible(False)
        self.benchRankBar_16 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_16.setObjectName(u"benchRankBar_16")
        self.benchRankBar_16.setGeometry(QRect(20, 332, 16, 16))
        self.benchRankBar_16.setMaximum(1)
        self.benchRankBar_16.setValue(1)
        self.benchRankBar_16.setTextVisible(False)
        self.benchRankBar_17 = QProgressBar(self.bench_frame_bars)
        self.benchRankBar_17.setObjectName(u"benchRankBar_17")
        self.benchRankBar_17.setGeometry(QRect(20, 348, 16, 16))
        self.benchRankBar_17.setMaximum(1)
        self.benchRankBar_17.setValue(1)
        self.benchRankBar_17.setTextVisible(False)
        self.bench_frame_0 = QFrame(self.home)
        self.bench_frame_0.setObjectName(u"bench_frame_0")
        self.bench_frame_0.setGeometry(QRect(50, 40, 181, 181))
        self.bench_frame_0.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_0.setFrameShape(QFrame.HLine)
        self.bench_frame_0.setFrameShadow(QFrame.Raised)
        self.lblBench_0 = QLabel(self.bench_frame_0)
        self.lblBench_0.setObjectName(u"lblBench_0")
        self.lblBench_0.setGeometry(QRect(0, 40, 181, 61))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(False)
        font3.setItalic(False)
        self.lblBench_0.setFont(font3)
        self.lblBench_0.setStyleSheet(
            u"background-color:#2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_0.setAlignment(Qt.AlignCenter)
        self.indexLbl_0 = QLabel(self.bench_frame_0)
        self.indexLbl_0.setObjectName(u"indexLbl_0")
        self.indexLbl_0.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_0.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_0.setIndent(10)
        self.graphWidget_0 = QWidget(self.bench_frame_0)
        self.graphWidget_0.setObjectName(u"graphWidget_0")
        self.graphWidget_0.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_1 = QFrame(self.home)
        self.bench_frame_1.setObjectName(u"bench_frame_1")
        self.bench_frame_1.setGeometry(QRect(240, 40, 181, 181))
        self.bench_frame_1.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_1.setFrameShape(QFrame.HLine)
        self.bench_frame_1.setFrameShadow(QFrame.Raised)
        self.lblBench_1 = QLabel(self.bench_frame_1)
        self.lblBench_1.setObjectName(u"lblBench_1")
        self.lblBench_1.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_1.setFont(font3)
        self.lblBench_1.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_1.setAlignment(Qt.AlignCenter)
        self.indexLbl_1 = QLabel(self.bench_frame_1)
        self.indexLbl_1.setObjectName(u"indexLbl_1")
        self.indexLbl_1.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_1.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_1.setIndent(10)
        self.graphWidget_1 = QWidget(self.bench_frame_1)
        self.graphWidget_1.setObjectName(u"graphWidget_1")
        self.graphWidget_1.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_2 = QFrame(self.home)
        self.bench_frame_2.setObjectName(u"bench_frame_2")
        self.bench_frame_2.setGeometry(QRect(430, 40, 181, 181))
        self.bench_frame_2.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_2.setFrameShape(QFrame.HLine)
        self.bench_frame_2.setFrameShadow(QFrame.Raised)
        self.lblBench_2 = QLabel(self.bench_frame_2)
        self.lblBench_2.setObjectName(u"lblBench_2")
        self.lblBench_2.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_2.setFont(font3)
        self.lblBench_2.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_2.setAlignment(Qt.AlignCenter)
        self.indexLbl_2 = QLabel(self.bench_frame_2)
        self.indexLbl_2.setObjectName(u"indexLbl_2")
        self.indexLbl_2.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_2.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_2.setIndent(10)
        self.graphWidget_2 = QWidget(self.bench_frame_2)
        self.graphWidget_2.setObjectName(u"graphWidget_2")
        self.graphWidget_2.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_3 = QFrame(self.home)
        self.bench_frame_3.setObjectName(u"bench_frame_3")
        self.bench_frame_3.setGeometry(QRect(50, 240, 181, 181))
        self.bench_frame_3.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_3.setFrameShape(QFrame.HLine)
        self.bench_frame_3.setFrameShadow(QFrame.Raised)
        self.lblBench_3 = QLabel(self.bench_frame_3)
        self.lblBench_3.setObjectName(u"lblBench_3")
        self.lblBench_3.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_3.setFont(font3)
        self.lblBench_3.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_3.setAlignment(Qt.AlignCenter)
        self.indexLbl_3 = QLabel(self.bench_frame_3)
        self.indexLbl_3.setObjectName(u"indexLbl_3")
        self.indexLbl_3.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_3.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_3.setIndent(10)
        self.graphWidget_3 = QWidget(self.bench_frame_3)
        self.graphWidget_3.setObjectName(u"graphWidget_3")
        self.graphWidget_3.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_4 = QFrame(self.home)
        self.bench_frame_4.setObjectName(u"bench_frame_4")
        self.bench_frame_4.setGeometry(QRect(240, 240, 181, 181))
        self.bench_frame_4.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_4.setFrameShape(QFrame.HLine)
        self.bench_frame_4.setFrameShadow(QFrame.Raised)
        self.lblBench_4 = QLabel(self.bench_frame_4)
        self.lblBench_4.setObjectName(u"lblBench_4")
        self.lblBench_4.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_4.setFont(font3)
        self.lblBench_4.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_4.setAlignment(Qt.AlignCenter)
        self.indexLbl_4 = QLabel(self.bench_frame_4)
        self.indexLbl_4.setObjectName(u"indexLbl_4")
        self.indexLbl_4.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_4.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_4.setIndent(10)
        self.graphWidget_4 = QWidget(self.bench_frame_4)
        self.graphWidget_4.setObjectName(u"graphWidget_4")
        self.graphWidget_4.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_5 = QFrame(self.home)
        self.bench_frame_5.setObjectName(u"bench_frame_5")
        self.bench_frame_5.setGeometry(QRect(430, 240, 181, 181))
        self.bench_frame_5.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_5.setFrameShape(QFrame.HLine)
        self.bench_frame_5.setFrameShadow(QFrame.Raised)
        self.lblBench_5 = QLabel(self.bench_frame_5)
        self.lblBench_5.setObjectName(u"lblBench_5")
        self.lblBench_5.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_5.setFont(font3)
        self.lblBench_5.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_5.setAlignment(Qt.AlignCenter)
        self.indexLbl_5 = QLabel(self.bench_frame_5)
        self.indexLbl_5.setObjectName(u"indexLbl_5")
        self.indexLbl_5.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_5.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_5.setIndent(10)
        self.graphWidget_5 = QWidget(self.bench_frame_5)
        self.graphWidget_5.setObjectName(u"graphWidget_5")
        self.graphWidget_5.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_6 = QFrame(self.home)
        self.bench_frame_6.setObjectName(u"bench_frame_6")
        self.bench_frame_6.setGeometry(QRect(630, 40, 181, 181))
        self.bench_frame_6.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_6.setFrameShape(QFrame.HLine)
        self.bench_frame_6.setFrameShadow(QFrame.Raised)
        self.lblBench_6 = QLabel(self.bench_frame_6)
        self.lblBench_6.setObjectName(u"lblBench_6")
        self.lblBench_6.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_6.setFont(font3)
        self.lblBench_6.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_6.setAlignment(Qt.AlignCenter)
        self.indexLbl_6 = QLabel(self.bench_frame_6)
        self.indexLbl_6.setObjectName(u"indexLbl_6")
        self.indexLbl_6.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_6.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_6.setIndent(10)
        self.graphWidget_6 = QWidget(self.bench_frame_6)
        self.graphWidget_6.setObjectName(u"graphWidget_6")
        self.graphWidget_6.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_7 = QFrame(self.home)
        self.bench_frame_7.setObjectName(u"bench_frame_7")
        self.bench_frame_7.setGeometry(QRect(820, 40, 181, 181))
        self.bench_frame_7.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_7.setFrameShape(QFrame.NoFrame)
        self.bench_frame_7.setFrameShadow(QFrame.Raised)
        self.lblBench_7 = QLabel(self.bench_frame_7)
        self.lblBench_7.setObjectName(u"lblBench_7")
        self.lblBench_7.setGeometry(QRect(10, 40, 161, 61))
        self.lblBench_7.setFont(font3)
        self.lblBench_7.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_7.setAlignment(Qt.AlignCenter)
        self.indexLbl_7 = QLabel(self.bench_frame_7)
        self.indexLbl_7.setObjectName(u"indexLbl_7")
        self.indexLbl_7.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_7.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_7.setIndent(10)
        self.graphWidget_7 = QWidget(self.bench_frame_7)
        self.graphWidget_7.setObjectName(u"graphWidget_7")
        self.graphWidget_7.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_8 = QFrame(self.home)
        self.bench_frame_8.setObjectName(u"bench_frame_8")
        self.bench_frame_8.setGeometry(QRect(1010, 40, 181, 181))
        self.bench_frame_8.setStyleSheet(u"background-color:#2f3b52;")
        self.bench_frame_8.setFrameShape(QFrame.HLine)
        self.bench_frame_8.setFrameShadow(QFrame.Raised)
        self.lblBench_8 = QLabel(self.bench_frame_8)
        self.lblBench_8.setObjectName(u"lblBench_8")
        self.lblBench_8.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_8.setFont(font3)
        self.lblBench_8.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_8.setAlignment(Qt.AlignCenter)
        self.indexLbl_8 = QLabel(self.bench_frame_8)
        self.indexLbl_8.setObjectName(u"indexLbl_8")
        self.indexLbl_8.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_8.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_8.setIndent(10)
        self.graphWidget_8 = QWidget(self.bench_frame_8)
        self.graphWidget_8.setObjectName(u"graphWidget_8")
        self.graphWidget_8.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_9 = QFrame(self.home)
        self.bench_frame_9.setObjectName(u"bench_frame_9")
        self.bench_frame_9.setGeometry(QRect(630, 240, 181, 181))
        self.bench_frame_9.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_9.setFrameShape(QFrame.HLine)
        self.bench_frame_9.setFrameShadow(QFrame.Raised)
        self.lblBench_9 = QLabel(self.bench_frame_9)
        self.lblBench_9.setObjectName(u"lblBench_9")
        self.lblBench_9.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_9.setFont(font3)
        self.lblBench_9.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_9.setAlignment(Qt.AlignCenter)
        self.indexLbl_9 = QLabel(self.bench_frame_9)
        self.indexLbl_9.setObjectName(u"indexLbl_9")
        self.indexLbl_9.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_9.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_9.setIndent(10)
        self.graphWidget_9 = QWidget(self.bench_frame_9)
        self.graphWidget_9.setObjectName(u"graphWidget_9")
        self.graphWidget_9.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_10 = QFrame(self.home)
        self.bench_frame_10.setObjectName(u"bench_frame_10")
        self.bench_frame_10.setGeometry(QRect(820, 240, 181, 181))
        self.bench_frame_10.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_10.setFrameShape(QFrame.HLine)
        self.bench_frame_10.setFrameShadow(QFrame.Raised)
        self.lblBench_10 = QLabel(self.bench_frame_10)
        self.lblBench_10.setObjectName(u"lblBench_10")
        self.lblBench_10.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_10.setFont(font3)
        self.lblBench_10.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_10.setAlignment(Qt.AlignCenter)
        self.indexLbl_10 = QLabel(self.bench_frame_10)
        self.indexLbl_10.setObjectName(u"indexLbl_10")
        self.indexLbl_10.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_10.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_10.setIndent(10)
        self.graphWidget_10 = QWidget(self.bench_frame_10)
        self.graphWidget_10.setObjectName(u"graphWidget_10")
        self.graphWidget_10.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_11 = QFrame(self.home)
        self.bench_frame_11.setObjectName(u"bench_frame_11")
        self.bench_frame_11.setGeometry(QRect(1010, 240, 181, 181))
        self.bench_frame_11.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_11.setFrameShape(QFrame.HLine)
        self.bench_frame_11.setFrameShadow(QFrame.Raised)
        self.lblBench_11 = QLabel(self.bench_frame_11)
        self.lblBench_11.setObjectName(u"lblBench_11")
        self.lblBench_11.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_11.setFont(font3)
        self.lblBench_11.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_11.setAlignment(Qt.AlignCenter)
        self.indexLbl_11 = QLabel(self.bench_frame_11)
        self.indexLbl_11.setObjectName(u"indexLbl_11")
        self.indexLbl_11.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_11.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_11.setIndent(10)
        self.graphWidget_11 = QWidget(self.bench_frame_11)
        self.graphWidget_11.setObjectName(u"graphWidget_11")
        self.graphWidget_11.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_12 = QFrame(self.home)
        self.bench_frame_12.setObjectName(u"bench_frame_12")
        self.bench_frame_12.setGeometry(QRect(630, 460, 181, 181))
        self.bench_frame_12.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_12.setFrameShape(QFrame.HLine)
        self.bench_frame_12.setFrameShadow(QFrame.Raised)
        self.lblBench_12 = QLabel(self.bench_frame_12)
        self.lblBench_12.setObjectName(u"lblBench_12")
        self.lblBench_12.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_12.setFont(font3)
        self.lblBench_12.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_12.setAlignment(Qt.AlignCenter)
        self.indexLbl_12 = QLabel(self.bench_frame_12)
        self.indexLbl_12.setObjectName(u"indexLbl_12")
        self.indexLbl_12.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_12.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_12.setIndent(10)
        self.graphWidget_12 = QWidget(self.bench_frame_12)
        self.graphWidget_12.setObjectName(u"graphWidget_12")
        self.graphWidget_12.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_13 = QFrame(self.home)
        self.bench_frame_13.setObjectName(u"bench_frame_13")
        self.bench_frame_13.setGeometry(QRect(820, 460, 181, 181))
        self.bench_frame_13.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_13.setFrameShape(QFrame.HLine)
        self.bench_frame_13.setFrameShadow(QFrame.Raised)
        self.lblBench_13 = QLabel(self.bench_frame_13)
        self.lblBench_13.setObjectName(u"lblBench_13")
        self.lblBench_13.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_13.setFont(font3)
        self.lblBench_13.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_13.setAlignment(Qt.AlignCenter)
        self.indexLbl_13 = QLabel(self.bench_frame_13)
        self.indexLbl_13.setObjectName(u"indexLbl_13")
        self.indexLbl_13.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_13.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_13.setIndent(10)
        self.graphWidget_13 = QWidget(self.bench_frame_13)
        self.graphWidget_13.setObjectName(u"graphWidget_13")
        self.graphWidget_13.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_14 = QFrame(self.home)
        self.bench_frame_14.setObjectName(u"bench_frame_14")
        self.bench_frame_14.setGeometry(QRect(1010, 460, 181, 181))
        self.bench_frame_14.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_14.setFrameShape(QFrame.HLine)
        self.bench_frame_14.setFrameShadow(QFrame.Raised)
        self.lblBench_14 = QLabel(self.bench_frame_14)
        self.lblBench_14.setObjectName(u"lblBench_14")
        self.lblBench_14.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_14.setFont(font3)
        self.lblBench_14.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_14.setAlignment(Qt.AlignCenter)
        self.indexLbl_14 = QLabel(self.bench_frame_14)
        self.indexLbl_14.setObjectName(u"indexLbl_14")
        self.indexLbl_14.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_14.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_14.setIndent(10)
        self.graphWidget_14 = QWidget(self.bench_frame_14)
        self.graphWidget_14.setObjectName(u"graphWidget_14")
        self.graphWidget_14.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_15 = QFrame(self.home)
        self.bench_frame_15.setObjectName(u"bench_frame_15")
        self.bench_frame_15.setGeometry(QRect(630, 660, 181, 181))
        self.bench_frame_15.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_15.setFrameShape(QFrame.HLine)
        self.bench_frame_15.setFrameShadow(QFrame.Raised)
        self.lblBench_15 = QLabel(self.bench_frame_15)
        self.lblBench_15.setObjectName(u"lblBench_15")
        self.lblBench_15.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_15.setFont(font3)
        self.lblBench_15.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_15.setAlignment(Qt.AlignCenter)
        self.indexLbl_15 = QLabel(self.bench_frame_15)
        self.indexLbl_15.setObjectName(u"indexLbl_15")
        self.indexLbl_15.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_15.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_15.setIndent(10)
        self.graphWidget_15 = QWidget(self.bench_frame_15)
        self.graphWidget_15.setObjectName(u"graphWidget_15")
        self.graphWidget_15.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_16 = QFrame(self.home)
        self.bench_frame_16.setObjectName(u"bench_frame_16")
        self.bench_frame_16.setGeometry(QRect(820, 660, 181, 181))
        self.bench_frame_16.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_16.setFrameShape(QFrame.HLine)
        self.bench_frame_16.setFrameShadow(QFrame.Raised)
        self.lblBench_16 = QLabel(self.bench_frame_16)
        self.lblBench_16.setObjectName(u"lblBench_16")
        self.lblBench_16.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_16.setFont(font3)
        self.lblBench_16.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_16.setAlignment(Qt.AlignCenter)
        self.indexLbl_16 = QLabel(self.bench_frame_16)
        self.indexLbl_16.setObjectName(u"indexLbl_16")
        self.indexLbl_16.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_16.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_16.setIndent(10)
        self.graphWidget_16 = QWidget(self.bench_frame_16)
        self.graphWidget_16.setObjectName(u"graphWidget_16")
        self.graphWidget_16.setGeometry(QRect(0, 90, 181, 91))
        self.bench_frame_17 = QFrame(self.home)
        self.bench_frame_17.setObjectName(u"bench_frame_17")
        self.bench_frame_17.setGeometry(QRect(1010, 660, 181, 181))
        self.bench_frame_17.setStyleSheet(u"background-color:#2f3b52")
        self.bench_frame_17.setFrameShape(QFrame.HLine)
        self.bench_frame_17.setFrameShadow(QFrame.Raised)
        self.lblBench_17 = QLabel(self.bench_frame_17)
        self.lblBench_17.setObjectName(u"lblBench_17")
        self.lblBench_17.setGeometry(QRect(0, 40, 181, 61))
        self.lblBench_17.setFont(font3)
        self.lblBench_17.setStyleSheet(
            u"background-color: #2f3b52; font: 63 30pt 'Segoe UI Semibold'"
        )
        self.lblBench_17.setAlignment(Qt.AlignCenter)
        self.indexLbl_17 = QLabel(self.bench_frame_17)
        self.indexLbl_17.setObjectName(u"indexLbl_17")
        self.indexLbl_17.setGeometry(QRect(1, 1, 179, 20))
        self.indexLbl_17.setStyleSheet(u"background-color:#315e73")
        self.indexLbl_17.setIndent(10)
        self.graphWidget_17 = QWidget(self.bench_frame_17)
        self.graphWidget_17.setObjectName(u"graphWidget_17")
        self.graphWidget_17.setGeometry(QRect(0, 90, 181, 91))
        self.progressBar_29 = QProgressBar(self.home)
        self.progressBar_29.setObjectName(u"progressBar_29")
        self.progressBar_29.setGeometry(QRect(50, 30, 561, 8))
        self.progressBar_29.setStyleSheet(
            u"QProgressBar::chunk {background-color: #cc0000;}"
        )
        self.progressBar_29.setValue(100)
        self.progressBar_29.setAlignment(Qt.AlignCenter)
        self.progressBar_29.setTextVisible(False)
        self.progressBar_29.setOrientation(Qt.Horizontal)
        self.progressBar_30 = QProgressBar(self.home)
        self.progressBar_30.setObjectName(u"progressBar_30")
        self.progressBar_30.setGeometry(QRect(630, 30, 561, 8))
        self.progressBar_30.setStyleSheet(
            u"QProgressBar::chunk {background-color: #1155cc;}"
        )
        self.progressBar_30.setValue(100)
        self.progressBar_30.setAlignment(Qt.AlignCenter)
        self.progressBar_30.setTextVisible(False)
        self.progressBar_30.setOrientation(Qt.Horizontal)
        self.progressBar_43 = QProgressBar(self.home)
        self.progressBar_43.setObjectName(u"progressBar_43")
        self.progressBar_43.setGeometry(QRect(630, 450, 561, 8))
        self.progressBar_43.setStyleSheet(
            u"QProgressBar::chunk {background-color: #351c75;}"
        )
        self.progressBar_43.setValue(100)
        self.progressBar_43.setAlignment(Qt.AlignCenter)
        self.progressBar_43.setTextVisible(False)
        self.progressBar_43.setOrientation(Qt.Horizontal)
        self.stackedWidget.addWidget(self.home)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.settings)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rb_ra_adv = QRadioButton(self.settings)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rb_ra_adv)
        self.rb_ra_adv.setObjectName(u"rb_ra_adv")

        self.gridLayout_2.addWidget(self.rb_ra_adv, 7, 0, 1, 1)

        self.rb_ra_easy = QRadioButton(self.settings)
        self.buttonGroup.addButton(self.rb_ra_easy)
        self.rb_ra_easy.setObjectName(u"rb_ra_easy")

        self.gridLayout_2.addWidget(self.rb_ra_easy, 6, 0, 1, 1)

        self.btn_refreshPage = QPushButton(self.settings)
        self.btn_refreshPage.setObjectName(u"btn_refreshPage")
        self.btn_refreshPage.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-reload.png);\n"
            "background-position: left center;\n"
            "background-repeat: no-repeat;\n"
            "padding-left: 21px;\n"
            "padding-right: 10px;\n"
            "border-radius: 0px;\n"
            "border: none;\n"
            "border-left: 12px solid transparent;\n"
            "background-color: transparent;\n"
            "text-align: left;\n"
            ""
        )

        self.gridLayout_2.addWidget(self.btn_refreshPage, 11, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.btn_directory = QPushButton(self.settings)
        self.btn_directory.setObjectName(u"btn_directory")
        self.btn_directory.setFont(font)
        self.btn_directory.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-folder.png);\n"
            "background-position: left center;\n"
            "background-repeat: no-repeat;\n"
            "padding-left: 21px;\n"
            "padding-right: 10px;\n"
            "border-radius: 0px;\n"
            "border: none;\n"
            "border-left: 12px solid transparent;\n"
            "background-color: transparent;\n"
            "text-align: left;\n"
            "\n"
            ""
        )

        self.gridLayout_2.addWidget(self.btn_directory, 10, 0, 1, 1)

        self.rb_volt_adv = QRadioButton(self.settings)
        self.buttonGroup.addButton(self.rb_volt_adv)
        self.rb_volt_adv.setObjectName(u"rb_volt_adv")

        self.gridLayout_2.addWidget(self.rb_volt_adv, 5, 0, 1, 1)

        self.label_24 = QLabel(self.settings)
        self.label_24.setObjectName(u"label_24")
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u'font: 15pt "Roboto Mono";')

        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_2, 9, 0, 1, 1)

        self.btn_about = QPushButton(self.settings)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-mug.png);\n"
            "background-position: left center;\n"
            "background-repeat: no-repeat;\n"
            "padding-left: 21px;\n"
            "padding-right: 10px;\n"
            "border-radius: 0px;\n"
            "border: none;\n"
            "border-left: 12px solid transparent;\n"
            "background-color: transparent;\n"
            "text-align: left;"
        )

        self.gridLayout_2.addWidget(self.btn_about, 12, 0, 1, 1)

        self.radioButton = QRadioButton(self.settings)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_2.addWidget(self.radioButton, 4, 0, 1, 1)

        self.rb_custom = QRadioButton(self.settings)
        self.buttonGroup.addButton(self.rb_custom)
        self.rb_custom.setObjectName(u"rb_custom")

        self.gridLayout_2.addWidget(self.rb_custom, 8, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.settings)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.page_history.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.page_history)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.treeView = QTreeView(self.page_history)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"QTreeView::item {   padding: 0 15px; }")
        self.treeView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_6.addWidget(self.treeView)

        self.stackedWidget.addWidget(self.page_history)
        self.page_performance = QWidget()
        self.page_performance.setObjectName(u"page_performance")
        self.label = QLabel(self.page_performance)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 0, 311, 16))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineGraphHistoryView = PlotWidget(self.page_performance)
        self.lineGraphHistoryView.setObjectName(u"lineGraphHistoryView")
        self.lineGraphHistoryView.setGeometry(QRect(10, 200, 1201, 631))
        self.layoutWidget = QWidget(self.page_performance)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(160, 80, 93, 92))
        self.gridLayout_4 = QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lblHighScore = QLabel(self.layoutWidget)
        self.lblHighScore.setObjectName(u"lblHighScore")

        self.gridLayout_4.addWidget(self.lblHighScore, 0, 0, 1, 1)

        self.lblAverageScore = QLabel(self.layoutWidget)
        self.lblAverageScore.setObjectName(u"lblAverageScore")

        self.gridLayout_4.addWidget(self.lblAverageScore, 1, 0, 1, 1)

        self.lblAverageAcc = QLabel(self.layoutWidget)
        self.lblAverageAcc.setObjectName(u"lblAverageAcc")

        self.gridLayout_4.addWidget(self.lblAverageAcc, 2, 0, 1, 1)

        self.lblTotalPlayed = QLabel(self.layoutWidget)
        self.lblTotalPlayed.setObjectName(u"lblTotalPlayed")

        self.gridLayout_4.addWidget(self.lblTotalPlayed, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.page_performance)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 20, 34, 34))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(
            u":/icons/images/icons/cil-description.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.pushButton.setIcon(icon4)
        self.comboBox = QComboBox(self.page_performance)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 20, 311, 34))
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)
        self.layoutWidget1 = QWidget(self.page_performance)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(60, 80, 93, 92))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.line_2 = QFrame(self.page_performance)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 180, 1181, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.barGraphHistoryView = PlotWidget(self.page_performance)
        self.barGraphHistoryView.setObjectName(u"barGraphHistoryView")
        self.barGraphHistoryView.setGeometry(QRect(520, 20, 691, 161))
        self.layoutWidget_2 = QWidget(self.page_performance)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(290, 80, 97, 92))
        self.gridLayout_5 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_12 = QLabel(self.layoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.layoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.layoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.layoutWidget_15 = QWidget(self.page_performance)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(400, 80, 93, 92))
        self.gridLayout_21 = QGridLayout(self.layoutWidget_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lblScore = QLabel(self.layoutWidget_15)
        self.lblScore.setObjectName(u"lblScore")

        self.gridLayout_21.addWidget(self.lblScore, 0, 0, 1, 1)

        self.lblDiffAverageScore = QLabel(self.layoutWidget_15)
        self.lblDiffAverageScore.setObjectName(u"lblDiffAverageScore")

        self.gridLayout_21.addWidget(self.lblDiffAverageScore, 1, 0, 1, 1)

        self.lblDiffHighScore = QLabel(self.layoutWidget_15)
        self.lblDiffHighScore.setObjectName(u"lblDiffHighScore")

        self.gridLayout_21.addWidget(self.lblDiffHighScore, 2, 0, 1, 1)

        self.lblTrending = QLabel(self.layoutWidget_15)
        self.lblTrending.setObjectName(u"lblTrending")

        self.gridLayout_21.addWidget(self.lblTrending, 3, 0, 1, 1)

        self.label_57 = QLabel(self.page_performance)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(60, 60, 191, 20))
        self.label_57.setAlignment(Qt.AlignCenter)
        self.label_58 = QLabel(self.page_performance)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(290, 60, 201, 20))
        self.label_58.setFont(font)
        self.label_58.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_performance)
        self.page_guide = QWidget()
        self.page_guide.setObjectName(u"page_guide")
        self.verticalLayout_21 = QVBoxLayout(self.page_guide)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame = QFrame(self.page_guide)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 90, 1201, 41))
        self.label_6.setStyleSheet(u"font: 63 30pt 'Segoe UI Semibold'")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 190, 391, 21))
        self.label_7.setStyleSheet(u"font:15pt 'egoe UI Semibold'")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 220, 401, 71))
        self.label_8.setStyleSheet(u"font: 63 10pt 'Segoe UI Semibold'")
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 140, 581, 20))
        self.label_9.setStyleSheet(u"font:13pt 'egoe UI Semibold'")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(230, 420, 201, 16))
        self.label_10.setStyleSheet(u"font:15pt 'egoe UI Semibold'")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(230, 480, 361, 16))
        self.label_16.setStyleSheet(u"font:15pt 'egoe UI Semibold'")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(230, 540, 241, 16))
        self.label_17.setStyleSheet(u"font:15pt 'egoe UI Semibold'")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(230, 590, 241, 16))
        self.label_18.setStyleSheet(u"font:15pt 'egoe UI Semibold'")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 640, 171, 24))
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(230, 440, 291, 16))
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(230, 500, 351, 16))
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(230, 560, 341, 16))
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(230, 610, 291, 16))

        self.verticalLayout_21.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_guide)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-envelope-open.png);"
        )

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-print.png);"
        )

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(
            u"background-image: url(:/icons/images/icons/cil-account-logout.png);"
        )

        self.verticalLayout_14.addWidget(self.btn_logout)

        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.contentSettings)

        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setStyleSheet(
            u"background-color:#2f3b52; color: rgb(220, 242, 255)"
        )
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.bottomBar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(
            u"QProgressBar::chunk {background-color:#46a46e;width: 20px;}\n"
            "QProgressBar{\n"
            "color:black\n"
            "}"
        )
        self.progressBar.setValue(50)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout_5.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.horizontalLayout_5.addWidget(self.creditsLabel, 0, Qt.AlignRight)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.bottomBar)

        self.verticalLayout_2.addWidget(self.contentBottom)

        self.appLayout.addWidget(self.contentBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Montserrat'; font-size:10pt; font-weight:500; font-style:normal;\">\n"
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Arte</p></body></html>',
                None,
            )
        )
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_history.setText(
            QCoreApplication.translate("MainWindow", u"History", None)
        )
        self.btn_performance.setText(
            QCoreApplication.translate("MainWindow", u"Performance", None)
        )
        self.btn_guide.setText(
            QCoreApplication.translate("MainWindow", u"Guides", None)
        )
        self.btn_settings.setText(
            QCoreApplication.translate("MainWindow", u"Guides", None)
        )
        self.titleRightInfo.setText(
            QCoreApplication.translate(
                "MainWindow",
                u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Montserrat'; font-size:10pt; font-weight:500; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">mis</p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Settings", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Minimize", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Maximize", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Close", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.benchmark_label.setText(
            QCoreApplication.translate("MainWindow", u" Voltaic Benchmarks", None)
        )
        self.rank_label.setText(QCoreApplication.translate("MainWindow", u"Rank", None))
        self.benchRankBar_0.setFormat("")
        self.benchRankBar_1.setFormat("")
        self.benchRankBar_2.setFormat("")
        self.benchRankBar_3.setFormat("")
        self.benchRankBar_4.setFormat("")
        self.benchRankBar_5.setFormat("")
        self.benchRankBar_6.setFormat("")
        self.benchRankBar_7.setFormat("")
        self.benchRankBar_8.setFormat("")
        self.benchRankBar_9.setFormat("")
        self.benchRankBar_10.setFormat("")
        self.benchRankBar_11.setFormat("")
        self.benchRankBar_12.setFormat("")
        self.benchRankBar_13.setFormat("")
        self.benchRankBar_14.setFormat("")
        self.benchRankBar_15.setFormat("")
        self.benchRankBar_16.setFormat("")
        self.benchRankBar_17.setFormat("")
        self.lblBench_0.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_0.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_1.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_1.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_2.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_2.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_3.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_3.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_4.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_4.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_5.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_5.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_6.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_6.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_7.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_7.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_8.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_8.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_9.setText(QCoreApplication.translate("MainWindow", u"9999", None))
        self.indexLbl_9.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_10.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_10.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_11.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_11.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_12.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_12.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_13.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_13.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_14.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_14.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_15.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_15.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_16.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_16.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.lblBench_17.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.indexLbl_17.setText(
            QCoreApplication.translate("MainWindow", u"1wall6targets TE", None)
        )
        self.rb_ra_adv.setText(
            QCoreApplication.translate("MainWindow", u"rA - Advanced", None)
        )
        self.rb_ra_easy.setText(
            QCoreApplication.translate("MainWindow", u"rA - Easy", None)
        )
        self.btn_refreshPage.setText(
            QCoreApplication.translate("MainWindow", u"Refresh", None)
        )
        self.btn_directory.setText(
            QCoreApplication.translate("MainWindow", u"Change Directory", None)
        )
        self.rb_volt_adv.setText(
            QCoreApplication.translate("MainWindow", u"Voltaic - Advanced", None)
        )
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"Benchmarks", None)
        )
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.radioButton.setText(
            QCoreApplication.translate("MainWindow", u"Voltaic - Intermediate", None)
        )
        self.rb_custom.setText(
            QCoreApplication.translate("MainWindow", u"Custom", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"SELECT SCENARIO", None)
        )
        self.lblHighScore.setText(
            QCoreApplication.translate("MainWindow", u"99999", None)
        )
        self.lblAverageScore.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.lblAverageAcc.setText(
            QCoreApplication.translate("MainWindow", u"99999", None)
        )
        self.lblTotalPlayed.setText(
            QCoreApplication.translate("MainWindow", u"99999", None)
        )
        # if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"Generates a ARIMA model to help predict future performance.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.comboBox.setCurrentText("")
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"Total Attempts :", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Avg Score :", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"Best Acc :", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"High Score :", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"Trending :", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"Diff Avg Score :", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"Diff High Score :", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", u"Score :", None)
        )
        self.lblScore.setText(QCoreApplication.translate("MainWindow", u"99999", None))
        self.lblDiffAverageScore.setText(
            QCoreApplication.translate("MainWindow", u"9999", None)
        )
        self.lblDiffHighScore.setText(
            QCoreApplication.translate("MainWindow", u"99999", None)
        )
        self.lblTrending.setText(
            QCoreApplication.translate("MainWindow", u"99999", None)
        )
        self.label_57.setText(
            QCoreApplication.translate("MainWindow", u"Summary", None)
        )
        self.label_58.setText(
            QCoreApplication.translate("MainWindow", u"Last Attempt", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow", u"Smoothness & Precision Routine", None
            )
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Instructions", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u2981	Increase your sensitivity by 10-20% to make it faster\n"
                "\u2981	for instance if you play 30cm/360 change it to 24cm/360\n"
                "\u2981	Change your field of view to 80 ow\n"
                "\u2981	Put a dot crosshair",
                None,
            )
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"20-30 minutes | Increase sensitivity by 10-50% | 80 FOV (ow)",
                None,
            )
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"Thin Gauntlet", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", u"Bounce 180 tracking small invincible fixed", None
            )
        )
        self.label_17.setText(
            QCoreApplication.translate("MainWindow", u"Popcorn GTI", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow", u"Air no ufo no skybots small", None
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Generate Playlist", None)
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "MainWindow", u"Focus on being as smooth as possible", None
            )
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Focus on being against both horizontal and vertical angles",
                None,
            )
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Focus on being against both horizontal and vertical angles",
                None,
            )
        )
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow", u"Focus on being as smooth as possible", None
            )
        )
        self.btn_message.setText(
            QCoreApplication.translate("MainWindow", u"Message", None)
        )
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(
            QCoreApplication.translate("MainWindow", u"Logout", None)
        )
        self.creditsLabel.setText(
            QCoreApplication.translate("MainWindow", u"[Data To Show]", None)
        )
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))

    # retranslateUi
