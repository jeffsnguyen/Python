# Type: Homework
# Level: 5
# Section: 5.2: Decorators
# Exercise: 3
# Description: This contains tests for Memoization of Loan waterfall function
#   Use your memoization decorator from the previous exercise to memoize the recursive versions
#       of the Loan waterfall functions. Time the functions before and after; do you see a difference?

# Importing necessary packages
import logging
#from utils.timer import Timer, Memoize
from loan.loan_base import Loan
from asset.asset import Asset, Car
import datetime
from time import time
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode='w',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################


def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the intenseLoop with Timer and Memoize decorator
    dT_start = '2018-08-21 12:5:30:123456'
    dT_start = datetime.datetime.strptime(dT_start, '%Y-%m-%d %H:%M:%S:%f')
    dT_end = '2048-09-23 1:6:30:123456'
    dT_end = datetime.datetime.strptime(dT_end, '%Y-%m-%d %H:%M:%S:%f')
    loan1 = Loan(100000, 0.05, dT_start, dT_end, Asset(100000))

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')
    print('1. Test the interestDueRecursive with Memoize to see how long it takes.')
    logging.info('1. Test the interestDueRecursive with Memoize to see how long it takes.')

    time_start = time()
    print('Using cached version')
    print(f'interestDueRecursive at month 14th = {loan1.interestDueRecursive(200)}')
    time_end = time()
    print(f'Took {time_end - time_start} to run.')
    # I'm not using Timer decorator because if I do it print the Timer everytime the recursion happens.
    print()

    logging.info(f'#######################{testNum} Completed.')

    ## Cached version with Memoize is quicker, though it's supposed to be a lot quicker??
    ## Not sure why the difference is marginal.

    #######################

#######################
if __name__ == '__main__':
    main()
