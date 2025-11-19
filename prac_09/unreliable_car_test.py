"""
CP1404 Prac 9
Emoke Bohuss
Client (test) code for unreliable car
"""
from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Run tests for UnreliableCar instances with various reliability"""
    mid_car = UnreliableCar("Ranger", 100, 50)
    good_car = UnreliableCar("Mazda", 100, 90)
    bad_car = UnreliableCar("BMW", 100, 10)
    print_successful_drive_percentage(mid_car)
    print_successful_drive_percentage(good_car)
    print_successful_drive_percentage(bad_car)


def print_successful_drive_percentage(car):
    """Attempt to drive 1km 100 times and display % of successful attempts."""
    no_of_successful_drives = 0
    for i in range(100):
        fuel = car.fuel
        car.drive(1)
        if car.fuel < fuel:
            no_of_successful_drives += 1
    chance = no_of_successful_drives / 100
    print(f"{car.name} with {car.reliability}% reliability successfully drove {chance * 100:.2f}% of attempts.")


run_tests()
