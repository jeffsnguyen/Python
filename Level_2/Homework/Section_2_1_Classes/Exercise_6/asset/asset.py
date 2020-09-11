# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 6
# Description: This contains the Asset class and its methods
#   Create a class called Asset. This class will represent the Asset covered by the loan. The class should
#       do the following:
#       a. Save an initial asset value upon object initialization (i.e. the initial value of a car).
#       b. Create a method that returns a yearly depreciation rate (i.e., 10%).
#       c. Create a method that calculates the monthly depreciation rate, from the yearly depreciation rate.
#       d. Create a method that returns the current value of the asset, for a given period. This is the
#           initial value times total depreciation. Total depreciation at time t can be calculated as:
#               (1-monthlyDeprRate)**t

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

    # Return the repr value of the Asset object
    def __repr__(self):
        return str(self._initialValue)

    # Return a yearly depreciation rate
    # For the purpose of this exercise, simply return 10% or 0.10
    def annualDepr(self):
        return .10

    # Calculate and return a monthly depreciation rate based on the annual depreciation rate
    # Formula monthly = annual / 12
    def monthlyDepr(self):
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
