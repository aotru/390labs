"""Recursive-descent parser for Python-like nested lists of integers."""


class Stream:
    """A stream over a sequence of elements."""

    def __init__(self, string):
        """Initialize this stream with the given string data."""
        self._data = string
        self._position = 0

    def read_char(self):
        """Read the next character and move the position forward."""
        if self._position < len(self._data):
            self._position += 1
            return self._data[self._position - 1]
        return ''

    def peek_char(self):
        """Read the next character without moving the position forward."""
        if self._position < len(self._data):
            return self._data[self._position]
        return ''


def parse(string):
    """Parse nested integer lists from a string.

    No whitespace is allowed, and a list may not end with a comma.
    >>> parse('[1]')
    [1]
    >>> parse('[123]')
    [123]
    >>> parse('[1,23]')
    [1, 23]
    >>> parse('[1,[2],3]')
    [1, [2], 3]
    >>> parse('[1,[2,4],3]')
    [1, [2, 4], 3]
    >>> parse('[1,[2,4],[3]]')
    [1, [2, 4], [3]]
    >>> parse('[1,[2,4],[3]] asdf')
    [1, [2, 4], [3]]
    """
    return parse_list(Stream(string))


def parse_list(stream):
    """Parse nested integer lists from a stream."""
    first_char = stream.read_char()
    if first_char == '[':
        elements = parse_elements_opt(stream)
        close_char = stream.read_char()
        if close_char == ']':
            return elements
        raise SyntaxError(f"expected ], got: '{close_char}'")
    raise SyntaxError(f"expected [, got: '{first_char}'")


def parse_elements_opt(stream):
    """Parse optional elements from a stream."""
    first_char = stream.peek_char()
    if first_char == ']':
        return []
    return parse_elements(stream)


def parse_elements(stream):
    """Parse comma-separated elements from a stream."""
    elements = [parse_element(stream)]
    next_char = stream.peek_char()
    if next_char == ',':
        stream.read_char()
        elements.extend(parse_elements(stream))
    return elements


def parse_element(stream):
    """Parse a single list or integer element from a stream."""
    first_char = stream.peek_char()
    if first_char == '[':
        return parse_list(stream)
    return parse_integer(stream)


def parse_integer(stream: Stream):
    """Parse an integer from a stream."""
    digits = []
    read_digits(stream, digits)
    return int(''.join(digits))


def read_digits(stream, digits):
    digit = stream.peek_char()
    if digit.isdigit():
        stream.read_char()
        digits.append(digit)
        read_digits(stream, digits)


if __name__ == '__main__':
    import readline  # noqa # pylint: disable=unused-import
    while True:
        try:
            line = input('> ')
            print(parse(line))
        except (EOFError, KeyboardInterrupt):
            break
        except SyntaxError as exc:
            print(f'Error: {exc}')
