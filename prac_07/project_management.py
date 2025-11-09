"""Prac 7 - Client code for project.py
Estimate: 75
Actual:
"""
import datetime

from project import Project

FILENAME = "projects.txt"

# def main():
#     projects = load_projects(FILENAME)
#     print(projects[1])
#
#
# def load_projects(filename):
#     """Load guitars from CSV file into a list of Guitar objects."""
#     projects = []
#     with open(filename, 'r') as in_file:
#         for line in in_file:
#             parts = line.strip().split("    ")
#             print(parts)
#             project = Project(parts[0], int(parts[1]), float(parts[2]))
#             projects.append(project)
#     return projects

with open(FILENAME, 'r') as in_file:
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        print(project)
