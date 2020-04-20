#!/usr/bin/env python3
"""main.py

A common command-line interface for all CSC 582 labs.

[//]: # (markdown comment # noqa)

Usage:
    main.py lab1 IN_TXT_FILE
            [ --verbose | -v ]
            [ --debug | -d ]
    main.py lab2
            [ --verbose | -v ]
            [ --debug | -d ]
    main.py lab3
            [ --verbose | -v ]
            [ --debug | -d ]
    main.py (-h | --help)
            [ --verbose | -v ]
            [ --debug | -d ]

Options:
    -h --help      Show this screen.
    --debug -d     printouts while running, extra debugging.
    lab1           A robot producer. Given an overview, outputs a movie cast & crew.
    lab2           Do the lab2 thing.
    lab3           Do the lab3 thing.
    IN_TXT_FILE    a file to read from.

Example:
    $ python main.py lab1 inputs/in1.txt
    ...

Resources:
    * [docopt is cool](http://docopt.org)

"""
import os
import subprocess
from enum import Enum

from docopt import docopt

from utils.terminal_colors import print_colored_doc, print_debug


class OS_NAME(Enum):
    # https://stackoverflow.com/a/1325587/5411712
    WINDOWS = "nt"
    UNIX = "posix"
    OTHER = "java"


def print_help():
    to_color_green_bold = (
        "main.py",
        "(-h | --help)",
    )
    to_color_yellow_bold = (
        "lab1",
        "IN_TXT_FILE",
        "lab2",
        "lab3",
        "lab4",
        "lab5",
    )
    to_color_white_bold = (
        "Do the main thing.",
        "Usage:",
        "Options:",
        "Example:",
        "Resources:",
        "Changelog:",
    )
    to_color_white_bold_patterns = (r"(\$.*)",)
    to_color_red_bold_patterns = (r"(defaults to.*)",)
    to_color_grey_out = ("[//]: # (markdown comment # noqa)",)
    print_colored_doc(
        doc=__doc__,
        to_color_green_bold=to_color_green_bold,
        to_color_yellow_bold=to_color_yellow_bold,
        to_color_white_bold=to_color_white_bold,
        to_color_white_bold_patterns=to_color_white_bold_patterns,
        to_color_red_bold_patterns=to_color_red_bold_patterns,
        to_color_grey_out=to_color_grey_out,
    )


if __name__ == "__main__":
    # My basic docopt setup...
    arguments = docopt(__doc__, version="csc582 Main 1.0.0", help=False)
    VERBOSE = arguments["--verbose"] or arguments["-v"]
    DEBUG = arguments["--debug"]
    print(arguments) if DEBUG else None
    print("VERBOSE:", VERBOSE) if DEBUG else None
    print("DEBUG:", DEBUG) if DEBUG else None
    if arguments["--help"]:
        print_help()
        exit()

    IN_TXT_FILE = arguments["IN_TXT_FILE"]

    if arguments["lab1"]:
        # https://stackoverflow.com/a/1325587/5411712
        set_options = [a for a, v in arguments.items() if v and a.startswith("-")]
        if os.name == OS_NAME.WINDOWS.value:
            # often Windows does not have `python3` as alias
            subprocess.run(["python", "robotproducer.py", IN_TXT_FILE, *set_options])
        elif os.name == OS_NAME.UNIX.value:
            subprocess.run(["python3", "robotproducer.py", IN_TXT_FILE, *set_options])
        else:
            print_debug(f"why is this Python running on {os.name}??")
            subprocess.run(["python", "robotproducer.py", IN_TXT_FILE, *set_options])
        exit()

    if arguments["lab2"]:
        subprocess.run(["echo", "lab2"])
        exit()

    if arguments["lab3"]:
        subprocess.run(["echo", "lab2"])
        exit()
