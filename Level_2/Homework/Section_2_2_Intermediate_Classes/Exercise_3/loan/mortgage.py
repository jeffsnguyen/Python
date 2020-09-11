# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 3
# Description: This contains the MortgageMixin class methods
#   Create a VariableMortgage and FixedMortgage class. These should each derive-from the appropriate base class(es)

# Importing packages
from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan

# Derived classes from Loan:
# MortgageMixin
# Does not derive from loan, only define certain things related to the mortgage
class MortgageMixin(object):
    def __init__(self, notional, rate, term, home):
        super().__init__(notional, rate, term)  # invoke init function if there is a base class
        self._home = home

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the argument home
    @property
    def home(self):
        return self._home

    # Decorator to set home value
    @home.setter
    def home(self, ihome):
        self._home = ihome  # Set instance variable home from input

    ##########################################################

    ##########################################################
    # Add instance method functionalities to MortgageMixin class

    # Return the repr value of the object
    def __repr__(self):
        return '$' + str(self._notional) + ' at ' + str(self._rate) + ' per year, for ' + str(self._term) + \
               ' years and home value is $' + str(self._home)

    # Instance method to calculate PMI based on LTV

    # Instance method to calculate PMI based on LTV
    # Private Mortgage Insurance:
    # PMI is an extra monthly payment that one must make to compensate for the added risk of having a Loan-to-Value
    #   (LTV) ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
    #   For example, for 100k home, mortgage > 100k -> have to pay PMI
    # This function returns .000075 of the loan notional value if LTV > .8
    def PMI(self, period = None):
        return .000075 * self._notional if (self._notional / self._home) > .8 else 0

    # Instance method to calculate monthly payment.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def monthlyPayment(self, period=None):
        return super(MortgageMixin, self).monthlyPayment(period) + self.PMI(period)

    # Instance method to calculate principal due.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def principalDue(self, period):
        return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue(period)
    ##########################################################


# Derived classes from MortgageMixin:
# FixedMortgage
# Derived from MortgageMixin and FixedRateLoan
class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass

# Derived from MortgageMixin and VariableRateLoan
class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass
    ##########################################################

    ##########################################################
    # Add class method functionalities

    ##########################################################
    # Add static method functionalities

    ##########################################################
