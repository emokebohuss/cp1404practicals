"""Prac 7 - Client code for project.py
Estimate: 135
Actual:
"""
import datetime

from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    # print(projects[1])
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice!")
        choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


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
