"""cp1404 prac_05
Hexadecimal colour code lookup
"""

COLOUR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "aqua": "#00ffff",
                 "apricot": "#fbceb1", "beaver": "#9f8170", "black": "#000000"}

colour = input("Colour name: ").lower()
while colour != "":
    try:
        print(f"{colour} is {COLOUR_TO_HEX[colour]}")
    except KeyError:
        print("Invalid colour name!")
    colour = input("Colour name: ").lower()
