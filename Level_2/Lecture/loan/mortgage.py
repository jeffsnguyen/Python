# mortgages class

from loan.loans import VariableRateLoan, FixedRateloan


class MortgageMixin(object):  # does not derive from loan, only define certain things related to the mortgage
    def __init__(self, notional, rate, term):
        # MortgageMixin.__init__(self)
        super(MortgageMixin, self).__init__()  # invoke init function if there is a base class

    # Mortgage-specific functionality goes here
    # Private Mortgage Insurance:
    # 100k home, mortgage > 100k -> have to pay PMI
    def PMI(self, period):
        # Mortgage-specific functions and code go here
        return 200


class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass


class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass
