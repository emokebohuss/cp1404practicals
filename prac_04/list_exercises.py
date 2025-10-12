"""
cp1404 prac_04
list_exercises.py
"""

# 1. Basic list operations
"""Get a predefined number of numbers from the user, add them to a list and print information about these numbers."""

NUMBER_OF_NUMBERS = 5


numbers = []
for number in range(NUMBER_OF_NUMBERS):
    new_number = int(input("Number: "))
    numbers.append(new_number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[len(numbers) - 1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# 2. Woefully inadequate security checker
"""Get username from user, check if user is authorised and display Access granted/denied message."""

authorised_usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                        'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                        'StartServer', 'bob']

username = input("Username: ")
if username in authorised_usernames:
    print("Access granted")
else:
    print("Access denied")
