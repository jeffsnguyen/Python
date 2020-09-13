# Type: Homework
# Level: 2
# Section: 2.2: Intermediate
# Exercise: 6
# Description: This contains the Asset class and its methods
#   This exercise focuses on creating the individual Asset derived classes. Do the following:
#       a. Modify the annualDeprRate method of the Asset class to trigger a not-implemented error.
#           This ensures that no one can directly instantiate an Asset object (makes it abstract).
#       b. Create a Car class, derived from Asset. Derive multiple car types from Car (i.e. Civic, Lexus,
#           Lamborghini, etc.). Give each one a different depreciation rate.
#       c. Create a HouseBase class, derived from Asset. Derive PrimaryHome and VacationHome
#           from House. Give each one a different depreciation rate (note, a vacation home will
#           depreciate slower than a primary home since it is often vacant).

# Importing packages


# Asset class
# This class object takes on the value of the asset
class Asset(object):

    # Initialization function with value
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, initialValue):
        # Main attributes
        self._initialValue = initialValue

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the argument value
    @property
    def value(self):
        return self._initialValue

    # Decorator to set value
    @value.setter
    def value(self, ivalue):
        self._initialValue = ivalue  # Set instance variable notional from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to asset class

    # Return a yearly depreciation rate
    # Raise NotImplementedError to make Asset object abstract and prevent direct instantiation
    def annualDeprRate(self, period = None):
        raise NotImplementedError

    # Calculate and return a monthly depreciation rate based on the annual depreciation rate
    # Formula monthly = annual / 12
    def monthlyDeprRate(self, period = None):
        return self.annualDepr() / 12

    # Calculate and return current value of asset at a given time t
    # Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    def value(self, t):
        return self._initialValue * ((1 - self.monthlyDepr())**t)

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