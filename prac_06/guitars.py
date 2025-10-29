"""CP1404 Prac 6 Guitars client code.
Estimated: 25 mins
Actual:
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022

print("My guitars!")
guitars = []
# name = input("Name: ")
# while name != "":
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print(f"These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(CURRENT_YEAR) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


