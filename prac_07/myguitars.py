"""myguitars.py by Emoke Bohuss
client code gor Guitar.py"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    get_new_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)


def load_guitars(filename):
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return guitars


if __name__ == '__main__':
    main()
