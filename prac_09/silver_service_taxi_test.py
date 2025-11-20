"""
CP1404 Prac 9
Emoke Bohuss
Client (test) code for SilverServiceTaxi class.
"""

from silver_service_taxi import SilverServiceTaxi

FLAGFALL = SilverServiceTaxi.flagfall

# Test 1
test_taxi = SilverServiceTaxi("Hummer", 200, 2)
test_taxi.drive(18)
expected_fare = 48.78  # price_per_km (1.23) * fanciness (2) * distance (18) + flagfall (4.50)
actual_fare = test_taxi.get_fare()
print(f"{test_taxi} Current fare = {test_taxi.get_fare()}")
assert f"{expected_fare:.2f}" == f"{actual_fare:.2f}"

# Test 2
test_taxi_2 = SilverServiceTaxi("Hummer2", 200, 1)
test_taxi_2.drive(18)
assert not f"{test_taxi.get_fare():.2f}" == f"{test_taxi_2.get_fare():.2f}"

# Test 3
test_taxi_no_flagfall = test_taxi.get_fare() - FLAGFALL
test_taxi_2_no_flagfall = test_taxi_2.get_fare() - FLAGFALL
assert f"{test_taxi_no_flagfall:.2f}" == f"{test_taxi_2_no_flagfall * 2:.2f}"
