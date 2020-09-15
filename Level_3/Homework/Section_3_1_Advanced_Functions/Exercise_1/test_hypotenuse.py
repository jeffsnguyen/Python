# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 1
# Description: This contains the method to test the hypotenus of a right triangle
#   Create a stored lambda function that calculates the hypotenuse of a right triangle; it should take
# base and height as its parameter. Invoke (test) this lambda with different arguments.

# Importing necessary packages

#######################
from math import sqrt

def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the calcHypotenuse lambda function
    ###############################################
    # Test 1.1
    # Scenario: Test the calcHypotenuse method to calculate the hypotenuse of a right triangle using lambda function.

    print('Test 1.1')
    calcHypotenuse = lambda base, height: sqrt(base**2 + height**2)
    print(calcHypotenuse(3, 4))
    print(calcHypotenuse(20, 21))
    print(calcHypotenuse(119, 120))
    print(calcHypotenuse(696, 697))
    print(calcHypotenuse(4059, 4060))
    print()


    ###############################################


#######################
if __name__ == '__main__':
    main()
