"""Prac 7 - Client code for project.py
Estimate: 135 mins
Actual: 92 mins + 2 hours playing with exception handling.
"""
from project import Project
from datetime import datetime
from operator import attrgetter

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = get_valid_string("File name: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = get_valid_string("File name: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date_choice = datetime.strptime(
                get_valid_string("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
            filter_by_date(date_choice, projects)
        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(i, project)
            # Get project choice number and print chosen project
            index = get_valid_integer("Project choice: ", (len(projects) - 1))
            chosen_project = projects[index]
            print(chosen_project)
            update_project(chosen_project)
        else:
            print("Invalid menu choice!")
        print(MENU)
        choice = input(">>> ").upper()
    saving_choice = input(f"Would you like to save to {FILENAME}? ")
    if saving_choice in "y,Y":
        save_projects(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file into a list of Project objects."""
    projects = []
    with open(filename, 'r', encoding="UTF-8") as in_file:
        in_file.readline()  # remove header
        for line in in_file:
            parts = line.strip().split("\t")  # handle tab delimited txt file data
            # Convert date to datetime.date
            parts[1] = datetime.strptime(parts[1], "%d/%m/%Y").date()  # Ignore warning
            # Construct a Project object using the elements
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects, filename):
    """Save projects to file."""
    with open(filename, 'w', encoding="UTF-8") as out_file:
        print(HEADER, file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    print("Incomplete projects:")
    incomplete_projects = [project for project in projects if not project.is_completed()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    complete_projects = [project for project in projects if project.is_completed()]
    complete_projects.sort()
    for project in complete_projects:
        print(f"  {project}")


def filter_by_date(date_choice, projects):
    """Filter and sort projects by date, then display them."""
    filtered_projects = [project for project in projects if project.start_date >= date_choice]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Get project details and add new project instance to projects."""
    name = get_valid_string("Name: ")
    start_date = datetime.strptime(get_valid_string("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = get_valid_integer("Priority: ", 9)
    cost = float(get_valid_integer("Cost estimate: ", 1000000))
    percent = get_valid_integer("Percent complete: ", 100)
    new_project = Project(name, start_date, priority, cost, percent)
    projects.append(new_project)


def update_project(chosen_project):
    """Get new percentage, priority and update chosen project."""
    try:
        new_percentage = int(input("New Percentage: "))
        chosen_project.completion_percentage = new_percentage
    except ValueError:
        pass
    try:
        new_priority = int(input("New Priority: "))
        chosen_project.priority = new_priority
    except ValueError:
        pass


def get_valid_integer(prompt, upper_condition):
    """Get valid integer."""
    is_valid_input = False
    while not is_valid_input:
        try:
            choice = int(input(prompt))
            if choice < 0 or choice > upper_condition:
                print(f"Number must be between 0 and {upper_condition}")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return choice  # No issue with potential undefined variable


def get_valid_string(prompt):
    """Get non-empty string."""
    text = input(prompt).strip()
    while text == "":
        print("Input can not be blank")
        text = input(prompt).strip()
    return text.strip()


if __name__ == '__main__':
    main()
