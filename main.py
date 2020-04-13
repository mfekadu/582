#!/usr/bin/env python3
"""main.py

Do the main thing.

[//]: # (markdown comment # noqa)

Usage:
    main.py [ --verbose | -v ]
            [ --debug | -d ]
    main.py (-h | --help)
            [ --verbose | -v ]
            [ --debug | -d ]

Options:
    -h --help                       Show this screen.

Example:
    $ python main.py

Resources:
    * docopt is cool
        * http://docopt.org
"""
import re

from colorama import init
from docopt import docopt
from termcolor import colored
from colors import strip_color

# from labs.lab1 import ???

# use Colorama to make Termcolor work on Windows too
init()


def green_bold(s: str) -> str:
    return colored(s, "green", "on_grey", attrs=["bold"])


def yellow_bold(s: str) -> str:
    return colored(s, "yellow", "on_grey", attrs=["bold"])


def white_bold(s: str) -> str:
    return colored(s, "white", "on_grey", attrs=["bold"])


def red_bold(s: str) -> str:
    return colored(s, "red", "on_grey", attrs=["bold"])


def grey_out(s: str) -> str:
    return colored(s, "grey", "on_grey")


def print_colored_doc():
    colored_doc = __doc__
    to_color_green_bold = (
        "main.py",
        "(-h | --help)",
    )
    to_color_white_bold = (
        "Do the main thing.",
        "Usage:",
        "Options:",
        "Resources:",
        "Example:",
    )
    to_color_white_bold_patterns = (r"(\$.*)",)
    to_color_red_bold_patterns = (r"(defaults to.*)",)
    to_color_grey_out = ("[//]: # (markdown comment # noqa)",)

    def repl(color_fun, strip=True):
        def _repl(m):
            s = m.group(1)
            s = strip_color(s) if strip else s
            return f"{color_fun(s)}"

        return _repl

    # for s in to_color_yellow_bold:
    #     colored_doc = colored_doc.replace(s, yellow_bold(s))
    for s in to_color_green_bold:
        colored_doc = colored_doc.replace(s, green_bold(s))
    for s in to_color_white_bold:
        colored_doc = colored_doc.replace(s, white_bold(s))
    for s in to_color_grey_out:
        colored_doc = colored_doc.replace(s, grey_out(s))
    for s in to_color_red_bold_patterns:
        colored_doc = re.sub(s, repl(red_bold), colored_doc)
    for s in to_color_white_bold_patterns:
        colored_doc = re.sub(s, repl(white_bold), colored_doc)
    print(colored_doc)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Clubs 1.0", help=False)
    VERBOSE = arguments["--verbose"]
    DEBUG = arguments["--debug"]
    print(arguments) if DEBUG else None
    if arguments["--help"]:
        print_colored_doc()
        exit()
