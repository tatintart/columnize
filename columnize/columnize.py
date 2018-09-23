import math


class Layout:

    """
    A layout defines how to represent a list of words.

    :attr col_count: the number of columns
    :attr row_count: the number of rows
    :attr col_widths: the width for each column
    :attr full_width: the full width of the layout
    :attr spacing: the spacing between each column
    """

    def __init__(self, elem_count, col_count, spacing):
        self.col_count = col_count
        self.row_count = math.ceil(elem_count / col_count)
        self.col_widths = [0] * col_count
        self.full_width = spacing * (col_count - 1)
        self.spacing = spacing

    def __str__(self):
        return "Layout({})".format(", ".join(str(w) for w in self.col_widths))

    def adjust_width(self, elt_idx, elt_width):
        """
        Adjust the width of a column so that it can fit a word

        :param elt_idx: index of the element
        :param elt_width: width of the element
        """
        elt_column = int(elt_idx / self.row_count)
        width_increase = elt_width - self.col_widths[elt_column]
        if width_increase > 0:
            self.col_widths[elt_column] = elt_width
            self.full_width += width_increase

    def format(self, words):
        """
        Format a list of words according to this layout

        :param words: list of words to format
        :returns: an iterator of formatted lines
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
                else:
                    break
            yield output.strip()


def columnize(words, width=80, spacing=2):
    """
    Format a list of words in columns

    :param width: total width of the layout
    :param spacing: minimum spacing between two columns
    :returns: an iterator of formatted lines
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
        if not layouts:
            break
    if layouts:
        return layouts[-1].format(words)
    else:
        return words
