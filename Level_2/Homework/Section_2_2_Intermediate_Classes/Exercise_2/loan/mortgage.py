# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 2
# Description: This contains MortgageMixin class methods.
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
    def __init__(self, notional, rate, term, home):
        super(MortgageMixin, self).__init__(notional, rate, term)  # invoke init function if there is a base class
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

    # Instance method to calculate PMI based on LTV
    # Private Mortgage Insurance:
    # PMI is an extra monthly payment that one must make to compensate for the added risk of having a Loan-to-Value
    #   (LTV) ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
    #   For example, for 100k home, mortgage > 100k -> have to pay PMI
    # This function returns .000075 of the loan notional value if LTV > .8
    def PMI(self):
        return .000075 * self._notional if (self._notional / self._home) > .8 else 0

    # Instance method to calculate monthly payment.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def monthlyPayment(self, period=None):
        return super(MortgageMixin, self).monthlyPayment(period) + self.PMI()

    # Instance method to calculate principal due.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def principalDue(self, t):
        return self.monthlyPayment() - super(MortgageMixin, self).interestDue(t)
    ##########################################################

    ##########################################################

    ##########################################################
    # Add class method functionalities

    ##########################################################
    # Add static method functionalities

    ##########################################################
