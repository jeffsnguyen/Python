# Type: Homework
# Level: 3
# Section: 3.3: Exception Handling
# Exercise: 1
# Description: Contains the tests for handling div/0 exception
#   Create code that takes a numerator and denominator input from the user. Output the quotient in
#       decimal form. Handle the divide-by-zero case gracefully, using exception handling.

#######################
# Importing necessary packages

#######################

###############################################


###############################################
def main():

    # Program takes 2 input from user, DOES NOT handle input exception
    # Handle division by 0 exception and print result of division
    # Also catch other unknown exceptions

    x = float(input('Input a number: '))  # take input and convert to float
    y = float(input('Input a number: '))

    # try-except block to handle division
    try:
        print('Division result = ', x/y)
    except ZeroDivisionError as divZeroEx:  # handle div/0 exception
        print(divZeroEx)
        pass
    except Exception as ex:  # handle other unknown exception
        print('Unknown error: ' + str(ex))


###############################################

#######################
if __name__ == '__main__':
    main()