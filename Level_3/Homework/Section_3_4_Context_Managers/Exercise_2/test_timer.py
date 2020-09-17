# Type: Homework
# Level: 3
# Section: 3.4: Context Managers
# Exercise: 2
# Description: Contains the tests for modified Timer class
#   Modify the Timer class to work as a context manager. Essentially, it should be possible to do the following:
#
#       with Timer('timerName')
#           print('Do Work Here')

#       An example output would look like: timerName: 1.5467 seconds
#
#   The timer class should still have a configurable display. The context manager should be coded so
#       that the following code works, to configure the display when using the context manager:
#
#       with Timer('timerName') as timer:
#           timer.configureTimerDisplay('hrs')
#           print('Do Work Here')
#
#   How does this compare to the previous approach of using the regular Timer class?

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
        except IOError as ioEx:  # catch input output error
            print(ioEx)
            pass
        except Exception as Ex:   # catch other unanticipated error
            print(Ex)
            pass
        # context manager automatically clean up after itself, no need to close the file

        print('Has the file been closed? ', f.closed)
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
        except Exception as keyEx:
            print('Time config invalid' + str(keyEx))
            print('Using seconds as default. Continue...')
        finally:

            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError as ioEx:  # catch input output error
                print(ioEx)
                pass
            except Exception as Ex:   # catch other unanticipated error
                print(Ex)
                pass
            # context manager automatically clean up after itself, no need to close the file

            print('Has the file been closed? ', f.closed)
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
        except Exception as keyEx:
            print('Time config invalid' + str(keyEx))
            print('Using seconds as default. Continue...')
        finally:

            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError as ioEx:  # catch input output error
                print(ioEx)
                pass
            except Exception as Ex:  # catch other unanticipated error
                print(Ex)
                pass
            # context manager automatically clean up after itself, no need to close the file

            print('Has the file been closed? ', f.closed)

    # The Context Manager approach is compared to previous method is:
    #       1. Cleaner, does not requires explicitly calling start() and end()
    #       2. Enable on-demand resources allocation
    #       3. Exception handling is easier
###############################################

#######################
if __name__ == '__main__':
    main()