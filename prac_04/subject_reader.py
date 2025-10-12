"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_records = load_subject_records(FILENAME)
    print(subject_records)
    display_subject_details(subject_records)


def load_subject_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        subject_details = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        subject_details[2] = int(subject_details[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subject_records.append(subject_details)
    input_file.close()
    return subject_records


def display_subject_details(subject_records):
    """Print subject details."""
    for subject in subject_records:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
