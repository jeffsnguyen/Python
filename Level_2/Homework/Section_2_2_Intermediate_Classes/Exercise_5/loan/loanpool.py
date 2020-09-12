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
class LoanPool(Loan):
    def __init__(self, loans=None):
        self._loans = loans
        self._loan = [loan for loan in self._loans]

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

    # __repr__ method to display input loans
    def __repr__(self):
        return str(self._loans)

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackNotionals(self):
        return [item[0] for item in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackRates(self):
        return [item[0] for item in self._loans]

    # Instance method
    # Get all the notional values from the loans list using list comprehension
    def unpackTerms(self):
        return [item[0] for item in self._loans]

    # Instance method
    # Get the total loan principals
    def balance(self, t=0):
        return sum([loan.balance(t) for loan in self._loans])

    # Instance method
    # Get the total loan balance for a given period
    def totalPrincipal(self):
        return sum(self.unpackNotionals())
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
