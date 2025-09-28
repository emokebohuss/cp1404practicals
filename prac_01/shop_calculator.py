"""
shop_calculator by Emoke Bohuss / CP1404_prac_01

This program gets the number of items and the price of each item, then displays the total price.
If the total price is over $100, then 10% discount is applied to the total before the amount is displayed.


total_price = 0

get number_of_items
while number_of_items is < 0:
    display error message
    get number_of_items
for item in number_of_items
    get price
    total_price = total_price + price
if total_price > $100
    total_price = total_price * 0.9
display total_price
"""

total_price = 0
DISCOUNT_THRESHOLD = 100  # $100

# Get valid input (positive number)
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Get price of each item
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price

# If total_price > DISCOUNT_THRESHOLD, apply 10% discount
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price * 0.9  # Calculate 90% of total price.
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
