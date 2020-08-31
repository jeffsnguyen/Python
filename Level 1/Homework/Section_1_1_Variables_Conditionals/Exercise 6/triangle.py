'''
Type: Homework
Level: 1
Section: 1.1 Variables/ Conditionals
Exercise: 6
Description: Create a program that takes two inputs from the user (using input):
            The base and height of a triangle. Output should be the area of the triangle.
            As input returns a string in all cases, you’ll need to convert it to a number using float.
            Be sure to have if statements which check that the input values are valid
                for the sides of a triangle (if not, print an error message to the user).
'''

import sys

def main():

    # Collect base, height input from user, terminate if there is not two value entered
    try:
        base, height = input('Input value of base and height of the triangle (separate by space): ').split()
    except:
        sys.exit('Must enter exactly 2 values, separated by space')

    # Check if the inputs are numbers, terminate if not
    try:
        float(base)
        float(height)
    except:
        sys.exit('Must be a number')

    # Convert inputs to float
    base = float(base)
    height = float(height)

    # Check if inputs are positive, terminate if not, output area of triangle result if yes
    if base <= 0 or height <=0:
        sys.exit('Input must be positive.')
    else:
        print('Triangle area = ', base*height/2) # Area = base*height/2


#######################
if __name__ == '__main__':
    main()