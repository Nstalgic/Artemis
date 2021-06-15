"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""
import pickle
import re
from PySide6.QtCore import QObject, QAbstractTableModel, Qt, Signal

saved_file = "saved_data"
STAT_FILE_RE = re.compile(r"(?P<name>.+) - Challenge - (?P<date>.+) Stats\.csv")


def Save(
    all_maps: list,
    table_entries: list,
    saved_files: list,
    stats_directory: str,
    benchmark_selection: int,
):
    """Saves application variables in 'saved_data' file.

    Args:
        all_maps (list): list of all maps saved.
        table_entries (list): list of table entries.
        saved_files (list): list of processed files.
        stats_directory (str): directory of stats files.
        benchmark_selection (int): integer of selected combo box.
    """

    outfile = open(saved_file, "wb")
    save_data = [
        all_maps,
        table_entries,
        saved_files,
        stats_directory,
        benchmark_selection,
    ]

    pickle.dump(save_data, outfile)


def Load():
    """Returns the contents of 'saved_data' ZipFile The class for reading and writing ZIP files.  See section

    Returns:
        list, list, list, str, int:  Returns saved variables: all_maps, table_entries, saved_files, stats_directory, benchmark_selection
    """

    infile = open(saved_file, "rb")
    out_list = pickle.load(infile)

    # Map names, Table data, saved file names
    return out_list[0], out_list[1], out_list[2], out_list[3], out_list[4]


class pandasModel(QAbstractTableModel):
    """Model of a pandas dataframedatetime A combination of a date and a time. Attributes: ()

    Args:
        QAbstractTableModel (object): table model.
    """

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class ThreadSignals(QObject):
    """Thread signals object.

    Args:
        QObject (QObject): QObject
    """

    update_data = Signal(str)

    update_progressbar_range = Signal(int, int)
    update_progressbar_value = Signal(int)

    show_progress_bar = Signal(bool)

    finish_loading_home = Signal()
