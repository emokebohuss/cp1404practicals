"""
cp1404 prac_04
quick_picks.py
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 0:
    print("Invalid number of quick picks!")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in quick_pick:  # ensure quick_pick does not contain any repeated number
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick.append(number)
    print((("{:2} " * NUMBERS_PER_LINE).rstrip()).format(*sorted(quick_pick)))
