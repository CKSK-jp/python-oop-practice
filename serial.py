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
    def __init__(self, start):
        "Initiate the generator with a starting value"
        self.start = start - 1
        self.updated = self.start

    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start={self.start} updated={self.updated}>"

    def generate(self):
        self.updated += 1
        return self.updated

    def reset(self):
        self.updated = self.start
    
