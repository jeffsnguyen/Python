# derived loan classes

from loan.loan_base import Loan


class FixedRateLoan(Loan):
    def rate(self, period):
        # Overrides the base class
        print('In the FixedRateLoan rate function')
        return self._rate  # Just need to return the rate, inherit the rate defined as a parameter in the init
                           # function the base class


class VariableRateLoan(Loan):
    def __init__(self, face, rateDict, term):  # overide the init function in the base class
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(face, None, term)  # invoke initialization the base class

    def rate(self, period):
        # Add code to find the rate for a given period
        # rateDict contains startPeriod as key and rate as value
        # for each rate
        print('In the VariableRateLoan rate function')

        # Interest rate stored in a dict {0: .025, 15: .045, 20: 015}
        # 0 is the original rate and is required
