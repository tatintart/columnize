import argparse
import fileinput
import shutil
from .columnize import columnize


def command():
    """
    Entry point for the command line.
    Reads stdin and formats its tokens to fit in the terminal's width
    """
    args = parse_args()
    words = sum((l.split() for l in fileinput.input(args.input)), [])
    for line in columnize(words, args.width, args.space):
        print(line)


def parse_args():
    parser = argparse.ArgumentParser(description="List things in columns")
    tty_columns = shutil.get_terminal_size().columns
    parser.add_argument('--width', '-w', default=tty_columns, type=int,
                        help="Maximum width of the output."
                        + " Default to the terminal width")
    parser.add_argument('--space', '-s', default=2, type=int,
                        help="Minimum space between columns. Defaut to 2")
    parser.add_argument('input', nargs='*', default='-',
                        help="Files to read from. Default to stdin")
    return parser.parse_args()
