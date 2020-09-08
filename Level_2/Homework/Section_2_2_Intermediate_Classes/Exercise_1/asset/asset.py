# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 1
# Description: This contains the Asset class, its objects and methods
#   As shown in the lecture, create derived classes as follows:
#       a. A FixedRateLoan class which derives from Loan.
#       b. A VariableRateLoan class which derives from Loan. This will differ from a FixedRateLoan in
#           that it has a rate dict instead of a single rate value. This dict will contain startPeriod as key
#           and rate as value. This should have its own __init__ function that does the following:
#               i. Validates that the rate parameter is indeed a dict (if not, print an error).
#               ii. Invokes the super-class’ __init__ function with all the parameters.
#
#           The result of the above is that a VariableRateLoan's _rate attribute, as well as its rate
#           property getters/setters will be a dict instead of a value. However, the functions that use
#           the rate (i.e. balance) does not yet know how to handle a dict of rates. To handle this, do the
#           following:
#               i. Create a getRate function in the base Loan class. This should take a period
#                   parameter. and return the result of the rate property.
#               ii. Override the getRate function in VariableRateLoan. This version will calculate the
#                   rate from the dict based on the period argument. Tip: Keep in mind that the dict
#                   only contains startPeriod for each rate -- the code will need to infer the rate for any
#                   period in between.
#
#           Then, modify the Loan class functions (i.e. balance) to use the getRate function to get the
#           rate for the current period.
#
#           Note that the monthly payment and balance formulas are technically different in this
#           Variable case, but we will avoid changing it for simplicity (the focus of the remaining
#           exercises and case study are on fixed rate loans only).

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
    # Add class method functionalities to loan class

    ##########################################################
    # Add static method functionalities to loan class

    ##########################################################
