"""project.py for Project class
Estimate: 12 mins
Actual: 8 +
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Guitar instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Represent Project data as a string."""
        return (f"{self.name} started on {self.start_date}, priority {self.priority}, estimated: "
                f"${self.cost_estimate:,.2f}, completed % {self.completion_percentage}")
