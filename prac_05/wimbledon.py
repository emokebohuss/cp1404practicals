"""Write a program to read this file, process the data and display processed information:

the champions and how many times they have won.
the countries of the champions in alphabetical order
Estimated: 45 mins
Actual:
"""


filename = "wimbledon.csv"

champion_to_wins = {}
data = []
champions_nationalities = []
with open(filename, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for line in in_file:
        line = line.strip()
        match_details = line.split(",")
        match_details[0] = int(match_details[0])  # Ignore error
        data.append(match_details)
        nationality = match_details[1]
        champions_nationalities.append(nationality)
        champion = match_details[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1


print("Wimbledon Champions:")
for champion in champion_to_wins:
    print(champion, champion_to_wins[champion])

print()
print("These 12 countries have won Wimbledon:")
print(", ".join(sorted(set(champions_nationalities))))
