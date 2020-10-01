# Type: Homework
# Level: 5
# Section: 5.2: Decorators
# Exercise: 3
# Description: This contains the class Timer
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
from functools import update_wrapper, partial

#######################
logging.basicConfig(format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style="{")
#######################


#######################
# Timer class
# This class object takes on hours, minutes, seconds arguments
# It also has functionalities to count time elapsed and configure format of said time elapsed
# Now works as a decorator
class Timer(object):

    # Initialization function with hours, minutes and seconds arguments
    # Modified for Timer class to take a function as a parameter so the class can work as a decorator
    def __init__(self, func):
        #self._timerName = timerName
        update_wrapper(self, func)
        self._func = func

    # Start the context (timer)
    def __enter__(self):
        self.start = time()  # Call start() to start timer
        logging.info('Starting timer, wait for process to complete...')
        return self

    # Exit the context (timer)
    def __exit__(self, *args):  # Call end() to get timer result and end the timer
        self.end = time()
        logging.info('End timer.')
        if (self.end - self.start) > self.warnThreshold:
            print(f'{self.timerName}: {self.end - self.start} {self.timer_dict[self.timer_config]}.')
        else:
            print(f'{self.timerName}: {self.end-self.start} {self.timer_dict[self.timer_config]}.')

    # Call method to use Timer as a decorator
    def __call__(self, *args, **kwargs):
        self.start = time()  # Start the timer
        func_result = self._func(*args, **kwargs)   # Call function
        self.end = time()  # End the timer
        print(f'Function {self._func}: {self.end - self.start} seconds.')   # Return result
        return func_result

    # Get method to get the other class instance object
    def __get__(self, obj, objtype):
        return partial(self.__call__, obj)

    # Set warnThreshold variable
    warnThreshold = 60
    # Initialize a counter instance variable to check if timer has/ has not started
    # Initial value is False: timer not started
    timer_check = False

    # Initialize objects to format elapsed time in seconds, minutes or hours
    # Initialize timer_config variable to format the displayed elapsed time, default is 1
    timer_config = 1
    # Initialize dictionary to lookup proper string to display 'seconds', 'minutes' or 'hours'
    timer_dict = {1: 'seconds', 60: 'minutes', 3600: 'hours'}

    ##########################################################
    # Decorators to define and set values for instance variables

    # Decorator to create a property function to define the argument seconds
    @property
    def timerName(self):
        return self._timerName

    # Decorator to set seconds
    @timerName.setter
    def timerName(self, itimerName):
        self._timerName = itimerName  # Set instance variable seconds from input

    ##########################################################
    # Class method functions to perform some actions

    # Default time function to set default time
    @classmethod
    # Set at the class level the value of hours, minutes, seconds as default if not speicified
    # Instead of storing dhours, dminutes and dseconds at the object level, store them at the class level
    def defaultTime(cls, timerName):
        # Get values of each class variable from the instance object
        cls._timerName = timerName

    ##########################################################
    # Instance methods

    # Instance method to start time counter
    def start(self):
        if self.timer_check:
            logging.info('Error: Timer already running. Please wait...')
        else:
            logging.info('Starting timer, wait for process to complete...')
            self.counter_start = time()
            self.timer_check = True

    # Instance method to end time counter
    # This also check if the timer is running. If not, print an error message
    # If the timer is running, print the time taken and return this value to the function
    def end(self):
        if not self.timer_check:  # If timer is not running, print error message
            logging.info('Error: Timer is not running. Use start to start timer.')
        else:  # If timer is not running:
            self.counter_end = time()  # Take the time stamp of the timer with time()
            logging.info('End timer.')  # Inform user that timer has ended.

            # Calculate time elapsed in given configuration
            self.time_elapsed_default = self.counter_end - self.counter_start
            self.time_elapsed = (self.counter_end - self.counter_start) / self.timer_config

            # Display result in correct timer configuration format
            # try except to handle exception of time configuration not existing in timer_dict dictionary
            # Only valid keys: 1: seconds, 60: minutes, 3600: hours
            try:
                logging.info(f'Function took {self.time_elapsed} {self.timer_dict[self.timer_config]} to run.')
            except KeyError:
                logging.info(f'Time config is not valid. Result will be displayed in seconds (config = 1).')
                logging.info(f'Function took {self.time_elapsed_default} seconds to run.')

            self.timer_check = False  # Reset the check variable

    # Instance method to retrieve last timer result
    # Last timer configuration is used
    def retrieveLastResult(self):
        self.last_result = self.time_elapsed
        # try except to handle exception of time configuration not existing in timer_dict dictionary
        # Only valid keys: 1: seconds, 60: minutes, 3600: hours
        try:
            logging.info(f'The last timer is: {self.last_result} {self.timer_dict[self.timer_config]}.')
        except KeyError:
            logging.info(f'Time config is not valid. Result will be displayed in seconds (config = 1).')
            logging.info(f'Function took {self.time_elapsed_default} seconds to run.')
        return self.last_result

    # Instance method to accept time display configuration
    def timerConfig(self, itimer_config):
        # Set time config based on user input
        # sec = 1 = seconds
        # min = 60 = minutes
        # hrs = 3600 = hours
        if itimer_config == 'sec':
            self.timer_config = 1
        elif itimer_config == 'min':
            self.timer_config = 60
        elif itimer_config == 'hrs':
            self.timer_config = 3600
        else:  # if input lookup fail, raise value error to user
            raise ValueError('Timer config invalid.')
        logging.info(f'Time is currently configured to display in {self.timer_dict[self.timer_config]}.')

    # Instance method to convert datetime to extract total microseconds
    def dateTimeConvert(self, dT_str, dT):
        # Create a lookup dict
        dT_dictMS = {'months': 2592000000000,
                     'days': 86400000000,
                     'hours': 3600000000,
                     'minutes': 60000000,
                     'seconds': 1000000,
                     'microseconds': 1}

        # Calculate total microseconds as the base
        total_microseconds = dT.days * dT_dictMS['days'] + dT.seconds * dT_dictMS['seconds'] + dT.microseconds
        logging.debug(f'Total base microseconds = {total_microseconds}')

        return total_microseconds / dT_dictMS[dT_str]
#######################