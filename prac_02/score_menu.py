"""Get score, print result or show stars, based on user choice.


def main()
    get valid score
    display menu
    get choice
    while choice != Q
        if choice == G
            get valid score
        else if choice == P
            print result
        else if choice == S
            show stars
        else
            display invalid input error message
        display menu
        get choice
    display farewell message


main()
"""

MENU = "-----------------\n(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit\n-----------------"


def main():
    """Get score, print result or show stars, based on user choice."""
    score = get_valid_score()
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").upper()
    print("Farewell.")


def get_valid_score():
    """Get valid score."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine result based on score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print stars."""
    print(score * "*")


main()
