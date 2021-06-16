"""
///////////////////////////////////////////////////////////////
APPLICATION BY: MICHAEL HUFF
Artemis created with: Qt Designer and PySide6
JUNE 10, 2021
V: 1.0.0
///////////////////////////////////////////////////////////////
"""
import pandas as pd
from pandas.core.frame import DataFrame


class Aimer:
    """Class that contains benchmark data for Aimer."""

    def get_start_benchmarks(self) -> dict:
        """Benchmarks used to determine starting rankdatetime A combination of a date and a time. Attributes: ()

        Returns:
            [dict]: A dictonary containing scenario keys and score values.
        """

        starterBenchmarks = {
            "Beginner": {
                "1wall6targets TE": 120,
                "Bounce 180 Tracking": 45,
                "Close Long Strafes Invincible": 11500,
            },
            "IBeginner": {
                "1wall6targets TE": 130,
                "Bounce 180 Tracking": 50,
                "Close Long Strafes Invincible": 12800,
            },
            "AdvBeginner": {
                "1wall6targets TE": 140,
                "Bounce 180 Tracking": 56,
                "Close Long Strafes Invincible": 1400,
            },
            "SubIntermediate": {
                "1wall6targets TE": 150,
                "Bounce 180 Tracking": 63,
                "Close Long Strafes Invincible": 14800,
            },
            "Intermediate": {
                "1wall6targets TE": 165,
                "Bounce 180 Tracking": 73,
                "Close Long Strafes Invincible": 16100,
            },
            "Advanced": {
                "1wall6targets TE": 180,
                "Bounce 180 Tracking": 85,
                "Close Long Strafes Invincible": 16800,
            },
            "SubAimbeast": {
                "1wall6targets TE": 181,
                "Bounce 180 Tracking": 86,
                "Close Long Strafes Invincible": 16801,
            },
        }

        return starterBenchmarks

    def get_beginner_routines(self) -> list:
        """Returns three routines for beginners. Tracking, Click, and Complete in that order.

        Returns:
            list: Returns 3 lists for tacking, click, and complete routines.
        """

        tracking = [
            "Midrange Long Strafes Invincible",
            "air far long strafes",
            "Vertical Long Strafes",
            "Bounce 180 Tracking Large",
            "1wall6targets TE",
            "Tile Frenzy – Strafing – 01",
            "Air Invincible",
        ]

        click = [
            "1wall6targets TE",
            "Tile Frenzy – Strafing – 02",
            "5 Sphere Hipfire small",
            "Tile Frenzy Flick",
            "Midrange Long Strafes Invincible",
            "Vertical Long Strafes",
        ]

        complete = [
            "Midrange Long Strafes Invincible",
            "1wall6targets TE",
            "air far long strafes",
            "Tile Frenzy – Strafing – 01",
            "Vertical Long Strafes",
            "Target Switching 90",
        ]

        return tracking, click, complete

    def get_ibeginner_routines(self) -> list:
        """Returns three routines for intermediate beginners. Tracking, Click, and Complete in that order.

        Returns:
            list: Returns 3 lists for tracking, click, and complete routines.
        """

        tracking = [
            "Close Long Strafes Invincible",
            "Smoothness Trainer",
            "Vertical Long Strafes",
            "Tile Frenzy 180 Strafing 200 Percent Tracking",
            "1wall9000targets",
            "Tile Frenzy 180",
        ]

        click = [
            "1w2ts reload",
            "Tile Frenzy 180",
            "1wall5targets_pasu slow",
            "patTargetSwitch easy ",
            "fuglaaXYLongstrafes",
            "Vertical Long Strafes",
        ]

        complete = [
            "Close Long Strafes Invincible",
            "1w2ts reload",
            "gp far long strafes",
            "1wall9000targets",
            "patTargetSwitch easy",
            "1wall5targets_pasu slow",
        ]

        return tracking, click, complete

    def get_advbeginner_routines(self) -> list:
        """Returns three routines for advanced beginners. Tracking, Click, and Complete in that order.

        Returns:
            list: Returns 3 lists for tracking, click, and complete routines.
        """

        tracking = [
            "RexStrafesCata Invincible",
            "Close Long Strafes Invincible",
            "LG Pin Practice 360",
            "1wall6Targets TE",
            "Thin Aiming Long Invincible",
            "1w2ts reload",
        ]

        click = [
            "1wall6targets TE",
            "1w2ts reload",
            "Bounce 180 Reload",
            "patTargetSwitch easy",
            "1wall5targets_pasu slow",
            "gp 2 invincible",
        ]

        complete = [
            "RexStrafesCata Invincible",
            "1wall6targets TE",
            "Air Target Switching 360",
            "1wall5targets_pasu slow",
            "Close Long Strafes Invincible",
            "5 Sphere Hipfire small",
        ]

        return tracking, click, complete

    def get_subintermediate_routines(self) -> list:
        """Returns three routines for sub-intermediate. Tracking, Click, and Complete in that order.

        Returns:
            list: Returns 3 lists for tracking, click, and complete routines.
        """

        tracking = [
            "Midrange Fast Strafes V2",
            "Close Fast Strafes Easy",
            "Vertical Long Strafes",
            "Tile Frenzy 180 Strafing 300 Percent Tracking",
            "Bounce 180 Tracking",
            "Ground Plaza Easy",
        ]

        click = [
            "Bounce 180 Reload",
            "1w6ts reload",
            "1wall5targets_pasu Reload",
            "Air Invincible 6",
            "Wide Wall 6Targets",
            "Ground Plaza Easy",
        ]

        complete = [
            "Midrange Fast Strafes V2",
            "Close Fast Strafes Easy",
            "Bounce 180 Reload",
            "1wall5targets_pasu Reload",
            "Tile Frenzy 180 Strafing 300 Percent Tracking",
            "Vertical Long Strafes",
        ]

        return tracking, click, complete

    def get_intermediate_routines(self) -> list:
        """Returns three routines for intermediate. Tracking, Click, Complete and target scores in that order.

        Returns:
            list: Returns 6 lists for tracking, click, and complete routines.
        """

        tracking = [
            "Close Fast Strafes Invincible",
            "Vertical Fast Strafes",
            "Ground Plaza Easy",
            "Air no UFO no SKYBOTS",
            "Bounce 180 Tracking",
            "1wall5targets_pasu Reload",
        ]

        click = [
            "Close Fast Strafes Easy Invincible",
            "1wall5targets_pasu Reload",
            "1wall 6targets small",
            "Target Acquisition Flick Easy",
            "Wide Wall 6Targets",
            "Bounce 180",
        ]

        complete = [
            "Close Fast Strafes Invincible",
            "Vertical Fast Strafes",
            "Ground Plaza Easy",
            "Bounce 180 Tracking",
            "1wall5targets_pasu Reload",
            "Bounce 180",
            "Target Acquisition Flick Easy",
        ]

        # Must beat at least 5 to advance.
        trackingTargetScores = {
            "Close Fast Strafes Invincible": 9800,
            "Vertical Fast Strafes": 8500,
            "Ground Plaza Easy": 894,
            "Air no UFO no SKYBOTS": 835,
            "Bounce 180 Tracking": 74,
            "1wall5targets_pasu Reload": 103,
        }

        clickTargetScores = {
            "Close Fast Strafes Easy Invincible": 13000,
            "1wall5targets_pasu Reload": 105,
            "1wall 6targets small": 1025,
            "Target Acquisition Flick Easy": 92,
            "Wide Wall 6Targets": 117,
            "Bounce 180": 70,
        }

        completeTargetScores = {
            "Close Fast Strafes Invincible": 9400,
            "Vertical Fast Strafes": 8300,
            "Ground Plaza Easy": 892,
            "Bounce 180 Tracking": 73,
            "1wall5targets_pasu Reload": 103,
            "Bounce 180": 65,
            "Target Acquisition Flick Easy": 90,
        }

        return (
            tracking,
            click,
            complete,
            trackingTargetScores,
            clickTargetScores,
            completeTargetScores,
        )

    def get_advanced_routines(self):
        """Returns three routines for intermediate. Tracking, Click, Complete and target scores in that order."""

        # Must beat at least 10 of the 16 in each to advance.
        trackingTargetScores = {
            "Close Fast Strafes Invincible": 11000,
            "Close FS Easy Dodge": 17400,
            "Vertical Fast Strafes": 10000,
            "Air no UFO no SKYBOTS": 857,
            "Air Dodge": 110,
            "Pasu Track Invincible v2": 6300,
            "Ground Plaza NO UFO": 99913,
            "lcg3 Reborn Varied": 28000,
            "Popcorn Goated Tracking Invincible": 1100,
            "Thin Gauntlet V2": 872,
            "Bounce 180 Tracking Small Invincible Fixed": 4000,
            "kinTargetSwitch small no reload": 16300,
            "Bounce 180 Tracking Small": 60,
            "psalmflick Strafing Tracking": 64,
            "patTargetSwitch Dodge 360": 11600,
            "Bounce 180 Tracking": 83,
            "kinTargetSwitch No Reload": 21000,
            "1wall5targets_pasu Reload": 118,
            "Popcorn Sparky": 200,
            "Bounce 180": 80,
            "Wide Wall 6Targets": 124,
        }

        clickTargetScores = {
            "Ground Plaza Easy": 903,
            "Pasu Track Invincible v2": 6200,
            "Air no UFO no SKYBOTS": 852,
            "Air Dodge": 108,
            "Pokeball Frenzy Auto Small": 48,
            "1wall6 flick": 118,
            "devTargetSwitch Goated": 530,
            "patTargetSwitch Dodge 360": 11600,
            "Bounce 180 Tracking": 82,
            "patTargetSwitch No Reload": 6800,
            "Popcorn Sparky": 210,
            "Reflex Flick – Fair": 5000,
            "Close Fast Strafes Shotgun": 14200,
            "patTargetClick 1shot": 6000,
            "1wall5targets_pasu Reload": 122,
            "Pasu Dodge Easy": 380000,
            "Bounce 180": 85,
            "1wall 6targets small": 1150,
            "Target Acquisition Flick": 65,
            "Reflex Flick – Mini": 4800,
            "1wall9000targets": 250,
            "Wide Wall 6Targets": 127,
            "1w2ts reload": 92,
            "Microshot Speed": 185,
            "1wall6targets TE": 180,
        }

        completeTargetScores = {
            "Close Fast Strafes Invincible": 10700,
            "Close FS Easy Dodge": 17000,
            "Vertical Fast Strafes": 9750,
            "Pasu Track Invincible v2": 6200,
            "Air no UFO no SKYBOTS": 854,
            "Air Dodge": 109,
            "psalmflick Strafing Tracking": 65,
            "kinTargetSwitch small no reload": 16500,
            "kinTargetSwitch No Reload": 21000,
            "patTargetSwitch Dodge 360": 12000,
            "patTargetSwitch No Reload": 7000,
            "Bounce 180 Tracking": 85,
            "1wall6 flick": 120,
            "Popcorn Sparky": 200,
            "Reflex Flick – Fair": 4700,
            "Close Fast Strafes Shotgun": 13800,
            "patTargetClick 1shot": 5850,
            "1wall5targets_pasu Reload": 118,
            "Pasu Dodge Easy": 370000,
            "Bounce 180": 80,
            "1w2ts reload": 90,
            "1wall9000targets": 243,
            "Wide Wall 6Targets": 124,
            "1wall 6targets small": 1100,
            "Microshot Speed": 182,
        }

        return (
            list(trackingTargetScores.keys()),
            list(clickTargetScores.keys()),
            list(completeTargetScores.keys()),
            trackingTargetScores,
            clickTargetScores,
            completeTargetScores,
        )


class Sparky:
    """Sparky Object."""

    def __init__(self):

        self.data = {
            "Scenario": [
                "1wall5targets_pasu Reload"
                "Popcorn Sparky"
                "ww6t reload"
                "1w6ts reload v2"
                "Bounce 180 Sparky"
                "Air no UFO no SKYBOTS"
                "Ground Plaza Sparky v3"
                "Popcorn Goated Tracking Invincible"
                "Thin Gauntlet V2"
                "Pasu Track Invincible v2"
                "patTS NR"
                "Bounce 180 Tracking"
                "kinTS NR"
                "devTS Goated NR"
                "voxTargetSwitch"
            ],
            "Silver": [
                80,
                70,
                105,
                85,
                55,
                780,
                850,
                500,
                825,
                3600,
                5400,
                45,
                15000,
                400,
                67,
            ],
            "Gold": [
                90,
                100,
                115,
                95,
                65,
                810,
                860,
                600,
                845,
                4500,
                6000,
                56,
                16500,
                450,
                77,
            ],
            "Platinum": [
                105,
                150,
                125,
                105,
                75,
                835,
                872.5,
                800,
                862.5,
                5500,
                6500,
                68,
                18500,
                500,
                87,
            ],
            "Diamond": [
                120,
                200,
                135,
                115,
                85,
                853,
                885,
                1100,
                872.5,
                6200,
                7100,
                80,
                20500,
                550,
                97,
            ],
            "Master": [
                135,
                250,
                145,
                125,
                95,
                868,
                892,
                1300,
                882.5,
                6900,
                7700,
                90,
                22000,
                600,
                107,
            ],
            "Grandmaster": [
                145,
                300,
                160,
                137,
                105,
                877,
                900,
                1600,
                895,
                7300,
                8000,
                100,
                23500,
                630,
                112,
            ],
        }

        self.df = pd.DataFrame(data=self.data)

    def get_sparky_dataframe(self) -> DataFrame:
        """Returns all sparky benchmarks as a dataframe.

        Returns:
            DataFrame: dataframe object.
        """
        return self.df


class Voltaic:
    """Voltaic object."""

    def __init__(self):

        self.intermediateData = {
            "Scenario": [
                "Pasu Voltaic Easy",
                "B180 Voltaic Easy",
                "Popcorn Voltaic Easy",
                "ww3t Voltaic",
                "1w4ts Voltaic",
                "6 Sphere Hipfire Voltaic",
                "Smoothbot Voltaic Easy",
                "Air Angelic 4 Voltaic Easy",
                "PGTI Voltaic Easy",
                "FuglaaXYZ Voltaic Easy",
                "Ground Plaza Voltaic Easy",
                "Air Voltaic Easy",
                "patTS Voltaic Easy",
                "psalmTS Voltaic Easy",
                "voxTS Voltaic Easy",
                "kinTS Voltaic Easy",
                "B180T Voltaic Easy",
                "Smoothbot TS Voltaic Easy",
            ],
            "Bronze": [
                40,
                52,
                100,
                83,
                70,
                95,
                1700,
                1800,
                700,
                7500,
                835,
                775,
                65,
                50,
                74,
                45,
                40,
                35,
            ],
            "Silver": [
                50,
                61,
                150,
                93,
                82,
                108,
                2100,
                2200,
                1000,
                8500,
                845,
                800,
                80,
                58,
                82,
                54,
                51,
                42,
            ],
            "Gold": [
                56,
                70,
                200,
                103,
                91,
                120,
                2400,
                2600,
                1300,
                10000,
                855,
                825,
                85,
                67,
                90,
                60,
                60,
                46,
            ],
            "Platinum": [
                66,
                77,
                250,
                113,
                100,
                132,
                2800,
                3000,
                1600,
                12000,
                870,
                852,
                91,
                76,
                100,
                66,
                69,
                50,
            ],
            "Diamond": [
                75,
                86,
                310,
                123,
                110,
                142,
                3100,
                3300,
                1900,
                14000,
                880,
                865,
                98,
                85,
                109,
                72,
                77,
                54,
            ],
        }

        self.advancedData = {
            "Scenario": [
                "Pasu Voltaic",
                "B180 Voltaic",
                "Popcorn Voltaic",
                "ww3t Voltaic",
                "1w4ts Voltaic",
                "6 Sphere Hipfire Voltaic",
                "Smoothbot Voltaic",
                "Air Angelic 4 Voltaic",
                "PGTI Voltaic",
                "FuglaaXYZ Voltaic",
                "Ground Plaza Voltaic",
                "Air Voltaic",
                "patTS Voltaic",
                "psalmTS Voltaic",
                "voxTS Voltaic",
                "kinTS Voltaic",
                "B180T Voltaic",
                "Smoothbot TS Voltaic",
            ],
            "Jade": [
                70,
                78,
                220,
                130,
                115,
                152,
                2600,
                2700,
                1100,
                11300,
                862,
                850,
                91,
                85,
                102,
                65,
                64,
                50,
            ],
            "Master": [
                78,
                88,
                260,
                138,
                120,
                160,
                2900,
                3000,
                1400,
                12500,
                870,
                860,
                97,
                90,
                110,
                72,
                70,
                55,
            ],
            "Grandmaster": [
                85,
                98,
                320,
                148,
                130,
                175,
                3400,
                3400,
                1800,
                13800,
                880,
                872,
                103,
                98,
                118,
                79,
                78,
                60,
            ],
            "Nova": [
                95,
                108,
                390,
                158,
                142,
                192,
                3800,
                3900,
                2200,
                14800,
                888,
                883,
                110,
                105,
                125,
                84,
                85,
                65,
            ],
            "Astra": [
                105,
                115,
                440,
                170,
                152,
                210,
                4000,
                4100,
                2500,
                16000,
                894,
                887,
                116,
                110,
                131,
                88,
                90,
                70,
            ],
        }

        self.df_int = pd.DataFrame(data=self.intermediateData)
        self.df_adv = pd.DataFrame(data=self.advancedData)

    def get_voltaic_data_int(self, dict=False) -> dict or DataFrame:
        """Returns intermediate benchmark information

        Returns:
            dataframe: benchmark information
            dict: benchamrk information
        """
        if dict:
            return self.intermediateData
        else:
            return self.df_int

    def get_voltaic_data_adv(self, dict=False) -> dict or DataFrame:
        """Returns advanced benchmark information

        Returns:
            dataframe: benchmark information
            dict: benchamrk information
        """
        if dict:
            return self.advancedData
        else:
            return self.df_adv

    def get_color_codes(tier: int, is_adv=False) -> str:
        """Returns color hex codes for associated rank

        Args:
            color (int): Tier - Example: 0 = Silver, 1 = Gold

        Returns:
            str, str: Color codes for each rank.
        """

        unranked = "#FFFFFF"

        primeBronze = "#b45f06"
        secondBronze = "#fce5cd"

        primeSilver = "#cbd9e6"
        secondSilver = "#dce5ec"

        primeGold = "#cab148"
        secondGold = "#e4dab0"

        primePlat = "#2fcfc2"
        secondPlat = "#b9efea"

        primeDiamond = "#b9f2ff"
        secondDiamond = "#e7faff"

        primeJade = "#85fa85"
        secondJade = "#cefdce"

        primeMaster = "#ec44ca"
        secondMaster = "#f8c0ed"

        primeGrandmaster = "#ffd700"
        secondGrandmaster = "#fff1aa"

        primeNova = "#7900ff"
        secondNova = "#c089ff"

        primeAstra = "#ff2262"
        secondAstra = "#ff89aa"

        if not is_adv:
            if tier == 0:
                return unranked, secondBronze
            elif tier == 1:
                return primeBronze, secondSilver
            elif tier == 2:
                return primeSilver, secondGold
            elif tier == 3:
                return primeGold, secondPlat
            elif tier == 4:
                return primePlat, secondDiamond
            elif tier == 5:
                return primeDiamond, secondDiamond

        if tier == 0:
            return primeJade, secondMaster
        elif tier == 1:
            return primeMaster, secondGrandmaster
        elif tier == 2:
            return primeGrandmaster, secondNova
        elif tier == 3:
            return primeNova, secondAstra
        elif tier == 4:
            return primeAstra, secondAstra


class Revosect:
    """Revosect object."""

    def __init__(self):

        self.easyData = {
            "Scenario": [
                "1w4ts reload",
                "Wide Wall 3 Targets",
                "voxTS Static Click rAim",
                "B180 rAim Easy",
                "Pasu rAim Easy",
                "Popcorn rAim Easy",
                "PGTI rAim Easy",
                "Smoothbot rAim Easy",
                "Air Angelic rAim Easy",
                "fuglaaXY Reactive rAim Easy",
                "Air 3478 rAim Easy",
                "Flicker Plaza rAim Easy",
                "patCircleSwitch NR",
                "Pokeball Wide rAim Easy",
                "voxTS rAim Easy",
                "B180T rAim Easy",
                "kinTS rAim Easy",
                "Pasu Track Smaller rAim Easy",
            ],
            "Bronze": [
                85,
                75,
                115,
                55,
                94,
                120,
                1000,
                2400,
                885,
                8000,
                882,
                860,
                5200,
                100,
                77,
                50,
                17000,
                52,
            ],
            "Silver": [
                90,
                85,
                125,
                65,
                100,
                160,
                1150,
                2700,
                890,
                9000,
                892,
                866,
                5600,
                110,
                83,
                55,
                18000,
                56,
            ],
            "Gold": [
                100,
                95,
                135,
                70,
                108,
                200,
                1350,
                3100,
                900,
                10000,
                902,
                874,
                6200,
                120,
                90,
                60,
                19000,
                60,
            ],
            "Platinum": [
                110,
                105,
                145,
                78,
                115,
                250,
                1550,
                3600,
                905,
                11000,
                912,
                884,
                6600,
                130,
                95,
                65,
                20000,
                64,
            ],
            "Ruby": [
                115,
                115,
                155,
                87,
                125,
                290,
                1800,
                4000,
                915,
                12000,
                918,
                892,
                7000,
                140,
                100,
                70,
                21000,
                68,
            ],
        }

        self.advancedData = {
            "Scenario": [
                "1w4ts reload",
                "Wide Wall 3 Targets",
                "voxTS Static Click rAim",
                "Bounce 180 rAim",
                "Pasu Reload Goated",
                "Popcorn Goated rAim",
                "Popcorn Goated Tracking Invincible",
                "SmoothBot Invincible Goated",
                "Air Angelic",
                "fuglaaXY Reactive rAim",
                "Air no UFO no SKYBOTS Small 3478",
                "Flicker Plaza",
                "patCircleSwitch NR",
                "Pokeball Wide rAim",
                "voxTS rAim",
                "Bounce 180 Tracking Small",
                "kinTS rAim",
                "Pasu Track Smaller rAim",
            ],
            "Emerald": [
                120,
                120,
                160,
                72,
                110,
                200,
                1250,
                3400,
                900,
                8200,
                884,
                878,
                7400,
                135,
                94,
                67,
                20000,
                66,
            ],
            "Diamond": [
                125,
                128,
                170,
                80,
                118,
                260,
                1500,
                3900,
                908,
                9100,
                894,
                888,
                7800,
                140,
                98,
                72,
                21500,
                71,
            ],
            "Immortal": [
                130,
                133,
                175,
                87,
                125,
                300,
                1700,
                4200,
                913,
                9900,
                903,
                895,
                8400,
                145,
                104,
                77,
                22500,
                76,
            ],
            "Archon": [
                140,
                138,
                185,
                95,
                135,
                350,
                2000,
                4700,
                921,
                10800,
                912,
                903,
                8800,
                150,
                110,
                84,
                23700,
                81,
            ],
            "Divine": [
                148,
                145,
                195,
                103,
                145,
                390,
                2300,
                5200,
                927,
                11700,
                920,
                910,
                9200,
                155,
                115,
                90,
                24600,
                86,
            ],
        }

        self.df_esy = pd.DataFrame(data=self.easyData)
        self.df_adv = pd.DataFrame(data=self.advancedData)

    def get_revosect_data_int(self, dict=False) -> dict or DataFrame:
        """Returns intermediate benchmark information

        Returns:
            dataframe: benchmark information
            dict: benchmark information
        """
        if dict:
            return self.easyData
        else:
            return self.df_esy

    def get_revosect_data_adv(self, dict=False) -> dict or DataFrame:
        """Returns advanced benchmark information

        Returns:
            dataframe: benchmark information
            dict: benchmark information
        """
        if dict:
            return self.advancedData
        else:
            return self.df_adv

    def get_color_codes(tier: int, is_adv=False) -> str:
        """Returns color hex codes for associated rank

        Args:
            color (int): Tier - Example: 1 = Bronze, 2= Silver

        Returns:
            str, str: Color codes for each rank.
        """

        unranked = "#FFFFFF"

        primeBronze = "#b45f06"
        secondBronze = "#eaad99"

        primeSilver = "#999999"
        secondSilver = "#d9d9d9"

        primeGold = "#ffd966"
        secondGold = "#fff2cc"

        primePlat = "#a4c2f4"
        secondPlat = "#efefef"

        primeRuby = "#e0115f"
        secondRuby = "#ffc7dc"

        primeEmerald = "#50c878"
        secondEmerald = "#aee9b6"

        primeDiamond = "#4a86e8"
        secondDiamond = "#c9daf8"

        primeImmortal = "#c36eff"
        secondImmortal = "#b4a7d6"

        primeArchon = "#ff0000"
        secondArchon = "#ea9999"

        primeDivine = "#050000"
        secondDivine = "#999999"

        if not is_adv:
            if tier == 0:
                return unranked, secondBronze
            elif tier == 1:
                return primeBronze, secondSilver
            elif tier == 2:
                return primeSilver, secondGold
            elif tier == 3:
                return primeGold, secondPlat
            elif tier == 4:
                return primePlat, secondRuby
            elif tier == 5:
                return primeRuby, secondEmerald

        if tier == 0:
            return primeEmerald, secondDiamond
        elif tier == 1:
            return primeDiamond, secondImmortal
        elif tier == 2:
            return primeImmortal, secondArchon
        elif tier == 3:
            return primeArchon, secondDivine
        elif tier == 4:
            return primeDivine, secondDivine


def find_volt_rank_int(tier_score: int) -> str:
    """Returns rank title based on provided score.

    Args:
        tier_score (int): score

    Returns:
        str: Rank name.
    """
    if tier_score >= 30:
        return "Diamond"
    if tier_score >= 24:
        return "Platinum"
    elif tier_score >= 18:
        return "Gold"
    elif tier_score >= 12:
        return "Silver"
    elif tier_score >= 6:
        return "Bronze"

    return "Unrated"


def find_volt_rank_adv(tier_score: int) -> str:
    """Returns rank title based on provided score.

    Args:
        tier_score (int): score

    Returns:
        str: Rank name.
    """
    if tier_score >= 24:
        return "Ascended"
    elif tier_score >= 18:
        return "Nova"
    elif tier_score >= 12:
        return "Grandmaster"
    elif tier_score >= 6:
        return "Master"


def find_ra_rank_easy(tier_score: int) -> str:
    """Returns rank title based on provided score.

    Args:
        tier_score (int): score

    Returns:
        str: Rank name.
    """
    if tier_score >= 30:
        return "Diamond"
    if tier_score >= 24:
        return "Platinum"
    elif tier_score >= 18:
        return "Gold"
    elif tier_score >= 12:
        return "Silver"
    elif tier_score >= 6:
        return "Bronze"

    return "Unrated"


def find_ra_rank_adv(tier_score: int) -> str:
    """Returns rank title based on provided score.

    Args:
        tier_score (int): score

    Returns:
        str: Rank name.
    """
    if tier_score >= 24:
        return "Archon"
    elif tier_score >= 18:
        return "Immortal"
    elif tier_score >= 12:
        return "Diamond"
    elif tier_score >= 6:
        return "Emerald"
