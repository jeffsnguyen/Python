# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 5
# Description: This contains LoanPool class methods
#   Create a LoanPool class that can contain and operate on a pool of loans (composition). Provide the
#       following functionality:
#   a. A method to get the total loan principal.
#   b. A method to get the total loan balance for a given period.
#   c. Methods to get the aggregate principal, interest, and total payment due in a given period.
#   d. A method that returns the number of ‘active’ loans. Active loans are loans that have a
#       balance greater than zero.
#   e. Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate
#       (WAR) of the loans. You may port over the previously implemented global functions.

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