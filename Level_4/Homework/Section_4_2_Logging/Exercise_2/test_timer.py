# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 1
# Description: Contains the tests for modified Timer class
#   Modify your Timer class to use a logging statement (info level) instead of a print statement.

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
#######################
# Create a testing function to run a meaningless loop to take up some time
# so that the Timer class can be tested
def testing_loop(x):
    logging.info('Running a meaningless count from 1 to ' + str(x) + ' to test the Timer class...')

    # Run the meaningless loop to test
    count = 0
    for i in range(1, x):
        count += i

    # Signal completion of loop
    logging.info('Loop completed.')
###############################################
logging.basicConfig(format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style="{")
###############################################
def main():

    # Set logging level
    logging.getLogger().setLevel(logging.INFO)

    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #       2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #           and its ability to config time display format
    #       3. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #           and its ability to config time display format.  This time using incorrect timer config format.
    #       4. Test the modified Timer class to time a loop that will take more than 60 seconds
    ###############################################

    # Test 1
    # 1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    logging.info('1. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1')

    with Timer('babySharkTimer'):
        # Doing work below
        # try-except block to catch errors
        try:
            with open("babyShark.txt", 'w') as f:  # open file
                f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
        except IOError:  # catch input output error
            logging.info(IOError('Input output error'))
            pass
        except Exception:   # catch other unanticipated error
            logging.info(Exception('Unknown error.'))
            pass
        # context manager automatically clean up after itself, no need to close the file
        logging.info(f'Has the file been closed? {f.closed}.')
    print()

    # Test 2
    # 2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #   and its ability to config time display format
    logging.info('2. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1 '
          'and its ability to config time display format')

    with Timer('babySharkTimer') as timer:
        # Doing work below

        try:
            timer.timerConfig('hrs')
        except Exception:
            logging.info(Exception('Timer config invalid.'))
            logging.info('Using seconds as default. Continue...')
        finally:
            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError:  # catch input output error
                logging.info(IOError('Input output error'))
                pass
            except Exception:   # catch other unanticipated error
                logging.info(Exception('Unknown error.'))
                pass
            # context manager automatically clean up after itself, no need to close the file
            logging.info(f'Has the file been closed? {f.closed}.')
    print()

    # Test 3
    # 3. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1
    #   and its ability to config time display format. This time using incorrect timer config format.
    logging.info('3. Test the modified Timer class to time babyShark file IO in Exercise 3.4.1 '
          'and its ability to config time display format.  This time using incorrect timer config format.')

    with Timer('babySharkTimer') as timer:
        # Doing work below

        try:
            timer.timerConfig('Hello')
        except ValueError as valEx:
            logging.info(valEx)
            logging.info('Using seconds as default. Continue...')
        finally:
            # try-except block to catch errors
            try:
                with open("babyShark.txt", 'w') as f:  # open file
                    f.write('Baby shark, doo, doo, doo, doo, doo, doo')  # write to file
            except IOError:  # catch input output error
                logging.info(IOError('Input output error'))
                pass
            except Exception:  # catch other unanticipated error
                logging.info(Exception('Unknown error.'))
                pass
            # context manager automatically clean up after itself, no need to close the file
            logging.info(f'Has the file been closed? {f.closed}.')

    # Test 4
    # 4. Test the modified Timer class to time a loop that will take more than 60 seconds
    logging.info('4. Test the modified Timer class to time a loop that will take more than 60 seconds.')

    with Timer('uselessLoop'):
        # Doing work below
        # try-except block to catch errors
        try:
            testing_loop(700000000)
        except Exception:  # catch other unanticipated error
            logging.info(Exception('Unknown error.'))
            pass
    print()

###############################################

#######################
if __name__ == '__main__':
    main()