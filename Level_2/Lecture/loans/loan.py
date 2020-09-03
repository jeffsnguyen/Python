# derived loan classes

from loans.loan_base import Loan

class FixedRateLoan(Loan):
    def rate(self, period):
        # Overrides the base class
        print 'In the FixedRateLoan rate function'
        retur self._rate

class VariableRateLoan(Loan):
    def __init__(self, face, rateDict, term):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(face, None, term)

    def rate(self, period):
        # Add code to find the rate for a given period
        # rateDict contains startPeriod as key and rate as value
        # for each rate
        print 'In the VariableRateLoan rate function'





def main():
    pass

#######################
if __name__ == '__main__':
    main()