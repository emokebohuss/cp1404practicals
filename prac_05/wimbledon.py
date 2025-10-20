"""Write a program to read this file, process the matches and display processed information:

the champions and how many times they have won.
the countries of the champions in alphabetical order
Estimated: 45 mins
Actual: 68 mins
"""

# import csv

FILENAME = "wimbledon.csv"


def main():
    """Load matches data from file, print champions and their number of wins, and the set of champions' countries"""
    matches = load_matches_data(FILENAME)
    champion_to_wins = create_champion_to_wins(matches)

    print("Wimbledon Champions:")
    for champion in champion_to_wins:
        print(champion, champion_to_wins[champion])

    champions_countries = find_champions_countries(matches)
    print(f"\nThese {len(champions_countries)} countries have won Wimbledon:")
    print(", ".join(champions_countries))


def load_matches_data(filename):
    """Load matches from file and return formatted list of matches."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        matches = []
        in_file.readline()
        for line in in_file:
            line = line.strip()
            match_details = line.split(",")
            match_details[0] = int(match_details[0])  # ignore error, convert year to int
            match_details[5] = ",".join(match_details[5:])  # create sting of scores
            del match_details[6:]  # delete redundant scores
            matches.append(match_details)
        return matches


# def load_matches_data(filename):  # csv reader version. Uncomment import if ran and comment out other version of func
#     """Using csv module, load matches from file and return list of matches."""
#     with open(filename, "r", encoding="utf-8-sig") as in_file:
#         matches = []
#         rows = csv.reader(in_file)
#         next(rows)  # remove header
#         for row in rows:
#             row[0] = int(row[0])  # Ignore error, convert year to int
#             matches.append(row)
#         return matches


def create_champion_to_wins(matches):
    """Create dictionary of champions and their number of wins."""
    champion_to_wins = {}
    for match in matches:
        champion = match[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def find_champions_countries(matches):
    """Create an alphabetically sorted set of champions' countries."""
    champions_countries = set()
    for match in matches:
        country = match[1]
        champions_countries.add(country)
    return sorted(champions_countries)


main()
