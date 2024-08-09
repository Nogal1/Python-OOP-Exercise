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
    """

    def __init__(self, start=0):
        """Initialize serial generator with a starting number."""
        self.start = start
        self.current = start

    def generate(self):
        """Return the next serial number and increment the counter."""
        current_serial = self.current
        self.current += 1
        return current_serial

    def reset(self):
        """Reset the serial number to the original start number."""
        self.current = self.start

    def __repr__(self):
        """Provide a string representation of the SerialGenerator instance."""
        return f"<SerialGenerator start={self.start} next={self.current}>"