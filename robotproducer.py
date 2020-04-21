#!/usr/bin/env python3
"""robotproducer.py

Give me a movie overview and I will find the right cast & crew!

[//]: # (markdown comment # noqa)

Usage:
    robotproducer.py IN_TXT_FILE
                     [ --verbose | -v ]
                     [ --debug | -d ]
    robotproducer.py (-h | --help)
                     [ --verbose | -v ]
                     [ --debug | -d ]

Options:
    -h --help                       Show this screen.
    --debug -d                      printouts while running, extra debugging.

Example:
    $ python robotproducer.py inputs/in1.txt
    title:  A Good Movie Title
    director:  Good Director
    cast:  Good Actress, Good Actor

Resources:
    * [docopt is cool](http://docopt.org)

"""
from typing import List

from docopt import docopt

from labs import lab1
from labs.lab1 import FullName, Overview, Suggestions, producer
from utils.terminal_colors import print_colored_doc, print_debug


def print_help():
    to_color_green_bold = (
        "robotproducer.py",
        "(-h | --help)",
    )
    to_color_yellow_bold = ("IN_TXT_FILE",)
    to_color_white_bold = (
        "Give me a movie overview and I will find the right crew!",
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
    arguments = docopt(__doc__, version="robotproducer 1.0", help=False)
    VERBOSE = arguments["--verbose"] or arguments["-v"]
    DEBUG = arguments["--debug"]
    print(arguments) if DEBUG else None
    print("VERBOSE:", VERBOSE) if DEBUG else None
    print("DEBUG:", DEBUG) if DEBUG else None
    if arguments["--help"]:
        print_help()
        exit()

    IN_TXT_FILE = arguments["IN_TXT_FILE"]

    overview = ""

    with open(IN_TXT_FILE, "r") as f:
        overview = f.read()

    assert overview != "", "overview file was empty"

    print_debug("overview[:100]", overview[:100]) if DEBUG else None

    overview: Overview = Overview(overview)

    lab1.DEBUG = DEBUG

    sugg: Suggestions = producer(overview, use_large=False)

    for k, v in sugg.items():
        if type(v) == list:
            names: List[FullName] = v  # pyre-ignore[9]
            print(f"{k}: ", ", ".join(names))
        else:
            print(f"{k}: ", v)
