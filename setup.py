"""File to be used with cx_freeze for packaging application."""
import sys
import os
from cx_Freeze import setup, Executable
import scipy
import statsmodels
import watchdog


packages = ["statsmodels", "scipy", "watchdog", "os", "sys"]


# ADD FILES
files = [
    "icon.ico",
    "themes/",
]

# TARGET
target = Executable(
    script="main.py", base="Win32GUI", icon="icon.ico", target_name="Artemis.exe"
)


# SETUP CX FREEZE
setup(
    name="Artemis",
    version="1.0",
    description="AI Training Assistant",
    author="Michael Huff",
    options={"build_exe": {"packages": packages, "include_files": files}},
    executables=[target],
)
