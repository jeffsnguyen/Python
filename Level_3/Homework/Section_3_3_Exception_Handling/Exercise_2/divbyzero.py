# Type: Homework
# Level: 3
# Section: 3.3: Exception Handling
# Exercise: 2
# Description: Contains the tests for handling div/0 exception
#   Extend exercise 1) to handle the situation when the user inputs something other than a number,
#       using exception handling. If the user does not enter a number, the code should provide the user
#       with an error message and ask the user to try again.
#   Note that this is an example of duck typing.

#######################
# Importing necessary packages

#######################

###############################################


###############################################
def main():

    # Program takes 2 input from user, handle input exception
    # If no input exception, handle division by 0 exception and print result of division
    # Also catch other unknown exceptions

    # 1st try-except block to handle input
    try:
        x = float(input('Input a number: '))  # take input and convert to float
        y = float(input('Input a number: '))
    except ValueError as valueEx:  # handle non-number exception, for example: string
        print(valueEx)
        pass
    except Exception as ex:  # handle other unknown exception
        print('Unknown error: ' + str(ex))
        pass
    else:
        # 2nd try-except block to handle division
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