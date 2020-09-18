# Type: Homework
# Level: 3
# Section: 3.3: Exception Handling
# Exercise: 3
# Description: Contains the tests for handling multiple exception via calculating a factorial
#   Create a function that calculates the factorial of an input number. If the input value is invalid, raise
#       an exception. Test this out in main(), and handle the exception. Provide several examples, using
#       explicit error handling and general error handling (catching all error types).

#######################
# Importing necessary packages

#######################

###############################################
# Return the factorial of num
def factorial(num):
    if not isinstance(int(num), int):
        raise ValueError('Must be an integer')
    elif not int(num) >= 0:
        raise ValueError('Must be a positive number')
    else:
        result = 1
        for n in range(2, int(num)+1):
            result *= n
        return result
###############################################
def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test 1. Handling both specific and general exception
    #       2. Test 2. Handling both only general exception
    ###############################################

    # Test 1. Handling both specific and general exceptions
    print('Test 1. Handling both specific and general exceptions.')
    # Program takes 1 input from user, handle input exception
def main():
    x = input('Input a number: ')  # take input
    try:
        print(str(x) + '! = ' + str(factorial(x)))
    except ValueError as valEx:  # handle non-number exception, for example: string
        print(valEx)
        pass
    except Exception as Ex:  # handle other unknown exception
        print('Unknown error: ' + str(Ex))
    pass
    print()

    # Test 2. Handling both only general exceptions
    print('Test 2. Handling only general exceptions.')
    # Program takes 1 input from user, handle strictly general exceptions
    x = input('Input a number: ')  # take input
    try:
        print(str(x) + '! = ' + str(factorial(x)))
    except Exception as Ex:  # handle other unknown exception
        print(Ex)
    pass
    print()


###############################################

#######################
if __name__ == '__main__':
    main()