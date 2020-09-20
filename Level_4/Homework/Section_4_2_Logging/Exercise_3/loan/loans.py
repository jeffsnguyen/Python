# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains various derived Loan methods
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
            raise ValueError('car must be a Car type.')
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
