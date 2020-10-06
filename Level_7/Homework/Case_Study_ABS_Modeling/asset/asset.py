# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains the Asset class and its methods
#   Add logging statements to your Loan class. This should consist of the following:
#       a. Anytime an exception is thrown (i.e., when an incorrect Asset type is passed-into the
#           initialization function), log an error prior to raising the exception.
#       b. Debug-level logs which display interim steps of calculations and return values for the Loan functions.
#       c. Info-level logs to display things like ‘t is greater than term’ in the loan functions.
#       d. At the point the exception is caught (in your main function) use logging.exception to display
#           the exception in addition to a custom message.
#       e. Add a warn log to the recursive versions of the waterfall functions (that they are expected to
#           take a long time, so the explicit versions are recommended).

# Importing packages
import logging


# Asset class
# This class object takes on the value of the asset
class Asset(object):

    # Initialization function with value
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, initialValue):

        # Main attributes
        self._initialValue = initialValue

    # Returning string representative
    def __repr__(self):
        return f'{self.__class__.__name__}({self._initialValue})'

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute initialValue
    @property
    def initialValue(self):
        return self._initialValue

    # Decorator to set value
    @initialValue.setter
    def initialValue(self, dinitialValue):
        self._initialValue = dinitialValue  # Set instance attribute initialValue from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to asset class

    # Return a yearly depreciation rate
    # Raise NotImplementedError to make Asset object abstract and prevent direct instantiation
    def annualDeprRate(self, period = None):
        # Capture step/job done to debug
        logging.error('Something went wrong. This is not implemented.')
        raise NotImplementedError

    # Calculate and return a monthly depreciation rate based on the annual depreciation rate
    # Formula monthly = annual / 12
    def monthlyDeprRate(self, period = None):
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
        # Capture step/job done to debug
        return self.annualDeprRate(period) / 12

    # Calculate and return current value of asset at a given time t
    # Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    def value(self, t):
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
        # Capture step/job done to debug
        return self._initialValue * ((1 - self.monthlyDeprRate(t))**t)

    ##########################################################

    ##########################################################
    # Add class method functionalities

    ##########################################################
    # Add static method functionalities

    ##########################################################


# Derived classes from Asset:
##########################################################
# Car
# Derived from Asset
class Car(Asset):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .05


# Derived classes from Car
# Lambourghini
# Derived from Car
class Lambourghini(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .20


# Lexus
# Derived from CarMixin and FixedRateLoan
class Lexus(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .08


# Civic
# Derived from CarMixin and FixedRateLoan
class Civic(Car):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .01


##########################################################
# HouseBase
# Derived from Asset
class HouseBase(Asset):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .005


# Derived classes from HouseBase
# PrimaryHome
# Derived from HouseBase
class PrimaryHome(HouseBase):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .007


# VacationHome
# Derived from HouseBase
class VacationHome(HouseBase):
    # Return a yearly depreciation rate
    # Return a constant
    def annualDeprRate(self, period=None):
        return .001