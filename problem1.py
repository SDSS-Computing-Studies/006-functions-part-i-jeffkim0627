#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse():
    if boolean == True:
        hyp = (a**2 + b**2)**(1/2)
        return hyp
    else:
        if a>b:
            missingside = (a**2 - b**2)**(1/2)
        else:
            b
            missingside = (b**2 - a**2)**(1/2)
        return missingside