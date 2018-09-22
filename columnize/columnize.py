import math


class Layout:

    """
    A layout defines how to represent a list of words.
    It contains:
    - a number of rows and columns
    - the width for each column
    - the spacing between each column
    """

    def __init__(self, elem_count, col_count, spacing):
        self.col_count = col_count
        self.col_widths = [0] * col_count
        self.full_width = 0
        self.row_count = math.ceil(elem_count / col_count)
        self.spacing = spacing

    def __str__(self):
        return "Layout({0})".format(self.col_widths)

    def adjust_width(self, elt_idx, elt_width):
        """
        Adjust the width of a column so that it can fit a word
        Args:
            elt_idx: index of the element
            elt_width: width of the element
        """
        elt_column = int(elt_idx / self.row_count)
        current_width = self.col_widths[elt_column]
        if elt_width > current_width:
            self.col_widths[elt_column] = elt_width
            self.full_width = sum(self.col_widths) \
                + self.spacing * (self.col_count - 1)

    def format(self, words):
        """
        Format a list of words according to this layout
        """
        for row_idx in range(self.row_count):
            output = ''
            for col_idx in range(self.col_count):
                elt_idx = self.row_count * col_idx + row_idx
                if elt_idx < len(words):
                    if col_idx + 1 == self.col_count:
                        output += words[elt_idx]
                    else:
                        width = self.col_widths[col_idx] + self.spacing
                        output += words[elt_idx].ljust(width)
            yield output.strip()


def columnize(words, width=80, spacing=2):
    """
    Format a list of words in columns
    Args:
        width: total width of the layout
        spacing: minimum spacing between two columns
    """
    avg_len = sum(len(s) for s in words) / len(words)
    max_col_count = min(len(words), int((width+spacing) / (avg_len+spacing)))
    layouts = [Layout(len(words), i+1, spacing) for i in range(max_col_count)]
    for elt_idx in range(len(words)):
        elt_len = len(words[elt_idx])
        for layout in layouts:
            layout.adjust_width(elt_idx, elt_len)
            if layout.full_width > width:
                layouts.remove(layout)
    if layouts:
        return layouts[-1].format(words)
    else:
        return words


def command():
    """
    Entry point for the command line.
    Reads stdin and formats its tokens to fit in the terminal's width
    """
    import fileinput
    import shutil
    words = sum((l.split() for l in fileinput.input()), [])
    tty_columns = shutil.get_terminal_size().columns
    for line in columnize(words, tty_columns):
        print(line)
