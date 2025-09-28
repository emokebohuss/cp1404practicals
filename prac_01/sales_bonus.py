"""
sales_bonus by Emoke Bohuss / CP1404_prac_01

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.


get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 10%
    else
        bonus = sales * 15%
    print bonus
    get sales
print exit message
"""

BONUS_THRESHOLD = 1000  # sales = $1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus = sales * 0.1  # 10 % bonus
    else:
        bonus = sales * 0.15  # 15 % bonus
    print(f"Your bonus is ${bonus}")
    sales = float(input("Enter sales: $"))
print("No more sales / invalid sale value")
