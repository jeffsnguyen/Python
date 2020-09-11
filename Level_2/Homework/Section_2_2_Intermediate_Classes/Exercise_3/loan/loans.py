# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 3
# Description: This contains Loan class methods: FixedRateLoan, VariableRateLoan, getRate
#   Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate base class(es)

# Importing packages
from loan.loan_base import Loan

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
    #   1. Look up the passed-in startPeriod attribute as the key in rateDict, return key value if exact match is found
    #   2. If exact match is not found, find the closest
    #       a. T
    def getRate(self, startPeriod):
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
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    ##########################################################
    # Add static method functionalities to loan class

    ##########################################################
