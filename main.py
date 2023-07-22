"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""
import logging

logging.basicConfig(filename="log.log", level=logging.INFO)
import datetime as dt
import glob
import itertools
import os
import re
import sys
import threading
import warnings
from collections import defaultdict

import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyqtgraph as pg
import statsmodels.api as sm
from pyqtgraph import PlotWidget
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from statsmodels.tsa.arima_model import ARIMA
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from modules import benchmarks as bchm
from modules import csv_util as cu
from modules import utility as util
from modules import *

mpl.rcParams["toolbar"] = "None"
STAT_FILE_RE = re.compile(r"(?P<name>.+) - Challenge - (?P<date>.+) Stats\.csv")

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

threadSignals = util.ThreadSignals()


class MainWindow(QMainWindow):
    """Main window of application

    Args:
        QMainWindow (QMainWindow): Main window from pyside6 library.
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        global WIDGETS
        WIDGETS = self.main_ui
        self.version = "v1.1.3"
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        title = "Artemis"
        WIDGETS.version.setText(self.version)
        self.setWindowTitle(title)

        self._connect_ui()

        UIFunctions.uiDefinitions(self)

        self.show()

        UIFunctions.style_widgets(self)

        self.selected_benchmark = -5
        self.all_maps = []
        self.table_entries = []
        self.saved_files = []
        self.dataframe = None
        self.stats_directory = None
        self.files_by_challenge = defaultdict(list)
        self.file_name = []
        self.event_handler = MonitorFolder()
        self.observer = Observer()

        if os.path.exists("saved_data"):
            (
                self.all_maps,
                self.table_entries,
                self.saved_files,
                self.stats_directory,
                self.selected_benchmark,
            ) = util.Load()

            self.observer.schedule(
                self.event_handler, path=self.stats_directory, recursive=True
            )

        self._set_benchmark(self.selected_benchmark)

        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.setIcon(QMessageBox.Warning)

        theme_file = "themes\\py_artemis.qss"
        UIFunctions.theme(self, theme_file, True)
        AppFunctions.set_theme_hack(self)

        WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.home)
        WIDGETS.btn_home.setStyleSheet(
            UIFunctions.selectMenu(WIDGETS.btn_home.styleSheet())
        )

        self.observer.start()

    def _button_click(self):
        """Method called on button click event."""
        btn = self.sender()
        btn_name = btn.objectName()
        print("BUTTON HIT:", btn_name)

        if btn_name == "btn_home":
            WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.home)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btn_name == "btn_history":
            WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.page_history)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btn_name == "btn_performance":
            WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.page_performance)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btn_name == "btn_guide":
            WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.page_guide)
            UIFunctions.resetStyle(self, btn_name)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btn_name == "btn_directory":
            self._update_data_directory()

        if btn_name == "btn_about":
            about = QMessageBox()
            about.about(
                self,
                "About",
                "Application by: Nstalgic",
            )

        # Does nothing
        if btn_name == "btn_save":
            print("Save BTN clicked!")

        if btn_name == "btn_refreshPage":
            self.load_data()
            print("refresh BTN clicked!")

        if btn_name == "btn_settings":
            WIDGETS.stackedWidget.setCurrentWidget(WIDGETS.settings)

        # PRINT BTN NAME
        print(f'Button "{btn_name}" pressed!')

    def mousePressEvent(self, event):
        """Handles mouse press event

        Args:
            event (click): mouse click
        """
        self.dragPos = event.globalPos()

        if event.buttons() == Qt.LeftButton:
            print("Mouse click: LEFT CLICK")
        if event.buttons() == Qt.RightButton:
            print("Mouse click: RIGHT CLICK")

    def _update_data_directory(self):
        """Prompts user to select a new file directory."""
        new_stats_directory = QtWidgets.QFileDialog.getExistingDirectory()

        if new_stats_directory:
            self._clear_data()
            self.stats_directory = new_stats_directory
            self.path = self.stats_directory + "\\*.csv"

            self.observer.schedule(
                self.event_handler, path=self.stats_directory, recursive=True
            )

            x = threading.Thread(target=self.load_data, daemon=True)

            x.start()

    def load_data(self):
        """Loads CSV files from selected file directory.

        Returns:
        Dataframe: A formated dataframe based on the provided list.

        """
        if not self.stats_directory:
            self.stats_directory = QtWidgets.QFileDialog.getExistingDirectory()

        while self.stats_directory == "":
            self.stats_directory = QtWidgets.QFileDialog.getExistingDirectory()

        self.path = os.path.join(self.stats_directory, "*.csv")

        for file in glob.glob(self.path):
            self.file_name.append(file.split("\\")[1])

        max_files = len(os.listdir(self.stats_directory))

        threadSignals.update_progressbar_range.emit(0, max_files)

        for fname in self.file_name:
            m = STAT_FILE_RE.match(fname)
            if not m:
                continue
            self.files_by_challenge[m.group("name")].append(fname)
        for file in glob.glob(self.path):

            threadSignals.show_progress_bar.emit(True)
            threadSignals.update_progressbar_value.emit(WIDGETS.progressBar.value() + 1)

            if file not in self.saved_files:
                try:

                    to_append = self._parse_files(file)
                    self.table_entries.append(to_append)
                    print(f"New File Saved: {file}")

                except AttributeError as msg:
                    logging.error(
                        f"LoadError(AttributeError) - File: {file} - Message: {msg}"
                    )
                    continue
                except ValueError as msg:
                    logging.error(
                        f"LoadError(ValueError) - File: {file} - Message: {msg}"
                    )
                    continue

        util.Save(
            self.all_maps,
            self.table_entries,
            self.saved_files,
            self.stats_directory,
            self.selected_benchmark,
        )

        if self.saved_files:
            threadSignals.finish_loading_home.emit()

    def _update_benchmark_bars(self, is_single=False):
        """Updates all or a single scenario benchmark.

        Args:
            is_single (bool, optional): Option to update a single benchmark. Defaults to False.
        """
        data = self.benchmark_list

        tier_keys = list(data.keys())

        scenario_names = data[tier_keys[0]]
        tier_1_scores = data[tier_keys[1]]
        tier_2_scores = data[tier_keys[2]]
        tier_3_scores = data[tier_keys[3]]
        tier_4_scores = data[tier_keys[4]]
        tier_5_scores = data[tier_keys[5]]
        i = None
        scenario_tiers = []

        if self.selected_benchmark == -3 or self.selected_benchmark == -2:
            benchmark_class = bchm.Revosect
            is_adv = self.selected_benchmark == -2
        else:
            benchmark_class = bchm.Voltaic
            is_adv = self.selected_benchmark == -4

        if is_single:
            new_scenario = self.dataframe["Scenario"].iloc[0]
            if new_scenario in scenario_names:
                i = scenario_names.index(new_scenario)
                scenario_names = [new_scenario]

        for scenario in scenario_names:

            if not is_single:
                i = scenario_names.index(scenario)

            bar_name = "benchBar_" + str(i)
            bar_tier = "benchRankBar_" + str(i)
            bench_bar = WIDGETS.home.findChild(QProgressBar, bar_name)
            bench_tier = WIDGETS.home.findChild(QProgressBar, bar_tier)
            bench_bar.setVisible(True)
            bench_tier.setVisible(True)
            bench_bar.setValue(0)
            df = self.dataframe.loc[self.dataframe["Scenario"] == scenario]
            if str(df["Score"].max()) != "nan":
                bench_bar.reset()
                bench_bar.setFormat(scenario)
                max_score = df["High Score"].max()

                if max_score >= tier_5_scores[i]:
                    bench_bar.setMaximum(max_score)
                    bench_bar.setMinimum(0)
                    tier_rank = 5
                elif max_score >= tier_4_scores[i]:
                    bench_bar.setMaximum(tier_5_scores[i])
                    bench_bar.setMinimum(tier_4_scores[i])
                    tier_rank = 4
                elif max_score >= tier_3_scores[i]:
                    bench_bar.setMaximum(tier_4_scores[i])
                    bench_bar.setMinimum(tier_3_scores[i])
                    tier_rank = 3
                elif max_score >= tier_2_scores[i]:
                    bench_bar.setMaximum(tier_3_scores[i])
                    bench_bar.setMinimum(tier_2_scores[i])
                    tier_rank = 2
                elif max_score >= tier_1_scores[i]:
                    bench_bar.setMaximum(tier_2_scores[i])
                    bench_bar.setMinimum(tier_1_scores[i])
                    tier_rank = 1
                else:
                    bench_bar.setMaximum(tier_1_scores[i])
                    bench_bar.setMinimum(0)
                    tier_rank = 0

                tier_color, bar_color = benchmark_class.get_color_codes(
                    tier_rank, is_adv=is_adv
                )

                bench_bar.setValue(max_score)
                bench_bar.setStyleSheet(
                    "QProgressBar::chunk"
                    "{"
                    f"background-color : {bar_color};"
                    "border :1px solid black;"
                    "}"
                    "QProgressBar"
                    "{"
                    "color: black;"
                    "}"
                )

                bench_tier.setStyleSheet(
                    "QProgressBar::chunk"
                    "{"
                    f"background-color : {tier_color};"
                    "border :1px solid black;"
                    "}"
                )

                scenario_tiers.append(tier_rank)
            else:
                bench_bar.setVisible(False)
                bench_tier.setVisible(False)

        if not is_single:
            self._find_ranking(scenario_tiers)

    def generate_arima(self):
        """Generates a graph presenting 'Auto Regressive Integrated Moving Average'."""
        scenario_name = str(WIDGETS.comboBox.currentText())

        df = self.dataframe.loc[self.dataframe["Scenario"] == scenario_name]
        df = df.sort_values(by="Date")

        df = df[["Date", "Score"]]
        df["Date"] = df["Date"].map(dt.datetime.toordinal)

        df = df.set_index("Date")
        # Define the p, d and q parameters to take any value between 0 and 3
        p = d = q = range(0, 3)
        # Generate all different combinations of p, q and q
        pdq = list(itertools.product(p, d, q))

        warnings.filterwarnings("ignore")
        aic = []
        parameters = []
        WIDGETS.progressBar.reset()
        threadSignals.update_progressbar_range.emit(0, len(pdq))
        try:
            for param in pdq:
                # for param in pdq:
                threadSignals.show_progress_bar.emit(True)
                threadSignals.update_progressbar_value.emit(
                    WIDGETS.progressBar.value() + 1
                )
                try:
                    mod = sm.tsa.statespace.SARIMAX(
                        df,
                        order=param,
                        enforce_stationarity=True,
                        enforce_invertibility=True,
                    )

                    results = mod.fit(disp=0)
                    # save results in lists
                    aic.append(results.aic)
                    parameters.append(param)
                except Exception:
                    continue
                    # find lowest aic
            index_min = min(range(len(aic)), key=aic.__getitem__)
            threadSignals.show_progress_bar.emit(False)
            # try:
            model = ARIMA(df, order=parameters[index_min])
            model_fit = model.fit(disp=0)
            model_fit.plot_predict(start=2, end=len(df) + 12)

            plt.legend(["Score Forecast", "Current Score", "95% Confidence Interval"])

            self._style_graph(scenario_name)

            plt.show()

        except Exception as e:
            self.msg.setText(str(e))
            self.msg.show()

    def _plot_data(self):
        """Plots refind data to graph."""
        WIDGETS.lineGraphHistoryView.setHidden(False)
        WIDGETS.barGraphHistoryView.setHidden(False)
        WIDGETS.lineGraphHistoryView.clear()
        WIDGETS.barGraphHistoryView.clear()

        if WIDGETS.comboBox.currentText():

            scenario_name = WIDGETS.comboBox.currentText()

            df = self.dataframe.loc[self.dataframe["Scenario"] == scenario_name]

            df = df.sort_values(by="Date")
            df["Acc."] = df["Acc."].apply(pd.to_numeric)
            scenario_count = df.shape[0]

            WIDGETS.barGraphHistoryView.plot(
                y=df["Score"].values, pen=pg.mkPen("#d7e5e4", width=1)
            )

            df = df.tail(10)

            WIDGETS.lineGraphHistoryView.plot(
                y=df["Score"].values, pen=pg.mkPen("#d7e5e4", width=4), symbol="o"
            )

            max_acc = df["Acc."].max()

            last_item = df.tail(1)

            diff_high_score = str(last_item["Diff High Score"].max())
            diff_avg_score = str(last_item["Diff Avg Score"].max())

            WIDGETS.lblDiffAverageScore.setText(diff_avg_score)
            WIDGETS.lblScore.setText(str(last_item["Score"].max()))
            WIDGETS.lblHighScore.setText(str(df["Score"].max()))
            WIDGETS.lblAverageScore.setText(str(round(df["Score"].mean())))

            red_value = "color:#da8fa5"
            green_value = "color:#33c191"

            WIDGETS.lblDiffHighScore.setText(diff_high_score)
            WIDGETS.lblDiffAverageScore.setText(diff_avg_score)
            WIDGETS.lblDiffAverageScore.setStyleSheet(red_value)
            WIDGETS.lblDiffHighScore.setStyleSheet(red_value)

            if diff_high_score == "0.0%":
                WIDGETS.lblDiffHighScore.setText("HIGH SCORE")
                WIDGETS.lblDiffHighScore.setStyleSheet("color:#dda01e")

            if diff_avg_score[0] == "+":
                WIDGETS.lblDiffAverageScore.setStyleSheet(green_value)

            if max_acc:
                WIDGETS.lblAverageAcc.setText(str(df["Acc."].max()))
            else:
                WIDGETS.lblAverageAcc.setText("No Data")

            WIDGETS.lblTotalPlayed.setText(str(scenario_count))

            self._show_information()

    def _show_information(self):
        """Enables label visability."""
        WIDGETS.label_2.setVisible(True)
        WIDGETS.label_3.setVisible(True)
        WIDGETS.label_4.setVisible(True)
        WIDGETS.label_5.setVisible(True)
        WIDGETS.label_11.setVisible(True)
        WIDGETS.label_12.setVisible(True)
        WIDGETS.label_13.setVisible(True)
        WIDGETS.label_14.setVisible(True)
        WIDGETS.label_57.setVisible(True)
        WIDGETS.label_58.setVisible(True)
        WIDGETS.lblScore.setVisible(True)
        WIDGETS.lblDiffAverageScore.setVisible(True)
        WIDGETS.lblDiffHighScore.setVisible(True)
        WIDGETS.lblTrending.setVisible(True)
        WIDGETS.lblHighScore.setVisible(True)
        WIDGETS.lblAverageScore.setVisible(True)
        WIDGETS.lblAverageAcc.setVisible(True)
        WIDGETS.lblTotalPlayed.setVisible(True)

        WIDGETS.lblTrending.setText("")
        WIDGETS.label_11.setText("")
        df = self.dataframe.loc[
            self.dataframe["Scenario"] == str(WIDGETS.comboBox.currentText())
        ]

        scenario_count = len(df)

        # if scenario_count >= 30:
        if False:
            WIDGETS.pushButton.setVisible(True)
        else:
            WIDGETS.pushButton.setVisible(False)

    def _create_dataframe(self):
        """Generate a data frame object from table_entries attribute."""
        columns = [
            "Date",
            "Scenario",
            "Score",
            "Kills",
            "Acc.",
            "Avg Score",
            "High Score",
            "Diff Avg Score",
            "Diff High Score",
        ]
        if self.table_entries:
            df = pd.DataFrame(np.array(self.table_entries), columns=columns)
            df = df.sort_values(by="Date", ascending=False)
            # Corrects datatypes in Dataframe
            df[["Date"]] = df[["Date"]].apply(pd.to_datetime)
            df[["Score"]] = df[["Score"]].apply(pd.to_numeric)
            df[["Avg Score"]] = df[["Avg Score"]].apply(pd.to_numeric)
            df[["High Score"]] = df[["High Score"]].apply(pd.to_numeric)

            self.dataframe = df
            self._update_benchmark_bars()
            self._setup_homepage()

    def _style_graph(self, scenario_name: str):
        """Applies styling to specfic graphs.

        Args:
            scenario_name (str): name of the selected scenario.
        """
        ax = plt.gca()
        ax.set_facecolor("#4873A5")
        ax.get_legend().legendHandles[0].set_color("#dda01e")
        ax.get_legend().legendHandles[1].set_color("#e6f4f1")
        ax.get_legend().get_frame().set_facecolor("#A6E1Fa")

        plt.gca().get_lines()[0].set_color("#dda01e")
        plt.gca().get_lines()[1].set_color("#e6f4f1")

        plt.title(scenario_name)

        manager = plt.get_current_fig_manager()

        manager.window.wm_iconbitmap("icon.ico")
        manager.set_window_title(scenario_name)

        plt.grid()

    def _setup_homepage(self):
        """Inital Homepage call"""
        data = self.benchmark_list

        scenario_names = data["Scenario"]
        self._populate_widgets(scenario_names)

    def _populate_widgets(self, scenario_names: str):
        """Populates main dashboard card with correct data.

        Args:
            scenario_names (str): name of the selected scenario.
        """
        for i, scenario in enumerate(scenario_names):

            df = self.dataframe.loc[self.dataframe["Scenario"] == scenario]

            df = df.sort_values(by="Date")
            df = df.tail(10)

            lbl_scen = "indexLbl_" + str(i)
            lbl_score = "lblBench_" + str(i)
            graph_name = "graphWidget_" + str(i)
            plot_widget = "pltWidget_" + str(i)

            title = WIDGETS.home.findChild(QLabel, lbl_scen)
            score = WIDGETS.home.findChild(QLabel, lbl_score)
            graph = WIDGETS.home.findChild(QWidget, graph_name)
            home_graph = WIDGETS.home.findChild(PlotWidget, plot_widget)
            title.setText(scenario)
            title.setStyleSheet("background-color:#315e73")

            if str(df["Score"].max()) != "nan":
                score.setText(str(df["High Score"].max()))
                if not home_graph:
                    home_graph = pg.PlotWidget()
                    home_graph.setObjectName(plot_widget)
                    home_graph.setBackground(None)
                    home_graph.enableAutoRange(True)
                    home_graph.setMouseEnabled(False, False)
                    plot_item = home_graph.getPlotItem()
                    plot_item.hideAxis("bottom")
                    plot_item.hideAxis("left")
                    layout = QtWidgets.QVBoxLayout()
                    layout.addWidget(home_graph)
                    # getting widget from code.
                    graph.setLayout(layout)

                home_graph.clear()
                home_graph.plot(y=df["Score"].values, pen=pg.mkPen("#d7e5e4", width=2))

            else:
                score.setText("No Data")
                if home_graph:
                    home_graph.clear()

    def _connect_ui(self):
        """Connects ui signals and slots."""
        WIDGETS.btn_home.clicked.connect(self._button_click)
        WIDGETS.btn_history.clicked.connect(self._button_click)
        WIDGETS.btn_performance.clicked.connect(self._button_click)
        WIDGETS.btn_guide.clicked.connect(self._button_click)
        WIDGETS.btn_directory.clicked.connect(self._button_click)
        WIDGETS.btn_about.clicked.connect(self._button_click)
        WIDGETS.btn_refreshPage.clicked.connect(self._button_click)
        WIDGETS.btn_settings.clicked.connect(self._button_click)
        WIDGETS.buttonGroup.buttonClicked.connect(self._setting_benchmark)

        threadSignals.update_data.connect(self._update_data)
        threadSignals.update_progressbar_range.connect(self._update_progressbar_range)
        threadSignals.update_progressbar_value.connect(self._update_progressbar)
        threadSignals.show_progress_bar.connect(self._update_progressbar_visibility)
        threadSignals.finish_loading_home.connect(self._launch)

        WIDGETS.pushButton.clicked.connect(lambda: window.generate_arima())
        WIDGETS.comboBox.currentIndexChanged.connect(lambda: self._plot_data())

    def _clear_data(self):
        """Clears all saved variables"""
        self.all_maps = []
        self.table_entries = []
        self.saved_files = []
        self.dataframe = None
        self.stats_directory = None
        self.files_by_challenge = defaultdict(list)
        self.file_name = []
        WIDGETS.comboBox.clear()

    def _update_pages(self):
        """updates all application pages with the update dataframe."""
        model = util.pandasModel(self.dataframe)
        map_names = list(self.dataframe["Scenario"].unique())
        map_names.sort()
        WIDGETS.comboBox.clear()
        WIDGETS.comboBox.addItems(map_names)
        WIDGETS.treeView.setModel(model)

    def _update_data(self, directory: str):
        """Adds a single new entry to the existing dataframe based on its directory.

        Args:
            directory (str): absolute location of csv file.
        """

        file_name = directory.split("\\")[-1]
        m = STAT_FILE_RE.match(file_name)

        if m:
            if file_name not in self.saved_files:
                try:
                    to_append = self._parse_files(directory)

                    a_series = pd.Series(to_append, index=self.dataframe.columns)
                    self.dataframe = self.dataframe.append(a_series, ignore_index=True)

                    self.dataframe[["Date"]] = self.dataframe[["Date"]].apply(
                        pd.to_datetime
                    )
                    self.dataframe[["Score"]] = self.dataframe[["Score"]].apply(
                        pd.to_numeric
                    )
                    self.dataframe[["Avg Score"]] = self.dataframe[["Avg Score"]].apply(
                        pd.to_numeric
                    )
                    self.dataframe[["High Score"]] = self.dataframe[
                        ["High Score"]
                    ].apply(pd.to_numeric)

                    self.dataframe = self.dataframe.sort_values(
                        by="Date", ascending=False
                    )

                    self.table_entries.append(to_append)
                    self.file_name.append(file_name)
                    self.saved_files.append(file_name)
                    self.files_by_challenge[m.group("name")].append(file_name)

                    util.Save(
                        self.all_maps,
                        self.table_entries,
                        self.saved_files,
                        self.stats_directory,
                        self.selected_benchmark,
                    )
                    WIDGETS.creditsLabel.setText(
                        f"Latest Scenario: {to_append[1]} | Score: {to_append[2]}"
                    )
                    self._update_pages()
                    self._setup_homepage()
                    self._update_header()

                    if self._is_tracked():
                        self._update_benchmark_bars(True)
                except Exception as msg:
                    logging.error(f"UpdateError - File: {file_name} - Message: {msg}")

    def _parse_files(self, directory: str) -> list:
        """Parses a csv file and loads the data into a list.

        Args:
            directory (str): absolute location of csv file.

        Returns:
            list: a list containing date, name, score, kills, accuracy,
            average, highscore, % difference from average, and % different from high score.
        """
        name = cu.get_map_name(directory)

        scenario_scores = cu.get_map_score(
            name, self.files_by_challenge, self.stats_directory
        )

        self.all_maps.append(name)
        session = cu.SessionStat.from_file(directory)
        score = session.summary.score
        kills = session.summary[0]
        date = str(session.date)
        accuracy = round(session.accuracy * 100)
        average = np.average(scenario_scores)
        average = np.nan_to_num(average)
        high_score = np.amax(scenario_scores)

        a = pd.Series([average, score])
        h = pd.Series([high_score, score])

        d_average = a.pct_change()
        d_high_score = h.pct_change()

        s_average = d_average[1]
        s_high_score = d_high_score[1]
        s_average = round(s_average * 100, 2)
        s_high_score = round(s_high_score * 100, 2)

        if kills == 0:
            kills = ""

        if s_average > 0:
            s_average = "+" + str(s_average)

        if s_high_score > 0:
            s_high_score = "+" + str(s_high_score)

        self.saved_files.append(directory)
        return [
            date,
            name,
            round(score, 1),
            kills,
            accuracy,
            round(average, 1),
            round(high_score, 1),
            str(s_average) + "%",
            str(s_high_score) + "%",
        ]

    def _update_header(self):
        """Updates headers of main dashboard with a white border"""
        data = self.benchmark_list
        scenario_names = data["Scenario"]
        replace = self.dataframe["Scenario"].iloc[0]
        to_replace = self.dataframe["Scenario"].iloc[1]

        if replace in scenario_names:
            lbl_new_highlight = "indexLbl_" + str(scenario_names.index(replace))
            title = WIDGETS.home.findChild(QLabel, lbl_new_highlight)
            title.setStyleSheet("border :2px solid White; background-color: #4873a4")

        if to_replace != replace:
            if to_replace in scenario_names:
                lbl_old_highlight = "indexLbl_" + str(scenario_names.index(to_replace))
                title = WIDGETS.home.findChild(QLabel, lbl_old_highlight)
                title.setStyleSheet("background-color:#315e73")

    def _update_progressbar(self, value: int):
        """Updates progress bar value provided by an emit.

        Args:
            value (int): new value of the progress bar
        """
        WIDGETS.progressBar.setValue(value)

    def _update_progressbar_range(self, min_value: int, max_value: int):
        """Updates the range of a progress bar provided by an emit.

        Args:
            min_value (int): Min value of the progress bar
            max_value (int): Max value fo the progress bar
        """
        WIDGETS.progressBar.setMinimum(min_value)
        WIDGETS.progressBar.setMaximum(max_value)

    def _update_progressbar_visibility(self, is_shown: bool):
        """Toggles visability of progress bar.

        Args:
            is_shown (bool): True to display; False to hide.
        """
        WIDGETS.progressBar.setVisible(is_shown)

    def _set_benchmark(self, selected_id: int):
        """Sets which benchmark values to use for the application

        Args:
            selected_id (int): index of the selected radio button on the settings page.
        """
        if selected_id == -5:
            self.benchmark_list = bchm.Voltaic().get_voltaic_data_int(dict=True)
            WIDGETS.benchmark_label.setText("Voltaic Intermediate")
        elif selected_id == -4:
            self.benchmark_list = bchm.Voltaic().get_voltaic_data_adv(dict=True)
            WIDGETS.benchmark_label.setText("Voltaic Advanced")
        elif selected_id == -3:
            self.benchmark_list = bchm.Revosect().get_revosect_data_int(dict=True)
            WIDGETS.benchmark_label.setText("Revosect Easy")
        elif selected_id == -2:
            self.benchmark_list = bchm.Revosect().get_revosect_data_adv(dict=True)
            WIDGETS.benchmark_label.setText("Revosect Advanced")

        WIDGETS.buttonGroup.button(selected_id).setChecked(True)

    def _setting_benchmark(self):
        """Updates and saves user preferences."""
        index_selection = WIDGETS.buttonGroup.checkedId()

        self.selected_benchmark = index_selection
        self._set_benchmark(index_selection)
        self._update_benchmark_bars()
        self._setup_homepage()
        self._update_header()

        util.Save(
            self.all_maps,
            self.table_entries,
            self.saved_files,
            self.stats_directory,
            self.selected_benchmark,
        )

    def _find_ranking(self, scen_list: list):
        """Finds the current rank based on benchmark specifications.

        Args:
            scen_list (list): list containing the names of benchmark scenarios
        """
        list_of_tiers = scen_list
        if list_of_tiers is not None:

            dynamic_list = list_of_tiers[:3]
            static_list = list_of_tiers[3:6]
            precise_list = list_of_tiers[6:9]
            reactive_list = list_of_tiers[9:12]
            speed_list = list_of_tiers[12:15]
            evasive_list = list_of_tiers[15:18]

            dynamic_max_value = 0
            static_max_value = 0
            precise_max_value = 0
            reactive_max_value = 0
            speed_max_value = 0
            evasive_max_value = 0

            if len(dynamic_list) > 0:
                dynamic_max_value = max(dynamic_list)
            if len(static_list) > 0:
                static_max_value = max(static_list)
            if len(precise_list) > 0:
                precise_max_value = max(precise_list)
            if len(reactive_list) > 0:
                reactive_max_value = max(reactive_list)
            if len(speed_list) > 0:
                speed_max_value = max(speed_list)
            if len(evasive_list) > 0:
                evasive_max_value = max(evasive_list)

            tier = (
                dynamic_max_value
                + static_max_value
                + precise_max_value
                + reactive_max_value
                + speed_max_value
                + evasive_max_value
            )

            if self.selected_benchmark == -5:
                tier_name = bchm.find_volt_rank_int(tier)
            elif self.selected_benchmark == -4:
                tier_name = bchm.find_volt_rank_adv(tier)
            elif self.selected_benchmark == -3:
                tier_name = bchm.find_ra_rank_easy(tier)
            elif self.selected_benchmark == -2:
                tier_name = bchm.find_ra_rank_adv(tier)
            elif self.selected_benchmark == -6:
                tier_name = bchm.find_volt_rank_int(tier)

            WIDGETS.rank_label.setText(tier_name)

    def _is_tracked(self) -> bool:
        data = self.benchmark_list
        tier_keys = list(data.keys())
        scenario_names = data[tier_keys[0]]
        new_scenario = self.dataframe["Scenario"].iloc[0]

        return new_scenario in scenario_names

    def version_check(self):
        response = requests.get(
            "https://api.github.com/repos/nstalgic/artemis/releases/latest"
        )

        try:
            git_version = response.json()["tag_name"]

            if git_version != self.version:
                msg_box = QMessageBox()
                msg_box.setWindowIcon(QIcon("icon.ico"))
                msg_box.setWindowTitle("Update")
                msg_box.setText(
                    "An update is available at:\nhttps://github.com/Nstalgic/Artemis"
                )
                msg_box.exec_()
        except:
            response.close()

    def _launch(self):
        """Launches creation of applications pages."""
        WIDGETS.progressBar.setVisible(False)
        WIDGETS.rb_custom.setEnabled(False)
        self._create_dataframe()
        self._update_pages()
        UIFunctions.show_main_cards(self)


class MonitorFolder(FileSystemEventHandler):
    """Monitors select folder for file create events.

    Args:
        FileSystemEventHandler (FileSystemEventHandler): File system event handler
    """

    def on_created(self, event):
        """On create event.

        Args:
            event (create event): File creation detected.
        """
        print(event.src_path, event.event_type)
        threadSignals.update_data.emit(event.src_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    if os.path.exists("saved_data"):
        window.load_data()

    WIDGETS.treeView.resizeColumnToContents(0)
    WIDGETS.treeView.resizeColumnToContents(1)
    window.version_check()
    sys.exit(app.exec())
