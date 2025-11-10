"""CP1404 Prac 6 Guitars client code.
Estimated: 25 mins
Actual: 31 mins
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.\n")
    name = input("Name: ")

print(f"These are my guitars:")
name_max_length = max(len(guitar.name) for guitar in guitars)
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}: {guitar.name:>{name_max_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
