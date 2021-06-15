"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""
from collections import defaultdict, namedtuple
import csv
from datetime import datetime
import os
import re

table_entries = []
file_name = []
files_by_challenge = defaultdict(list)
scenario_name = []
STAT_FILE_RE = re.compile(r"(?P<name>.+) - Challenge - (?P<date>.+) Stats\.csv")


class SessionStat(object):
    """Stats for a single session."""

    Summary = namedtuple(
        "Summary",
        [
            "kills",
            "deaths",
            "fight_time",
            "avg_ttk",
            "damage_done",
            "damage_taken",
            "score",
            "game_version",
        ],
    )
    Kill = namedtuple(
        "Kill",
        [
            "kill",
            "timestamp",
            "bot",
            "weapon",
            "ttk",
            "shots",
            "hits",
            "accuracy",
            "damage_done",
            "damage_possible",
            "efficiency",
            "cheated",
        ],
    )
    Weapon = namedtuple(
        "Weapon", ["weapon", "shots", "hits", "damage_done", "damage_possible"]
    )

    def __init__(self, date, summary, kills, weapons):
        self.date = date
        self.summary = summary
        self.kills = kills
        self.weapons = weapons

    @property
    def accuracy(self):
        total_shots, total_hits = 0, 0
        for kill in self.kills:
            total_shots += kill.shots
            total_hits += kill.hits
        if total_shots == 0:
            return 0
        return total_hits / total_shots

    @property
    def ttk(self):
        total_ttk = 0
        for kill1, kill2 in zip(self.kills, self.kills[1:]):
            total_ttk += (kill2.timestamp - kill1.timestamp).total_seconds()
        if len(self.kills) <= 1:
            return 0
        return total_ttk / (len(self.kills) - 1)

    @staticmethod
    def from_file(fname: str) -> object:
        """Returns a sessionstat object

        Args:
            fname (str): Absolute directory of stats ZipFile The class for reading and writing ZIP files.  See section

        Returns:
            sessionstat: Sessionstat object
        """

        m = STAT_FILE_RE.match(fname)
        date = datetime.strptime(m.group("date"), "%Y.%m.%d-%H.%M.%S")
        with open(fname, "r") as f:
            kill_csv, weapon_csv, summary_csv, settings_csv = f.read().split("\n\n")

        summary_info = {
            row[0].strip(":"): row[1] for row in csv.reader(summary_csv.splitlines())
        }

        score_offset = -99000 if "Ground Plaza NO UFO" in m.group("name") else 0

        summary = SessionStat.Summary(
            int(summary_info["Kills"]),
            int(summary_info["Deaths"]),
            float(summary_info["Fight Time"]),
            float(summary_info["Avg TTK"]),
            float(summary_info["Damage Done"]),
            float(summary_info["Damage Taken"]),
            float(summary_info["Score"]) + score_offset,
            tuple(map(int, summary_info["Game Version"].split("."))),
        )

        timestamp_format = (
            "%H:%M:%S:%f" if summary.game_version < (2, 0, 1, 0) else "%H:%M:%S.%f"
        )

        kills = []
        reader = csv.DictReader(kill_csv.splitlines())
        for row in reader:
            kills.append(
                SessionStat.Kill(
                    int(row["Kill #"]),
                    datetime.strptime(row["Timestamp"], timestamp_format),
                    row["Bot"],
                    row["Weapon"],
                    float(row["TTK"][:-1]),
                    int(row["Shots"]),
                    int(row["Hits"]),
                    float(row["Accuracy"]),
                    float(row["Damage Done"]),
                    float(row["Damage Possible"]),
                    float(row["Efficiency"]),
                    bool(row["Cheated"]),
                )
            )

        weapons = []
        reader = csv.DictReader(weapon_csv.splitlines())
        for row in reader:
            weapons.append(
                SessionStat.Weapon(
                    row["Weapon"],
                    int(row["Shots"]),
                    int(row["Hits"]),
                    float(row["Damage Done"]),
                    float(row["Damage Possible"]),
                )
            )

        return SessionStat(date, summary, kills, weapons)


def get_files_by_challenge():
    return files_by_challenge


def get_file_names():
    return file_name


def get_map_name(file_name: str) -> str:
    """Returns the name of the scenario in a file name

    Args:
        file_name (string): File name

    Returns:
        string: Name of a scenario
    """
    m = STAT_FILE_RE.match(file_name)
    name = m.group("name")
    return name.split("\\")[1]


def get_map_score(name: str, files_by_challenge: list, stats_directory: str) -> list:
    """Returns map scores for a specific scenario

    Args:
        name (str): Name of the desired scenario

    Returns:
        List: a list of scenario scores
    """
    scenario_scores = []
    for scenario in files_by_challenge[name]:
        scenario_directory = os.path.join(stats_directory, scenario)
        scenario_scores.append(SessionStat.from_file(scenario_directory).summary.score)

    return scenario_scores
