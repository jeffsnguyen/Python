# Type: Homework
# Level: 4
# Section: 4.1 Python Strings
# Exercise: 4
# Description: Contains the tests for various filepath operations
# Create a program that does the following:
#   a. Prompts the user for name, age (integer), and country of residence. Display the information
#       as follows: <name> is <age> years old and lives in <country>.
#   b. Do the same as above, but using a decimal number for the age. Display the number with one decimal place.
#   c. Do the same as above, but make the country name all caps.
#
# Write a separate version of the above using format flags, a version using the format function with
# numeric placeholders, a version using the format function with keyword placeholders, and a version
# using f-Strings – which is cleanest?
#######################
# Importing necessary packages

#######################

###############################################

###############################################
def main():

    # Testing block summary:
    # Scenario:
    #   This block will:
    #       1. Test a): take input prompt and display using various methods.
    #       2. Test b): take input prompt and display using various methods, displaying 1 decimal for age
    #       3. Test c): take input prompt and display using various methods, displaying 1 decimal for age and
    #                   country value in caps
    #
    # Testing block 1
    # Scenario:
    #   This block will: Test a): take input prompt and display using various methods.
    #       1.1 Test 1.1 Using format flag
    #       1.2 Test 1.2 Using format function with keyword placeholder
    #       1.3 Test 1.3 Using format function with numeric placeholder
    #       1.4 Test 1.4 Using f string
    #
    ###############################################
    # Test 1: Test a): take input prompt and display using various methods.
    # Prompts the user for name, age (integer), and country of residence. Display the information
    #       as follows: <name> is <age> years old and lives in <country>.
    #######################
    # 1.1 Test 1.1 Using format flag
    print('Test 1.1 Using format flag')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = int(age)
            except ValueError:   # catch non-integer input
                print(ValueError('Age must be an integer'))
            except Exception as Ex:   # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:   # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 1.1 Using format flag to display result
                    #######################
                    print('%s is %i years old and lives in %s.'%(name, age, country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    #######################
    # 1.2 Test 1.2 Using format function with keyword placeholder
    print('Test 1.2 Using format function with keyword placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = int(age)
            except ValueError:  # catch non-integer input
                print(ValueError('Age must be an integer'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 1.2 Using format function to display result
                    #######################
                    print('{name} is {age} years old and lives in {country}.'
                          .format(name = name, age = age, country = country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 1.3 Test 1.3 Using format function with numeric placeholder
    print('Test 1.3 Using format function with numeric placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = int(age)
            except ValueError:  # catch non-integer input
                print(ValueError('Age must be an integer'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 1.3 Using format function with numeric placeholder to display result
                    #######################
                    print('{0} is {1} years old and lives in {2}.'
                          .format(name, age, country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 1.4 Test 1.4 Using f string
    print('Test 1.4 Using f string')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = int(age)
            except ValueError:  # catch non-integer input
                print(ValueError('Age must be an integer'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 1.4 Using f string to display result
                    #######################
                    print(f'{name} is {age} years old and lives in {country}.')
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################

    # Testing block 2
    # Scenario:
    #   This block will: Test b): take input prompt and display using various methods, displaying 1 decimal for age
    #       2.1 Test 1.1 Using format flag
    #       2.2 Test 1.2 Using format function with keyword placeholder
    #       2.3 Test 1.3 Using format function with numeric placeholder
    #       2.4 Test 1.4 Using f string
    #
    ###############################################
    # Test 2: Test b): take input prompt and display using various methods, displaying 1 decimal for age
    # Prompts the user for name, age (integer), and country of residence. Display the information
    #       as follows: <name> is <age> years old and lives in <country>.
    #######################
    # 2.1 Test 2.1 Using format flag
    print('Test 2.1 Using format flag')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 2.1 Using format flag to display result
                    #######################
                    print('%s is %.1f years old and lives in %s.' % (name, age, country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    #######################
    # 2.2 Test 2.2 Using format function with keyword placeholder
    print('Test 2.2 Using format function with keyword placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 2.2 Using format function with keyword placeholder to display result
                    #######################
                    print('{name} is {age:,.1f} years old and lives in {country}.'
                          .format(name=name, age=age, country=country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 2.3 Test 2.3 Using format function with numeric placeholder
    print('Test 2.3 Using format function with numeric placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 2.3 Using format function with numeric placeholder to display result
                    #######################
                    print('{0} is {1:,.1f} years old and lives in {2}.'
                          .format(name, age, country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 2.4 Test 2.4 Using f string
    print('Test 2.4 Using f string')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 2.4 Using f string to display result
                    #######################
                    print(f'{name} is {round(age, 1)} years old and lives in {country}.')
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################

    # Testing block 3
    # Scenario:
    #   This block will: Test c): take input prompt and display using various methods, displaying 1 decimal for age and
    #                        country value in caps
    #       3.1 Test 1.1 Using format flag
    #       3.2 Test 1.2 Using format function with keyword placeholder
    #       3.3 Test 1.3 Using format function with numeric placeholder
    #       3.4 Test 1.4 Using f string
    #
    ###############################################
    # Test 3: Test c): take input prompt and display using various methods, displaying 1 decimal for age and
    #           country value in caps
    # Prompts the user for name, age (integer), and country of residence. Display the information
    #       as follows: <name> is <age> years old and lives in <country>.
    #######################
    # 3.1 Test 3.1 Using format flag
    print('Test 3.1 Using format flag')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 3.1 Using format flag to display result
                    #######################
                    print('%s is %.1f years old and lives in %s.' % (name, age, country.upper()))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    #######################
    # 3.2 Test 3.2 Using format function using keyword placeholder
    print('Test 3.2 Using format function using keyword placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 3.2 Using format function with keyword placeholder to display result
                    #######################
                    country = country.upper()
                    print('{name} is {age:.1f} years old and lives in {country}.'
                          .format(name=name, age=age, country=country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 3.3 Test 3.3 Using format function using numeric placeholder
    print('Test 3.3 Using format function using numeric placeholder')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 3.2 Using format function with numeric placeholder to display result
                    #######################
                    country = country.upper()
                    print('{0} is {1:,.1f} years old and lives in {2}.'.format(name, age, country))
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################
    # 3.4 Test 3.4 Using f string
    print('Test 3.4 Using f string')
    keepGoing = 1
    # Take all input in strings, use split to enable 1 line input
    while not keepGoing == '0':  # loop to keep prompting input for easier test
        try:  # try-except block to handle input
            name, age, country = input('Enter name, age and country separated by a single space '
                                       '(Example: Kobe 41 US): ').split()
        # handle case where user not enter input separate by space or not enough parameter (3 needed)
        except ValueError:
            print(ValueError('Enter 3 parameters, separate by a single space (Example: Kobe 41 US)'))
            pass
        except Exception:  # catch unknown exceptions
            print(Exception('Unknown Error'))
        else:
            try:  # handle case where user enter an age value that is not an integer
                age = float(age)
            except ValueError:  # catch non-float input
                print(ValueError('Age must be a number (integer or float).'))
            except Exception as Ex:  # catch unknown exceptions
                print(Exception('Unknown Error'))
            else:
                if not age >= 0:  # check if age is positive
                    print(ValueError('Age must be a positive value.'))
                else:
                    #######################
                    # 3.4 Using f string to display result
                    #######################
                    print(f'{name} is {round(age, 1)} years old and lives in {country.upper()}.')
        keepGoing = input('To stop enter 0, to continue enter anything else: ')
        print()
    #######################

    # f string version is the cleanest as variable is descriptive
    # inline expression can be evaluated inside the string
    # not having to memorized format flags
    ###############################################



###############################################

#######################
if __name__ == '__main__':
    main()