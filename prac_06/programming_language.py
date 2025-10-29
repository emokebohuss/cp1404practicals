"""CP1404/CP5632 Practical - ProgrammingLanguage class."""


class ProgrammingLanguage:
    """ProgrammingLanguage class"""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise a ProgrammingLanguage object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"
