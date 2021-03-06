#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance():
    a = float((x,y))
    b = float((x1,y1))

    ans = ((a[1]-b[1])**2 + (a[2]-b[2])**2)**(1/2)

    return ans