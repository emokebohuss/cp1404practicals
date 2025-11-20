"""
CP1404 Prac 9
Emoke Bohuss
Client (test) code for SilverServiceTaxi class.
"""

from silver_service_taxi import SilverServiceTaxi

# Test 1
test_taxi = SilverServiceTaxi("Hummer", 200, 2)
test_taxi.drive(18)
expected_fare = 48.80  # round(price_per_km (1.23) * fanciness (2) * distance (18)) + flagfall (4.50)
actual_fare = test_taxi.get_fare()
print(f"{test_taxi} Current fare = ${test_taxi.get_fare():.2f}")
assert expected_fare == actual_fare
