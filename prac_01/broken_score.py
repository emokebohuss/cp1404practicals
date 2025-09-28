"""
broken_score by Emoke Bohuss / CP1404_prac_01
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")


# Tested values: -1, -0.1, 0, 100, 100.1, 101, 90, 89, 50, 49
