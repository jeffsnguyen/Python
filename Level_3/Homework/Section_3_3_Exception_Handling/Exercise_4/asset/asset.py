# Type: Homework
# Level: 2
# Section: 2.2: Intermediate
# Exercise: 7
# Description: This contains the Asset class and its methods
#   Now that we have our Loan and Asset classes, let’s incorporate the asset into the loan. As a loan is
#       ‘on an’ asset, which is similar to ‘has a’, we use composition instead of derivation. To this end:
#
#   a. Add an asset parameter to the base loan __init__ function, which saves it down into an
#       object-level attribute. The one caveat here is that we must to ensure that the asset
#       parameter indeed contains an Asset object (or any of its derived classes). If it’s not an Asset
#       type, you should print an error message to the user, and leave the function.
#   b. Modify MortgageMixin to initialize with a home parameter. In this case, we need to ensure
#       that the value of home is indeed a primary home, vacation home, or any other derived
#       HouseBase type. Modify the PMI function to calculate LTV based on the asset initial value
#       (instead of the loan’s face value).
#   c. Do the same for the AutoLoan class.
#   d. Create a method called recoveryValue in the Loan base class. This method should return the
#       current asset value for the given period, times a recovery multiplier of 0.6.
#   e. Create a method called equity in the Loan base class. This should return the available equity
#       (the asset value less the loan balance).
#   f. In main, instantiate different Loan types with different assets and test the new functionality.
#
#   Note that the ‘recovery value’ of an asset, in terms of a loan, is the amount of money the lender
#       can recover if the borrower defaults (forecloses). The lender will usually auction off the
#       property. The ‘multiplier’ is necessary, as the lender is not likely to receive full market value of
#       the property in an auction. The above is an overly simplistic model, as the recovery rates vary
#       across asset classes and markets (the subject of a different course).

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
        raise NotImplementedError

    # Calculate and return a monthly depreciation rate based on the annual depreciation rate
    # Formula monthly = annual / 12
    def monthlyDeprRate(self, period = None):
        return self.annualDeprRate(period) / 12

    # Calculate and return current value of asset at a given time t
    # Formula: current value = initial value * [(1-monthlyDeprRate)**t]
    def value(self, t):
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