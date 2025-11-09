"""Prac 7 - Client code for project.py
Estimate: 75
Actual:
"""
import datetime

from project import Project

FILENAME = "projects.txt"


def main():
    projects = load_projects(FILENAME)
    print(projects[1])


def load_projects(filename):
    """Load projects from file into a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # remove header
        for line in in_file:
            parts = line.strip().split("\t")  # handle tab delimited txt file data
            # Convert date to datetime.date
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            # Construct a Project object using the elements
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


if __name__ == '__main__':
    main()
