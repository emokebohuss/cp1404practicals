""" The program asks the user for a password, with error-checking to
 repeat if the password doesn't meet a minimum length set by a variable.
 The program then prints asterisks as long as the word.


MIN_PASSWORD_LENGTH = 6

get password
while len(password) < 6
    display error message
    get password
display len(Password) * "*"
"""

MIN_PASSWORD_LENGTH = 6


def main():
    """Get valid password and print stars of password length."""
    password = get_password()
    print_stars(password)


def print_stars(password: str):
    """Print stars."""
    print(len(password) * "*", end="")


def get_password() -> str:
    """Get valid password."""
    password = input("Password: ")
    while len(password) < 6:
        print("Incorrect password")
        password = input("Password: ")
    return password


main()
