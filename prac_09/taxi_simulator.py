"""
CP1404 Prac09
Taxi simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("choice")
        elif choice == "D":
            print("drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
