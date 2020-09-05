## Type: Homework
## Level: 1
## Section: 2.1: Classes
## Exercise: 1
## Description: This contains the class Timer

import time

# Timer class
class Timer(object):

    # Initialization function with hours, minutes and seconds arguments
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, hours = None, minutes = None, seconds = None):
        self._hours = float(hours) if hours is not None \
            else float(Timer._dhours) if hasattr(Timer, '_dhours') else 0
        self._minutes = float(minutes) if minutes is not None \
            else float(Timer._dminutes) if hasattr(Timer, '_dminutes') else 0
        self._seconds = float(seconds) if seconds is not None \
            else float(Timer._dseconds) if hasattr(Timer, '_dseconds') else 0

    # Default time function to set default time
    @classmethod
    # Set at the class level the value of hours, minutes, seconds as default if not speicified
    # Instead of storing dhours, dminutes and dseconds at the object level, store them at the class level
    def defaultTime(cls, hours, minutes, seconds):
        cls._dhours = hours  # ._dhours get values of the hours variable
        cls._dminutes = minutes
        cls._dseconds = seconds

    # Decorator to create a property function to define the argument hours
    @property
    def hours(self):
        return self._hours

    # decorator set hours
    @hours.setter
    def hours(self, ihours):
        self._hours = ihours  # Set _hours to be input hours

    # Decorator to create a property function to define the argument minutes
    @property
    def minutes(self):
        return self._minutes

    # decorator set hours
    @minutes.setter
    def minutes(self, iminutes):
        self._minutes = iminutes  # Set _minutes to be input minutes

    # Decorator to create a property function to define the argument seconds
    @property
    def seconds(self):
        return self._seconds

    # decorator set hours
    @seconds.setter
    def seconds(self, iseconds):
        self._seconds = iseconds  # Set _seconds to be input seconds



    # Class method to start time counter
    @classmethod
    def start(cls):
        counter_start = time.time()
        return counter_start

    # Class method to start time counter
    @classmethod
    def end(cls):
        counter_end = time.time()
        return counter_end

    # Class method to retrieve last timer result
    @classmethod
    def retrieveLastResult(cls):

