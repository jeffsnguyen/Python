# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the function run_once
#

# Importing packages
from time import time
import logging
from functools import wraps

#######################
#######################


#######################
# Have method executed only once based on a flag, can be reset base on the flag
# This will work as a decorator in other methods
def run_once(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            res = func(*args, **kwargs)
            wrapper.has_run = True
            return res
        wrapper.has_run = False
        return wrapper


#######################
