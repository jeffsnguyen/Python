# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 5
# Description: This contains LoanPool class methods
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
from loan.loan_base import Loan


# LoanPool Class
class LoanPool(object):
    def __init__(self, loans=None):
        self._loans = loans
        self._loan = [loan for loan in self._loans]
        self._notional = [loan.notional for loan in self._loans]
        self._rate = [loan.rate for loan in self._loans]
        self._term = [loan.term for loan in self._loans]
    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute loans

    @property
    def loans(self):
        return self._loans

    # Decorator to set loans value
    @loans.setter
    def loans(self, iloans):
        self._loans = iloans  # Set instance variable loans from input

    ##########################################################
    # Add instance methods

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackNotionals(self):
        return [loan.notional for loan in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackRates(self):
        return [loan.rate for loan in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackTerms(self):
        return [loan.term for loan in self._loans]

    # Instance method
    # Get the aggregate remaining loan balance for a given period
    def totalPayments(self, t=0):
        return sum([loan.balance(t) for loan in self._loans])

    # Instance method
    # Get the total loan principal
    def totalPrincipal(self):
        return sum(self._notional)

    # Instance method
    # Get the aggregate payment due for a given period
    def paymentDue(self, t=0):
        return sum([loan.monthlyPayment(t) for loan in self._loans])

    # Instance method
    # Get the aggregate interest due for a given period
    def totalInterest(self, t=0):
        return sum([loan.interestDue(t) for loan in self._loans])

    # Instance method
    # Get the aggregate principal due for a given period
    def principalDue(self, t=0):
        return self.paymentDue(t) - self.totalInterest(t)

    # Instance method
    # Get the count of loan with positive balance for a given period
    def activeLoanCount(self, t):
        count = 0
        for loan in self._loans:
            if loan.balance(t) > 0:
                count += 1
        return count

    # Instance method
    # Calculate Weighted Average Maturity of loans in the pool
    def WAM(self):
        sum_amount = self.totalPrincipal()   # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAM_rate = 0  # Initialize WAR rate to be 0
        for loan in self._loans:
            WAM_rate += loan.notional * loan.term / sum_amount
        return WAM_rate

    # Instance method
    # Calculate Weighted Average Rate of loans in the pool
    def WAR(self):
        sum_amount = self.totalPrincipal()  # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAR_rate = 0  # Initialize WAR rate to be 0
        for loan in self._loans:
            WAR_rate += loan.notional * loan.rate / sum_amount
        return WAR_rate
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
