""" The program asks the user for a password, with error-checking to
 repeat if the password doesn't meet a minimum length set by a variable.
 The program then prints asterisks as long as the word.


MIN_PASSWORD_LENGTH = 6

get password
while len(password) < 6
    display error message
    get password
display len(Password) * "*"
"""

MIN_PASSWORD_LENGTH = 6

password = input("Password: ")
while len(password) < 6:
    print("Invalid password")
    password = input("Password: ")
print(len(password) * "*", end="")
