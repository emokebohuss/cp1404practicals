"""
cp1404 prac_04
quick_picks.py
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Generate and display a grid of random numbers."""
    number_of_quick_picks = get_valid_number_of_quick_picks()
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print((("{:2} " * NUMBERS_PER_LINE).rstrip()).format(*sorted(quick_pick)))
        # print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate quick pick of unique random numbers."""
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = generate_valid_number(quick_pick)
        quick_pick.append(number)
    return quick_pick


def get_valid_number_of_quick_picks():
    """Get valid number_of_quick_picks >= 0."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number of quick picks!")
        number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


def generate_valid_number(quick_pick):
    """Generate a random number not already in quick_pick."""
    number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    while number in quick_pick:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
    return number


main()
