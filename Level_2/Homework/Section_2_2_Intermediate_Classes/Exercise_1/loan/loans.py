# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 1
# Description: This contains Loan class methods: FixedRateLoan, VariableRateLoan, getRate
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
from loan.loan_base import Loan

# Derived classes from Loan:
# FixedRateLoan class
class FixedRateLoan(Loan):
    def rate(self, period = None):
        # Overrides the base class
        return self._rate

# VariableRateLoan class
class VariableRateLoan(Loan):

    # Initialize function
    def __init__(self, notional, rateDict, term):  # overide the init function in the base class
        # Check if rateDict is actually a dict vis isinstance()
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
