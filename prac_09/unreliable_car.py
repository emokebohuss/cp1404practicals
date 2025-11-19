"""
CP1404 Prac 9
Emoke Bohuss
UnreliableCar class
"""

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, reliability, **kwargs):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = 0.0
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current reliability."""
        return f"{super().__str__()}, {self.reliability}% reliable to start."

    def __repr__(self):
        """Return string representation of an UnreliableCar instance."""
        return str(vars(self))







