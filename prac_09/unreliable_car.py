"""
CP1404 Prac 9
Emoke Bohuss
UnreliableCar class
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car but with current reliability."""
        return f"{super().__str__()}, {self.reliability}% reliable to start."

    def __repr__(self):
        """Return string representation of an UnreliableCar instance."""
        return str(vars(self))

    def drive(self, distance):
        """Drive the car a given distance only if a randomly generated number is less than the car's reliability.

        Drive given distance if car has enough fuel
        or drive until fuel runs out, return the distance actually driven.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
