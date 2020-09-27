# Type: Homework
# Level: 5
# Section: 5.2: Decorators
# Exercise: 2
# Description: This contains tests for Memoization
#   Create a decorator that memoize’s the result of a function. This decorator should be flexible
#       enough that it can work with a function with any number of parameters. Note that memoizing
#       should happen on a per-parameter basis; meaning, cache the result for every unique set of
#       parameter values. Hint: Use a dict.
#
#   Be sure to test this decorator on different functions to ensure it works properly. You should also
#       use in conjunction with the timer decorator, to demonstrate that subsequent calls to the
#       memoized function are quicker than the initial call for a given parameter set.

# Importing necessary packages
import logging
from time import sleep
from utils.timer import Timer
import functools
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################


# Memoize class
class Memoize:
    def __init__(self, func):
        self._func = func
        self._memoized_dict = {}  # Initialize an empty dict to cache
        self.__wrapped__ = self.__call__

    def __call__(self, *args, **kwargs):
        # check if args or kwargs are in the dict
        # if not, add to the dict and return the key value
        if (str(args) + str(kwargs)) not in self._memoized_dict:
            logging.debug(f'{args} or {kwargs} is is not in the dict.')
            self._memoized_dict[(str(args) + str(kwargs))] = self._func(*args, **kwargs)
            logging.debug(f'Saved {self._memoized_dict[(str(args) + str(kwargs))]} to cache.')
            logging.debug(f'My cache is now {self._memoized_dict}')
        return self._memoized_dict[(str(args) + str(kwargs))]

#######################


# Timing the Memoize of 1+1
@Timer  # decorating the function with the Timer function
@Memoize  # Memoize decorator to cache
def intenseFunction(param1, param2):
    sleep(5)  # cause program to wait and do nothing for 5 seconds
    return f'{param1} + {param2} = {param1+param2}'


# Timing the Memoize of a Fib sequence generator
@Timer  # decorating the function with the Timer function
@Memoize  # Memoize decorator to cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the intenseFunction with Timer and Memoize decorator
    #       2. Test the fib() with Timer and Memoize decorator
    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')
    print('1. Test the modified Timer class as a decorator')
    logging.info('1. Test the modified Timer class as a decorator')

    print(intenseFunction(1, 1))
    print()

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 2
    testNum = 'Test 2'
    logging.info(f'{testNum}')
    print('2. Test the fib() with Timer and Memoize decorator')
    logging.info('2. Test the fib() with Timer and Memoize decorator')

    print(fib(100))

    logging.info(f'#######################{testNum} Completed.')
    #######################

    ###############################################


#######################
if __name__ == '__main__':
    main()
