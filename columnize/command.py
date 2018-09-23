import fileinput
import shutil
from .columnize import columnize


def command():
    """
    Entry point for the command line.
    Reads stdin and formats its tokens to fit in the terminal's width
    """
    words = sum((l.split() for l in fileinput.input()), [])
    tty_columns = shutil.get_terminal_size().columns
    for line in columnize(words, tty_columns):
        print(line)
