"""myguitars.py by Emoke Bohuss
client code gor Guitar.py"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars from CSV file, get new guitars from user, display them and save them to CSV file. """
    guitars = load_guitars(FILENAME)
    get_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Load guitars from CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display guitars."""
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    """Get new guitars from user and append to guitars list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Write guitars details to CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == '__main__':
    main()
