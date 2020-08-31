'''
Type: Homework
Level: 1
Section: 1.6 Packages
Exercise: 1
Description: Import the math module and demonstrate usage of many of its built-in functions.
'''

import math

# Main
def main():
    print('Demonstrate some built-in function of Python math module\n')

    # math.factorial(x)
    # Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
    print('math.factorial(x): Return x factorial as an integer. '
          'Raises ValueError if x is not integral or is negative.')
    print('5! = ',math.factorial(5))

    # math.exp(x)
    # Return e raised to the power x, where e = 2.718281… is the base of natural logarithms.
    # This is usually more accurate than math.e ** x or pow(math.e, x).
    print('math.exp(x): Return e raised to the power x, where e = 2.718281… '
          'is the base of natural logarithms. This is usually more accurate than math.e ** x or pow(math.e, x).')
    print('e^2 = ', math.exp(2))

    # math.sqrt(x)
    # Return the square root of x.
    print('math.sqrt(x): Return the square root of x.')
    print('sqrt(49) = ', math.sqrt(49))

    # math.sin(x)
    # Return the sine of x radians.
    print('math.sin(x): Return the sine of x radians.')
    print('sin(pi/2) = ', math.sin(math.pi/2))

    # math.degrees(x)
    # Convert angle x from radians to degrees.
    print('math.degrees(x): Convert angle x from radians to degrees.')
    print('pi/2 radians = ' + str(math.degrees(math.pi/2)) + ' degrees.')

#######################
if __name__ == '__main__':
    main()