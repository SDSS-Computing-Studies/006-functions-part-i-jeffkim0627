#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
import math

def isItnteger(number):
    if (number/2) == (math.ceil(number/2)):
        return True
    else:
        return False