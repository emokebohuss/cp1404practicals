"""
CP1404 Prac09
Band Class
"""


class Band:
    """Band class."""

    def __init__(self, name):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join((str(musician) for musician in self.musicians))})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to Band."""
        self.musicians.append(musician)
