# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains the MortgageMixin class methods
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
from loan.loans import FixedRateLoan, VariableRateLoan
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
import logging
# Derived classes from Loan:
# MortgageMixin
# Does not derive from loan, only define certain things related to the mortgage
class MortgageMixin(object):
    def __init__(self, notional, rate, term, home):
        # Check if passed-in home attribute is of the HouseBase family (base or derived)
        # Init the attribute if True, else raise value error
        if not isinstance(home, HouseBase):
            raise ValueError('home attribute needs to be a HouseBase type.')
        else:
            # invoke init function if there is a base class
            super(MortgageMixin, self).__init__(notional, rate, term, home)

    ##########################################################

    ##########################################################
    # Add instance method functionalities to MortgageMixin class

    # Instance method to calculate PMI based on LTV

    # Instance method to calculate PMI based on LTV
    # Private Mortgage Insurance:
    # PMI is an extra monthly payment that one must make to compensate for the added risk of having a Loan-to-Value
    #   (LTV) ratio of less than 80% (in other words, the loan covers >= 80% of the value of the asset).
    #   For example, for 100k home, mortgage > 100k -> have to pay PMI
    # This function returns .000075 of the loan notional value if LTV > .8
    def PMI(self, period = None):
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
        # Capture step/job done to debug
        logging.debug('Step: Calculate PMI')
        return .000075 * self._asset.value(period) if (self._notional / self._asset.value(period)) > .8 else 0

    # Instance method to calculate monthly payment.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def monthlyPayment(self, period=None):
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
        # Capture step/job done to debug
        logging.debug('Step: Calculate monthlyPayment')
        return super(MortgageMixin, self).monthlyPayment(period) + self.PMI(period)

    # Instance method to calculate principal due.
    # This add PMI on top of the monthly payment value in Loan.monthlyPayment()
    # NOTE: This overrides Loan.monthlyPayment
    def principalDue(self, period):
        logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
        # Capture step/job done to debug
        logging.debug('Step: Calculate principalDue')
        return self.monthlyPayment(period) - super(MortgageMixin, self).interestDue(period)
    ##########################################################


# Derived classes from MortgageMixin:
# FixedMortgage
# Derived from MortgageMixin and FixedRateLoan
class FixedMortgage(MortgageMixin, FixedRateLoan):
    pass
# VariableMortgage
# Derived from MortgageMixin and VariableRateLoan
class VariableMortgage(MortgageMixin, VariableRateLoan):
    pass
    ##########################################################

    ##########################################################
    # Add class method functionalities

    ##########################################################
    # Add static method functionalities

    ##########################################################
