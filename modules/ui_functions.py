"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""

from threading import Thread
from main import *


GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True


class UIFunctions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.main_ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.main_ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.main_ui.maximizeRestoreAppBtn.setIcon(
                QIcon(u":/icons/images/icons/icon_restore.png")
            )
            self.main_ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.main_ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.main_ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.main_ui.maximizeRestoreAppBtn.setIcon(
                QIcon(u":/icons/images/icons/icon_maximize.png")
            )
            self.main_ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def returStatus(self):
        return GLOBAL_STATE

    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def toggleMenu(self, enable):
        if enable:
            width = self.main_ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(
                self.main_ui.leftMenuBg, b"minimumWidth"
            )
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    def toggleLeftBox(self, enable):
        if enable:
            width = self.main_ui.extraLeftBox.width()
            widthRightBox = self.main_ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            style = self.main_ui.toggleLeftBox.styleSheet()

            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.main_ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.main_ui.settingsTopBtn.styleSheet()
                    self.main_ui.settingsTopBtn.setStyleSheet(
                        style.replace(Settings.BTN_RIGHT_BOX_COLOR, "")
                    )
            else:
                widthExtended = standard
                self.main_ui.toggleLeftBox.setStyleSheet(style.replace(color, ""))

        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.main_ui.extraRightBox.width()
            widthLeftBox = self.main_ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            style = self.main_ui.settingsTopBtn.styleSheet()

            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.main_ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.main_ui.toggleLeftBox.styleSheet()
                    self.main_ui.toggleLeftBox.setStyleSheet(
                        style.replace(Settings.BTN_LEFT_BOX_COLOR, "")
                    )
            else:
                widthExtended = standard
                self.main_ui.settingsTopBtn.setStyleSheet(style.replace(color, ""))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0

        self.left_box = QPropertyAnimation(self.main_ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        self.right_box = QPropertyAnimation(self.main_ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def selectStandardMenu(self, widget):
        for w in self.main_ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    def resetStyle(self, widget):
        for w in self.main_ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, "r").read()
            self.main_ui.styleSheet.setStyleSheet(str)

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        self.main_ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            def moveWindow(event):
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            self.main_ui.titleRightInfo.mouseMoveEvent = moveWindow

            self.main_ui.frame_size_grip.hide()

        else:
            self.main_ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.main_ui.minimizeAppBtn.hide()
            self.main_ui.maximizeRestoreAppBtn.hide()
            self.main_ui.frame_size_grip.hide()
            self.main_ui.closeAppBtn.hide()

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.main_ui.bgApp.setGraphicsEffect(self.shadow)

        self.sizegrip = QSizeGrip(self.main_ui.frame_size_grip)
        self.sizegrip.setStyleSheet(
            "width: 20px; height: 20px; margin 0px; padding: 0px;"
        )

        self.main_ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        self.main_ui.maximizeRestoreAppBtn.clicked.connect(
            lambda: UIFunctions.maximize_restore(self)
        )

        self.main_ui.closeAppBtn.clicked.connect(lambda: self.close())

    def show_main_cards(self):
        """Displays main dashboard graph cards."""
        self.main_ui.bench_frame_0.setVisible(True)
        self.main_ui.bench_frame_1.setVisible(True)
        self.main_ui.bench_frame_2.setVisible(True)
        self.main_ui.bench_frame_3.setVisible(True)
        self.main_ui.bench_frame_4.setVisible(True)
        self.main_ui.bench_frame_5.setVisible(True)
        self.main_ui.bench_frame_6.setVisible(True)
        self.main_ui.bench_frame_7.setVisible(True)
        self.main_ui.bench_frame_8.setVisible(True)
        self.main_ui.bench_frame_9.setVisible(True)
        self.main_ui.bench_frame_10.setVisible(True)
        self.main_ui.bench_frame_11.setVisible(True)
        self.main_ui.bench_frame_12.setVisible(True)
        self.main_ui.bench_frame_13.setVisible(True)
        self.main_ui.bench_frame_14.setVisible(True)
        self.main_ui.bench_frame_15.setVisible(True)
        self.main_ui.bench_frame_16.setVisible(True)
        self.main_ui.bench_frame_17.setVisible(True)
        self.main_ui.bench_frame_bars.setVisible(True)
        self.main_ui.progressBar_29.setVisible(True)
        self.main_ui.progressBar_30.setVisible(True)
        self.main_ui.progressBar_43.setVisible(True)

    def style_widgets(self):
        """Styles visibility of WIDGETS."""

        self.main_ui.settingsTopBtn.setVisible(False)
        self.main_ui.maximizeRestoreAppBtn.setVisible(False)
        self.main_ui.btn_guide.setVisible(False)

        self.main_ui.bench_frame_0.setVisible(False)
        self.main_ui.bench_frame_1.setVisible(False)
        self.main_ui.bench_frame_2.setVisible(False)
        self.main_ui.bench_frame_3.setVisible(False)
        self.main_ui.bench_frame_4.setVisible(False)
        self.main_ui.bench_frame_5.setVisible(False)
        self.main_ui.bench_frame_6.setVisible(False)
        self.main_ui.bench_frame_7.setVisible(False)
        self.main_ui.bench_frame_8.setVisible(False)
        self.main_ui.bench_frame_9.setVisible(False)
        self.main_ui.bench_frame_10.setVisible(False)
        self.main_ui.bench_frame_11.setVisible(False)
        self.main_ui.bench_frame_12.setVisible(False)
        self.main_ui.bench_frame_13.setVisible(False)
        self.main_ui.bench_frame_14.setVisible(False)
        self.main_ui.bench_frame_15.setVisible(False)
        self.main_ui.bench_frame_16.setVisible(False)
        self.main_ui.bench_frame_17.setVisible(False)
        self.main_ui.bench_frame_bars.setVisible(False)
        self.main_ui.progressBar_29.setVisible(False)
        self.main_ui.progressBar_30.setVisible(False)
        self.main_ui.progressBar_43.setVisible(False)
        # Side Rank bars

        self.main_ui.progressBar_31.setVisible(False)
        self.main_ui.progressBar_32.setVisible(False)
        self.main_ui.progressBar_33.setVisible(False)
        self.main_ui.progressBar_34.setVisible(False)
        self.main_ui.progressBar_35.setVisible(False)
        self.main_ui.progressBar_36.setVisible(False)
        self.main_ui.progressBar_37.setVisible(False)
        self.main_ui.progressBar_38.setVisible(False)
        self.main_ui.progressBar_39.setVisible(False)
        self.main_ui.progressBar_40.setVisible(False)
        self.main_ui.progressBar_41.setVisible(False)
        self.main_ui.progressBar_42.setVisible(False)
        self.main_ui.progressBar_47.setVisible(False)
        self.main_ui.progressBar_51.setVisible(False)
        self.main_ui.progressBar_52.setVisible(False)
        self.main_ui.progressBar_53.setVisible(False)
        self.main_ui.progressBar_54.setVisible(False)
        self.main_ui.progressBar_55.setVisible(False)

        self.main_ui.label_2.setVisible(False)
        self.main_ui.label_3.setVisible(False)
        self.main_ui.label_4.setVisible(False)
        self.main_ui.label_5.setVisible(False)
        self.main_ui.label_11.setVisible(False)
        self.main_ui.label_12.setVisible(False)
        self.main_ui.label_13.setVisible(False)
        self.main_ui.label_14.setVisible(False)
        self.main_ui.label_57.setVisible(False)
        self.main_ui.label_58.setVisible(False)
        self.main_ui.lblHighScore.setVisible(False)
        self.main_ui.lblAverageScore.setVisible(False)
        self.main_ui.lblAverageAcc.setVisible(False)
        self.main_ui.lblTotalPlayed.setVisible(False)
        self.main_ui.lblScore.setVisible(False)
        self.main_ui.lblDiffAverageScore.setVisible(False)
        self.main_ui.lblDiffHighScore.setVisible(False)
        self.main_ui.lblTrending.setVisible(False)
        self.main_ui.pushButton.setVisible(False)

        self.main_ui.lineGraphHistoryView.setBackground(None)
        self.main_ui.lineGraphHistoryView.enableAutoRange(True)
        self.main_ui.lineGraphHistoryView.setMouseEnabled(False, False)

        self.main_ui.barGraphHistoryView.setBackground(None)
        self.main_ui.barGraphHistoryView.enableAutoRange(True)
        self.main_ui.barGraphHistoryView.setMouseEnabled(False, False)

        self.main_ui.lineGraphHistoryView.setHidden(True)
        self.main_ui.barGraphHistoryView.setHidden(True)

        plotitem = self.main_ui.lineGraphHistoryView.getPlotItem()
        plotitem.setLabels(left="Score", bottom="Last 10 Attempts")
        plotitem.showGrid(x=True, y=True)
        plotitem.getAxis("left").setPen("#d7e5e4")
        plotitem.getAxis("bottom").setPen("#d7e5e4")

        plotitem.getAxis("left").setTextPen("#d7e5e4")
        plotitem.getAxis("bottom").setTextPen("#d7e5e4")

        plotitem = self.main_ui.barGraphHistoryView.getPlotItem()
        plotitem.showGrid(x=True, y=True)

        plotitem.getAxis("left").setPen("#d7e5e4")
        plotitem.getAxis("bottom").setPen("#d7e5e4")

        plotitem.getAxis("left").setTextPen("#252e42")
        plotitem.hideAxis("bottom")

        self.main_ui.treeView.setFrameShape(QFrame.NoFrame)
        self.main_ui.creditsLabel.setText("")

        self.main_ui.progressBar.setVisible(False)
