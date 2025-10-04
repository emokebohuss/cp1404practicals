"""
Prac_03
randoms.py
"""
# Q1
# What did you see on line 1?
# What was the smallest number you could have seen, what was the largest?

# Answer: smallest possible integer is 5 and the largest is 20.


# Q2
# What did you see on line 2?
# What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?

# Answer: smallest possible integer is 3 and the largest is 9.
# 4 cannot be produced because the program prints integers in steps of 2, starting from 3,
# therefore only odd numbers are possible (i.e. 3, 5, 7, 9)


# Q3
# What did you see on line 3?
# What was the smallest number you could have seen, what was the largest?
# Answer: smallest possible is 2.5 and largest possible is 5.5


# Write code, not a comment, to produce a random number between 1 and 100 inclusive
import random

print(random.randint(1, 100))
