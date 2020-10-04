# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the derived classes from Tranche class
# Derived classes:
#   - StandardTranche
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging
from spv.tranche_base import Tranche
from utils.called_once import calledOnce
from utils.memoize import Memoize

#######################

#######################


# Standard Tranche class
# Standard tranches receive both interest and principal payments from the pool of loans.
class StandardTranche(Tranche):
    def __init__(self, notional, rate, subordinationFlag):
        # Invoke base class init
        super(StandardTranche, self).__init__(notional, rate, subordinationFlag)
        self._principalPaid = {0: 0}  # Record principal payment
        self._interestPaid = {0: 0}  # Record interest payment
        self._interestShortFall = {0: 0}  # Record interest shortfall
        self._interestDue = {0: 0}  # Record interest due for each period
        self._notionalBalance = {0: notional}  # Record notional balance owed to the tranche
        self._timePeriod = 0

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car

    ##########################################################
    # Add instance methods

    # Increase the current time period of the object
    def increaseTimePeriod(self):
        self._timePeriod += 1
        return self._timePeriod

    # Record principal payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    @calledOnce  # Decorator to make sure the method only called once
    def makePrincipalPayment(self, t, paidAmount):
        if not self.notionalBalance(t) == 0:
            self._principalPaid[t] = paidAmount
        else:
            raise ValueError('Insufficient balance to make payment')

    # Record interest payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    # If the interest amount is less than the current interest due:
    #   In this case, the missing amount needs to be recorded separately as an interest shortfall.
    @calledOnce  # Decorator to make sure the method only called once
    def makeInterestPayment(self, t, paidAmount):
        interestDue = self.interestDue(t)
        if not interestDue == 0:
            self._interestShortFall[t] = interestDue - paidAmount
            self._interestPaid[t] = paidAmount
        else:
            raise Exception('There is no interest due balance.')

    # Return the amount of notional still owed to the tranche for the current time period (after any payments made).
    # You can calculate this based on the original notional,
    # the sum of all the principal payments already made, and any interest shortfalls.
    def notionalBalance(self, t):
        if not t == 0:
            self._notionalBalance[t] = self._notional - sum([val for val in self._principalPaid.values()])
        return self._notionalBalance[t]

    # Return the amount of interest due for the current time period.
    def interestDue(self, t):
        if not t == 0:
            self._interestDue[t] = self.notionalBalance(t-1) * self.monthlyRate(self._rate) + \
                                   self._interestShortFall[t-1]
        return self._interestDue[t]

    # Reset the tranche to time t=0
    def reset(self):
        self._principalPaid = {0: 0}  # Record principal payment
        self._interestPaid = {0: 0}  # Record interest payment
        self._interestShortFall = {0: 0}  # Record interest shortfall
        self._interestDue = {0: 0}  # Record interest due for each period
        self._notionalBalance = {0: self._notional}  # Record notional balance owed to the tranche
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    # Calculate monthly rate based on annual rate
    @staticmethod
    def monthlyRate(annual_rate):
        return annual_rate / 12
    ##########################################################
