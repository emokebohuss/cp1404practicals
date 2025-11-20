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
    total_bill = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print()
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    print("Taxis available:")
    display_taxis(taxis)
    chosen_taxi = int(input("Choose taxi: "))
    current_taxi = taxis[chosen_taxi]
    print(current_taxi)
    return current_taxi


def drive_taxi(current_taxi, total_bill):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        total_bill += current_taxi.get_fare()
    return total_bill


main()
