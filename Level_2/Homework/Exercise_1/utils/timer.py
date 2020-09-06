## Type: Homework
## Level: 1
## Section: 2.1: Classes
## Exercise: 1
## Description: This contains the class Timer

# Importing packages
from time import time


# Timer class
# This class object takes on hours, minutes, seconds arguments
# It also has functionalities to count time elapsed and configure format of said time elapsed
class Timer(object):

    # Initialization function with hours, minutes and seconds arguments
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, hours=None, minutes=None, seconds=None, is_live=None):
        self._hours = float(hours) if hours is not None \
            else float(Timer._dhours) if hasattr(Timer, '_dhours') else 0
        self._minutes = float(minutes) if minutes is not None \
            else float(Timer._dminutes) if hasattr(Timer, '_dminutes') else 0
        self._seconds = float(seconds) if seconds is not None \
            else float(Timer._dseconds) if hasattr(Timer, '_dseconds') else 0

    # Initialize a counter instance variable to check if timer has/ has not started
    # Initial value is False: timer not started
    timer_check = False

    # Initialize objects to format elapsed time in seconds, minutes or hours
    timer_config = 1 # Initialize timer_config variable to format the displayed elapsed time, default is 1
    timer_dict = {1: 'seconds', 60: 'minutes', 3600: 'hours'} # Initialize dictionary to lookup proper string
                                                            # to display 'seconds', 'minutes' or 'hours'

    # Default time function to set default time
    @classmethod
    # Set at the class level the value of hours, minutes, seconds as default if not speicified
    # Instead of storing dhours, dminutes and dseconds at the object level, store them at the class level
    def defaultTime(cls, hours, minutes, seconds):
        cls._dhours = hours  # Get values of each class variable from the instance object
        cls._dminutes = minutes
        cls._dseconds = seconds

    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the argument hours
    @property
    def hours(self):
        return self._hours

    # Decorator to set hours
    @hours.setter
    def hours(self, ihours):
        self._hours = ihours  # Set instance variable hours from input

    # Decorator to create a property function to define the argument minutes
    @property
    def minutes(self):
        return self._minutes

    # Decorator to set minutes
    @minutes.setter
    def minutes(self, iminutes):
        self._minutes = iminutes  # Set instance variable minutes from input

    # Decorator to create a property function to define the argument seconds
    @property
    def seconds(self):
        return self._seconds

    # Decorator to set seconds
    @seconds.setter
    def seconds(self, iseconds):
        self._seconds = iseconds  # Set instance variable seconds from input

        # Class method to configure format of timer


    # Class method functions to perform some actions
    # Class method to start time counter
    @classmethod
    def start(cls):
        if cls.timer_check == True:
            print('Error: Timer already running. Please wait...')
        else:
            print('Starting timer, wait for process to complete...')
            cls.counter_start = time()
            cls.timer_check = True

    # Class method to start time counter
    # This also check if the timer is running. If not, print an error message
    # If the timer is running, print the time taken and return this value to the function
    @classmethod
    def end(cls):
        if cls.timer_check == False:  # If timer is not running, print error message
            print('Error: Timer is not running. Use start to start timer.')
        else:  # If timer is not running:
            cls.counter_end = time()  # Take the time stamp of the timer with time()
            print('End timer.')  # Inform user that timer has ended.

            # Calculate time elapsed in given configuration
            cls.time_elapsed = (cls.counter_end - cls.counter_start) / cls.timer_config

            # Display result in correct timer configuration format
            print('Function took ' + str(cls.time_elapsed) + ' ' + cls.timer_dict[cls.timer_config] + ' to run.')

            cls.timer_check = False  # Reset the check variable

    # Class method to retrieve last timer result
    # Last timer configuration is used
    @classmethod
    def retrieveLastResult(cls):
        cls.last_result = (cls.counter_end - cls.counter_start) / cls.timer_config
        print('The last timer is: ' + str(cls.last_result) + ' ' + cls.timer_dict[cls.timer_config])
        return cls.last_result

    # Class method to accept time display configuration
    @classmethod
    def timerConfig(cls, itimer_config):
        cls.timer_config = itimer_config
        print('Time is currently configured to display in ' + str(cls.timer_dict[cls.timer_config]) + '.')
        return cls.timer_config