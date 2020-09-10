# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 2
# Description: This contains Loan class methods: FixedRateLoan, VariableRateLoan, getRate
#   Create a MortgageMixin class which will contain mortgage-specific methods. In particular, we’d like
#       to implement the concept of Private Mortgage Insurance (PMI). For those unaware, PMI is an extra
#       monthly payment that one must make to compensate for the added risk of having a Loan-to-Value
#       (LTV) ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
#   To this end, implement a function called PMI that returns 0.0075% of the loan face value, but only if
#       the LTV is < 80%. For now, assume that the initial loan amount is for 100% of the asset value.
#   Additionally, override the base class monthlyPayment and principalDue functions to account for
#       PMI (Hint: use super to avoid duplicating the formulas, and note that the other methods
#       (interestDue, balance, etc.) should not require any changes).

# Importing packages
from loan.loan_base import Loan

# Derived classes from Loan:
# MortgageMixin
# Does not derive from loan, only define certain things related to the mortgage
class MortgageMixin(object):
    def __init__(self, notional, rate, term):
        # MortgageMixin.__init__(self)
        super(MortgageMixin, self).__init__(notional, rate, term)  # invoke init function if there is a base class

    # Mortgage-specific functionality goes here
    # Private Mortgage Insurance:
    # 100k home, mortgage > 100k -> have to pay PMI
    def PMI(self, period):
        # Mortgage-specific functions and code go here
        return 200
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    ##########################################################
    # Add static method functionalities to loan class

    ##########################################################
