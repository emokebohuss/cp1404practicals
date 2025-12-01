"""
CP1404 Prac09
Taxi simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Main for taxi_simulator program. Allow user to choose taxis and drive them, calculating the fare for each trip
    and the total bill."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            chosen_taxi = choose_taxi(taxis)
            if chosen_taxi is not None:
                current_taxi = chosen_taxi
        elif choice == "D":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxis and their details."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Get valid taxi index from user and return chosen taxi."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_index = int(input("Choose taxi: "))
        chosen_taxi = taxis[taxi_index]
        return chosen_taxi
    except ValueError:
        print("Invalid taxi choice")
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(current_taxi, total_bill):
    """Complete a drive taxi interaction.
    If no taxi is selected, display error message. If taxi is selected, drive given distance, display taxi and trip
     details, then calculate and return the total bill including this trip's fare."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        current_taxi.start_fare()
        distance = get_valid_distance()
        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
        total_bill += current_taxi.get_fare()
    return total_bill


def get_valid_distance():
    """Get positive integer and return as distance."""
    is_valid_input = False
    while not is_valid_input:
        try:
            distance = int(input("Drive how far? "))
            if distance < 0:
                print("Distance must be at least 0km.")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid distance")
    return distance  # No problem with potential undefined variable


main()
