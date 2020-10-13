# Type: Homework
# Level: 4
# Section: 4.2: Logging
# Exercise: 3
# Description: This contains LoanPool class methods
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
import logging
import random
import math


# LoanPool Class
class LoanPool(object):
    def __init__(self, loans):
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

    # Decorator to create a property function to define the attribute notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set notional value
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the attribute rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set interest rate
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute term
    @property
    def term(self):
        return self._term

    # Decorator to set term
    @term.setter
    def term(self, iterm):
        self._term = iterm  # Set instance variable rate from input
    ##########################################################
    # Add instance methods

    # Instance method
    # Get the aggregate remaining loan balance for a given period
    def totalPayments(self, t=0):
        # Capture step/job done to debug
        return sum([loan.balance(t) for loan in self.loans])

    # Instance method
    # Get the total loan principal
    def totalPrincipal(self):
        # Capture step/job done to debug
        return sum(self.notional)

    # Instance method
    # Get the aggregate payment due for a given period
    def paymentDue(self, t):
        # Capture step/job done to debug
        return sum([loan.monthlyPayment(t) for loan in self.loans])

    # Instance method
    # Get the aggregate interest due for a given period
    def totalInterest(self, t):
        # Capture step/job done to debug
        return sum([loan.interestDue(t) for loan in self.loans])

    # Instance method
    # Get the aggregate principal due for a given period
    def principalDue(self, t):
        # Capture step/job done to debug
        return self.paymentDue(t) - self.totalInterest(t)

    # Instance method
    # Get the count of loan with positive balance for a given period
    def activeLoanCount(self, t):
        return sum([loan.balance(t) > 0 for loan in self.loans])

    # Instance method to run a Monte Carlo on default scenario for its loan
    # The result is the total recovery value of the asset
    # t is the current time period
    # The integer range should be so that the odds of a given number occurring is the same
    #   odds as the default probability for the time period (always start the range from zero)
    def checkDefaults(self, t):
        return \
            sum([loan.checkDefault(t, math.floor(int((1 / loan.getDefaultProbability(t)) + 1) * random.random()))
                 for loan in self.loans])

    # Reset default flag on all loans
    def reset(self):
        for loan in self.loans:
            loan.reset()

    # Instance method
    # Calculate Weighted Average Maturity of loans in the pool
    def WAM(self):
        # Capture step/job done to debug

        sum_amount = self.totalPrincipal()   # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAM_rate = 0  # Initialize WAR rate to be 0

        # Capture step/job done to debug

        for loan in self._loans:
            WAM_rate += loan.notional * loan.term / sum_amount
        return WAM_rate

    # Instance method
    # Calculate Weighted Average Rate of loans in the pool
    def WAR(self):
        # Capture step/job done to debug

        sum_amount = self.totalPrincipal()  # assign temp variable to hold the total principal
        # Loop to calculate weighted rate of each mortgage and add them together
        WAR_rate = 0  # Initialize WAR rate to be 0

        for loan in self.loans:
            WAR_rate += loan.notional * loan.rate / sum_amount
        return WAR_rate

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
