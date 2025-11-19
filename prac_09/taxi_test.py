"""Client code for taxi class
CP1404 Prac09 Emoke Bohuss"""

from taxi import Taxi

# 1. Create new taxi object
my_taxi = Taxi("Prius 1", 100)

# 2. Drive taxi 40km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: {my_taxi.get_fare()}")

# 4. Restart the fare meter and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Print the details and the current fare
print(my_taxi)
print(f"Current fare: {my_taxi.get_fare()}")
