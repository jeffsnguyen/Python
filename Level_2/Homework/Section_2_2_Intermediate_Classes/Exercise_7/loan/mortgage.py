# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 3
# Description: This contains the MortgageMixin class methods
#   Now that we have our Loan and Asset classes, let’s incorporate the asset into the loan. As a loan is
#       ‘on an’ asset, which is similar to ‘has a’, we use composition instead of derivation. To this end:
#
#   a. Add an asset parameter to the base loan __init__ function, which saves it down into an
#       object-level attribute. The one caveat here is that we must to ensure that the asset
#       parameter indeed contains an Asset object (or any of its derived classes). If it’s not an Asset
#       type, you should print an error message to the user, and leave the function.
#   b. Modify MortgageMixin to initialize with a home parameter. In this case, we need to ensure
#       that the value of home is indeed a primary home, vacation home, or any other derived
#       HouseBase type. Modify the PMI function to calculate LTV based on the asset initial value
#       (instead of the loan’s face value).
#   c. Do the same for the AutoLoan class.
#   d. Create a method called recoveryValue in the Loan base class. This method should return the
#       current asset value for the given period, times a recovery multiplier of 0.6.
#   e. Create a method called equity in the Loan base class. This should return the available equity
#       (the asset value less the loan balance).
#   f. In main, instantiate different Loan types with different assets and test the new functionality.
#
#   Note that the ‘recovery value’ of an asset, in terms of a loan, is the amount of money the lender
#       can recover if the borrower defaults (forecloses). The lender will usually auction off the
#       property. The ‘multiplier’ is necessary, as the lender is not likely to receive full market value of
#       the property in an auction. The above is an overly simplistic model, as the recovery rates vary
#       across asset classes and markets (the subject of a different course).


# Importing packages
from loan.loans import FixedRateLoan, VariableRateLoan
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome

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
        return .000075 * self._asset.value(period) if (self._notional / self._asset.value(period)) > .8 else 0

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
