"""
CP1404/CP5632 - Practical
Program to determine score status

def main()
    get score
    result = determine result(score)
    print result


main()
"""

import random


def main():
    """Ask user for their score and print result."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    # Generate random score and print result.
    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"{random_score:.2f} is {random_result}")


def determine_result(score: float):
    """Determine result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
