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
        self.reset()

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car

    ##########################################################
    # Add instance methods

    # Increase the current time period of the object
    def increaseTimePeriod(self):
        self._timePeriod += 1
        return self._timePeriod

    # Record principal due, payment and shortfall for the current tranche time period
    # Can only be called once, otherwise raised an error
    @calledOnce  # Decorator to make sure the method only called once
    def makePrincipalPayment(self, t, prinDue, prinPaid, prinShortFall):
        self._principalDue[t] = prinDue  # Record principal due for the period
        self._principalPaid[t] = prinPaid  # Record principal paid for the period
        self._principalShortFall[t] = prinShortFall  # Record principal short fall for the period

        if self.notionalBalance(t) == 0:
            raise Exception('Zero balance. All paid.')

    # Record interest payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    # If the interest amount is less than the current interest due:
    #   In this case, the missing amount needs to be recorded separately as an interest shortfall.
    @calledOnce  # Decorator to make sure the method only called once
    def makeInterestPayment(self, t, paidAmount):
        self._interestDue[t] = self.interestDue(t)  # Record interest due for the period
        self._interestPaid[t] = paidAmount  # Record interest paid for the period
        self._interestShortFall[t] = self._interestDue[t] - paidAmount  # Record interest short fall for the period

        if self._interestDue[t] == 0:
            raise Exception('Zero Balance. All Paid.')

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
        self._principalShortFall = {0: 0}  # Record principal payment
        self._principalDue = {0: 0}  # Record principal due for each period
        self._interestPaid = {0: 0}  # Record interest payment
        self._interestShortFall = {0: 0}  # Record interest shortfall
        self._interestDue = {0: 0}  # Record interest due for each period
        self._notionalBalance = {0: self._notional}  # Record notional balance owed to the tranche
        self._timePeriod = 1

    # Method to access the tranche notional
    def get_notional(self):
        return self._notional

    # Method to access the tranche rate
    def get_rate(self):
        return self._rate

    # Method to access the tranche subordinationFlag
    def get_subordinationFlag(self):
        return self._subordinationFlag

    # Method to access interestDue
    def get_interestDue(self, t):
        return self._interestDue[t]

    # Method to access interestShortFall
    def get_interestShortFall(self, t):
        return self._interestShortFall[t]

    # Method to access principalPaid
    def get_principalPaid(self, t):
        return self._principalPaid[t]

    # Method to access principalShortFall
    def get_principalShortFall(self, t):
        return self._principalShortFall[t]

    # Method to access notionalBalance
    def get_notionalBalance(self, t):
        return self._notionalBalance[t]

    ###################################

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    # Calculate monthly rate based on annual rate
    @staticmethod
    def monthlyRate(annual_rate):
        return annual_rate / 12
    ##########################################################
