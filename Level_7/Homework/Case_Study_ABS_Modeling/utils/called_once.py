# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the function run_once
# Have method executed only once based on a flag, can be reset base on the flag
#   This will work as a decorator in other methods

# Importing packages
from functools import partial

#######################
#######################


#######################
# Have method executed only once based on a flag, can be reset base on the flag
# This will work as a decorator in other methods
class calledOnce:
    def __init__(self, func):
        self._func = func
        self._called_dict = {}

    def __call__(self, *args, **kwargs):
        # check if args or kwargs are in the dict
        # if not, add to the dict run the method
        # if yes, raise exception
        if (str(args) + str(kwargs)) not in self._called_dict:
            self._called_dict[(str(args) + str(kwargs))] = True
            return self._func(*args, **kwargs)
        else:
            raise Exception(f'Payment already made for this period')

    # Get method to get the other class instance object
    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)

#######################
