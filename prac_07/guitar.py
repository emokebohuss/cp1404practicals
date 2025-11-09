"""CP1404 Practical - Guitar class.
Expected: 6 mins
Actual: 6 mins 45 sec
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Represent Guitar data as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self, current_year):
        """Calculate the age of the Guitar instance."""
        return current_year - self.year

    def is_vintage(self, current_year):
        """Determine whether a Guitar is vintage (50 or more years old)."""
        return self.get_age(current_year) >= 50  # Vintage over 50 or more years old


