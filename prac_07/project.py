"""project.py for Project class
Estimate: 12 mins
Actual: 13 mins
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string representation of a Project instance."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: "
                f"${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Determine whether priority of Project instance is lower than other instance's."""
        return self.priority < other.priority

    def is_completed(self):
        """Determine if project is 100% complete."""
        return self.completion_percentage == 100
