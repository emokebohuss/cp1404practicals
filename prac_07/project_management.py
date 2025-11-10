"""Prac 7 - Client code for project.py
Estimate: 135
Actual: 56 +
"""
import datetime

from project import Project

FILENAME = "projects.txt"
MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
        "- (A)dd new project\n- (U)pdate project\n- (Q)uit")


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    for project in projects:
        print(project)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            new_in_filename = get_valid_string("File name: ")
            load_projects(new_in_filename)
        elif choice == "S":
            new_out_filename = get_valid_string("File name: ")
            save_projects(new_out_filename)

        elif choice == "D":
            print("Incomplete projects:")
            incomplete_projects = (project for project in projects if not Project.is_completed(project))
            display_projects(incomplete_projects)
            print("Completed projects:")
            complete_projects = (project for project in projects if Project.is_completed(project))
            display_projects(complete_projects)

        elif choice == "F":
            date_choice = datetime.datetime.strptime(
                get_valid_string("Show projects that start after date (dd/mm/yy): "), "%d/%m/%Y").date()
            recent_projects = (project for project in projects if project.start_date >= date_choice)
            for project in recent_projects:
                print(project)

        elif choice == "A":
            print("Let's add a new project")
            name = get_valid_string("Name: ")
            start_date = datetime.datetime.strptime(get_valid_string("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
            priority = get_valid_integer("Priority: ", 9)
            cost = get_valid_integer("Cost estimate: ", 1000000)
            percent = get_valid_integer("Percent complete: ", 100)
            new_project = Project(name, start_date, priority, cost, percent)
            projects.append(new_project)

        elif choice == "U":
            # Display numbered projects
            for i, project in enumerate(projects):
                print(i, project)
            # Get project choice number and print chosen project
            project_choice_number = get_valid_integer("Project choice: ", (len(projects) - 1))
            chosen_project = projects[project_choice_number]
            print(chosen_project)

            update_project(chosen_project)

        else:
            print("Invalid menu choice!")
        print(MENU)
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
            parts[1] = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()  # Ignore warning
            # Construct a Project object using the elements
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def display_projects(projects):
    """Display projects."""
    for project in sorted(projects):
        print(f"  {project}")


def update_project(chosen_project):
    """Get new percentage, priority and update chosen project."""
    new_percentage = input("New Percentage: ").strip()
    if new_percentage == "":
        chosen_project.completion_percentage = chosen_project.completion_percentage
    else:
        new_percentage = get_valid_integer("New Percentage: ", 100)
        chosen_project.completion_percentage = new_percentage
    print(chosen_project)

    new_priority = input("New Priority: ").strip()
    if new_priority == "":
        chosen_project.priority = chosen_project.priority
    else:
        new_priority = get_valid_integer("New Priority: ", 9)
        chosen_project.priority = new_priority
    print(chosen_project)


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
    return choice  # Ignore warning


def get_valid_string(prompt):
    """Get non-empty string."""
    text = input(prompt).strip()
    while text == "":
        print("Input can not be blank")
        text = input(prompt).strip()
    return text.strip()


def save_projects(filename, projects):
    """Dave projects to file"""
    with open(filename, 'w') as out_file:
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                  f"{project.cost_estimate}\t{project.cost_estimate}")


if __name__ == '__main__':
    main()
