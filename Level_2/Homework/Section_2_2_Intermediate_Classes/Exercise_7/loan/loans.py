# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 7
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
from loan.loan_base import Loan
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome

# Derived classes from Loan:
# FixedRateLoan
class FixedRateLoan(Loan):
    def rate(self, period = None):
        # Overrides the base class
        return self._rate

class VariableRateLoan(Loan):
    def __init__(self, notional, rateDict, term):  # overide the init function in the base class
        self._rateDict = rateDict if isinstance(rateDict, dict) else print('Rate is not a dictionary')
        super(VariableRateLoan, self).__init__(notional, None, term)  # invoke initialization the base class

    # Derived instance method to find the rate of a given period
    # rateDict contains startPeriod as key and rate as value for each rate
    # Methodology:
    #   1. Create a new temporary dict that sort the key (period) by values
    #   2. Of this new temp dict:
    #       a. Find the key that is closest to the passed-in period
    #       b. Compare this key with the passed-in period, if the passed-in value is smaller,
    #           remove the key from the temp dict
    #       c. Find the new closest key based on the new dict.
    #       d. Continue loop until said key is found.
    #   3. Return the corresponded key value (interest rate) of the newly founded closest key. This is the interest
    #       rate we are looking for.
    def getRate(self, startPeriod = None):
        self.sorted_key = dict(sorted(self._rateDict.items(), key = lambda k:k[1], reverse = False))
        self.closest_key = min(self.sorted_key.keys(), key = lambda k: abs(k - startPeriod))
        while self.closest_key > startPeriod:
            self.sorted_key.pop(self.closest_key, None)
            self.closest_key = min(self.sorted_key.keys(), key=lambda k: abs(k - startPeriod))
        return self._rateDict[self.closest_key]

    # Return the repr value of the whole rateDict
    def __repr__(self):
        return str(self._rateDict)
    # Interest rate stored in a dict {0: .025, 15: .045, 20: 015}
    # 0 is the original rate and is required

# AutoLoan: derived from FixedRateLoan
class AutoLoan(FixedRateLoan):
    def __init__(self, notional, rate, term, car):  # override the init function in the base class
        # Check if passed-in car attribute is of the Car family (base or derived)
        # Init the attribute if True, else raise value error
        if not isinstance(car, Car):
            raise ValueError('car attribute needs to be a Car type.')
        else:
            # invoke init function if there is a base class
            super(AutoLoan, self).__init__(notional, rate, term, car)

            ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car
    @property
    def car(self):
        return car._home

    # Decorator to set car value
    @car.setter
    def car(self, icar):
        self._car = icar  # Set instance variable car from input

    ##########################################################
    # Add instance methods
    # Return the repr value of the object
    def __repr__(self):
        return '$' + str(self._notional) + ' at ' + str(self._rate) + ' per year, for ' + str(self._term) + \
               ' years and car value is $' + str(self._car)
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
