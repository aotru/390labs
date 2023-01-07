"""
range.py.

A simplified version of Python's range type.
"""

from math import ceil


class Range:
    """Represents a fixed sequence of integers.

    The sequence is defined by an inclusive start, an exclusive end,
    and a step value between adjacent integers in the sequence.
    """

    def __init__(self, start, stop, step=1):
        """Construct this range with the given start, stop, and step.

        Requires start, stop, and step to be integers, and step to be
        positive.
        """
        self.start = start
        self.stop = stop
        self.step = step
        self.len = ceil((stop - start) / step)

    def __iter__(self):
        """Return an iterator object over this sequence."""
        return RangeIter(self.start, self.stop, self.step)

    def __len__(self):
        """Return the length of this sequence."""
        return self.len

    def __contains__(self, i):
        """Return whether the given integer is in this range."""
        return self.start <= i < self.stop and (i - self.start) % self.step == 0


class RangeIter:
    """An iterator over a range of integers."""

    def __init__(self, start, stop, step):
        """Construct an iterator with the given start, stop, and step.

        Requires start, stop, and step to be integers, and step to be
        positive.
        """
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        """Return this object."""
        return self

    def __next__(self):
        """Return the next item in the sequence.

        Raises a StopIteration if there are no more items.
        """
        if self.start >= self.stop:
            raise StopIteration
        else:
            value = self.start
            self.start += self.step
            return value
