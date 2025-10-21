"""
emails.py
cp1404
Prac5

Estimate: 30 minutes
Actual: 64 minutes  # got it working in about 36 mins but struggled with handling of multiple special chars
"""

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Get email, extract name from email then create a dictionary and print it."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name_from_email(email)
        response = input(f"Is your name {name}? (Y/n) ").strip().upper()
        if response not in ("Y", ""):
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()
    print()
    display_data(email_to_name)


def extract_name_from_email(email):
    """Extract user's name from email address."""
    user_name = email.split("@")[0]
    name_letters = []
    for character in user_name:
        if character in SPECIAL_CHARACTERS:
            if not (len(name_letters) > 0 and name_letters[-1] == " "):  # avoid multiple spaces
                name_letters.append(" ")  # replace special character with space
        else:
            name_letters.append(character)
    name = "".join(name_letters).strip().title()
    return name


def display_data(email_to_name):
    """Display name and associated email from dictionary."""
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
