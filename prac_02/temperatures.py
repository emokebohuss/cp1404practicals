"""
CP1404/CP5632 - Practical
Program for temperature conversion


def main()
    display menu
    get choice
    while choice != "Q"
        if choice = "C"
            get Celsius
            convert Celsius to Fahrenheit(Celsius)
            print result
        else if choice = "F"
            get Fahrenheit
            convert Fahrenheit to Celsius(Fahrenheit)
            print result
        else:
            display error message
        display menu
        get choice
    display goodbye message


main()
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert Celsius to Fahrenheit or vice versa, based on menu choice."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


main()
