# Type: Homework
# Level: 4
# Section: 4.1: Python Strings
# Exercise: 5
# Description: Contains the tests for modified Timer class
#   Convert your Timer class’ print statement to use f-Strings instead of concatenating strings.

#######################
# Importing necessary packages
from utils.timer import Timer
#######################

###############################################

###############################################
def main():

    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #       2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #           and its ability to config time display format
    #       3. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #           and its ability to config time display format.  This time using incorrect timer config format.
    ###############################################

    # Test 1
    # 1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    print('1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1')

    with Timer('babySharkTimer'):
        # Doing work below
        # try-except block to catch errors
        try:
            with open("babyShark.txt", 'w') as f:  # open file
                f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
        except IOError:  # catch input output error
            print(IOError('Input output error'))
            pass
        except Exception:   # catch other unanticipated error
            print(Exception('Unknown error.'))
            pass
        # context manager automatically clean up after itself, no need to close the file
        print(f'Has the file been closed? {f.closed}.')
    print()

    # Test 2
    # 2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #   and its ability to config time display format
    print('2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1 '
          'and its ability to config time display format')

    with Timer('babySharkTimer') as timer:
        # Doing work below

        try:
            timer.timerConfig('hrs')
        except Exception:
            print(Exception('Timer config invalid.'))
            print('Using seconds as default. Continue...')
        finally:
            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError:  # catch input output error
                print(IOError('Input output error'))
                pass
            except Exception:   # catch other unanticipated error
                print(Exception('Unknown error.'))
                pass
            # context manager automatically clean up after itself, no need to close the file
            print(f'Has the file been closed? {f.closed}.')
    print()

    # Test 3
    # 2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #   and its ability to config time display format. This time using incorrect timer config format.
    print('2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1 '
          'and its ability to config time display format.  This time using incorrect timer config format.')

    with Timer('babySharkTimer') as timer:
        # Doing work below

        try:
            timer.timerConfig('Hello')
        except ValueError as valEx:
            print(valEx)
            print('Using seconds as default. Continue...')
        finally:
            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError:  # catch input output error
                print(IOError('Input output error'))
                pass
            except Exception:  # catch other unanticipated error
                print(Exception('Unknown error.'))
                pass
            # context manager automatically clean up after itself, no need to close the file
            print(f'Has the file been closed? {f.closed}.')

    # The Context Manager approach is compared to previous method is:
    #       1. Cleaner, does not requires explicitly calling start() and end()
    #       2. Enable on-demand resources allocation
    #       3. Exception handling is easier
###############################################

#######################
if __name__ == '__main__':
    main()