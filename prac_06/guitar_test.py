"""CP1404 Practical - Guitar class testing.
Expected: 10 mins
Actual: 9 mins
"""
from prac_06.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)
print(guitar)

print(f"Gibson L-5 CES get_age() - Expected 100. Got {guitar.get_age(2022)}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age(2022)}")
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar.is_vintage(2022)}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage(2022)}")
