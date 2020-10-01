# Type: Homework
# Level: 5
# Section: 5.2: Decorators
# Exercise: 3
# Description: This contains the class Memoize
#   Modify the Timer class to work as a decorator (feel free to use the provided sample code). Its
#       usage should look like this:
#       @Timer
#       def myFunc(arg1, arg2):
#           print('Do Work Here')
#   An example output would look like: <function myFunc at 0x34173DF0>: 1.5467 seconds
#
#   How does this compare to the previous approach to using the context manager? When is this
#       more useful and when are context managers more useful?

# Importing packages
from time import time
import logging
from functools import partial

#######################
logging.basicConfig(format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style="{")
#######################


#######################
# Memoize class
class Memoize:
    def __init__(self, func):
        self._func = func
        self._memoized_dict = {}  # Initialize an empty dict to cache

    def __call__(self, *args, **kwargs):
        # check if args or kwargs are in the dict
        # if not, add to the dict and return the key value
        if (str(args) + str(kwargs)) not in self._memoized_dict:
            logging.debug(f'{args} or {kwargs} is is not in the dict.')
            self._memoized_dict[(str(args) + str(kwargs))] = self._func(*args, **kwargs)
            logging.debug(f'Saved {self._memoized_dict[(str(args) + str(kwargs))]} to cache.')
            logging.debug(f'My cache is now {self._memoized_dict}')
        return self._memoized_dict[(str(args) + str(kwargs))]

    # Get method to get the other class instance object
    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)
#######################
