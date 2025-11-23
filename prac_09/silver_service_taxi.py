"""
CP1404 Practical 9
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}."

    def __repr__(self):
        """Return string representation of data in a SilverServiceTaxi."""
        return str(vars(self))

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip, including flagfall."""
        return super().get_fare() + self.flagfall
