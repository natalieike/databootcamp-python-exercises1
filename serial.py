"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    >>> repr(serial)
    'serial <SerialGenerator start=100 next=101>'
    """

    def __init__(self, start):
        self.start = start
        self._current = start - 1 #first generated number should return start number

    def __repr__(self):
        return 'serial <SerialGenerator start={start} next={next}>'.format(start=self.start, next=self.next)

    def generate(self):
        self._current = self._current + 1
        return self._current
    
    def reset(self):
        self._current = self.start - 1

    @property
    def next(self):
        return self._current + 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
