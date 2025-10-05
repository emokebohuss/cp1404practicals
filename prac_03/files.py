"""
files.py
Prac_03
"""

# 1.
""" Ask user for name and write it into a file"""
name = input("Name: ")
while name == "":
    print("Invalid name")
    name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()


# 2.
"""Read name from file"""
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# 3.
"""Read the first two lines from a file and add them together."""
with open("numbers.txt", 'r') as in_file:
    total_number = int(in_file.readline().strip())
    total_number = total_number + int(in_file.readline().strip())
    print(f"Result: {total_number}")


# 4.
"""Read all lines from a file and add them together"""
with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total = total + int((line.strip()))
print(f"Total: {total}")
