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

#######################

#######################


# Standard Tranche class
# Standard tranches receive both interest and principal payments from the pool of loans.
class StandardTranche(Tranche):
    def __init__(self, notional, rate, subordinationFlag):
        # Invoke base class init
        super(StandardTranche, self).__init__(notional, rate, subordinationFlag)
        self._principalPaid = {0: 0}  # Record principal payment
        self._principalShortFall = {0: 0}  # Record principal payment
        self._principalDue = {0: 0}  # Record principal due for each period
        self._interestPaid = {0: 0}  # Record interest payment
        self._interestShortFall = {0: 0}  # Record interest shortfall
        self._interestDue = {0: 0}  # Record interest due for each period
        self._notionalBalance = {0: notional}  # Record notional balance owed to the tranche
        self._timePeriod = 1

    ##########################################################
    # Decorators to define and set values for instance variables

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

    # Decorator to set rate value
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute subordinationFlag
    @property
    def subordinationFlag(self):
        return self._subordinationFlag

    # Decorator to set subordinationFlag value
    @subordinationFlag.setter
    def subordinationFlag(self, isubordinationFlag):
        self._subordinationFlag = isubordinationFlag  # Set instance variable subordinationFlag from input

    # Decorator to create a property function to define the attribute interestDue
    @property
    def interestDue(self):
        return self._interestDue

    # Decorator to set interestDue value
    @interestDue.setter
    def interestDue(self, iinterestDue, t):
        self._interestDue[t] = iinterestDue  # Set instance variable interestDue from input

    # Decorator to create a property function to define the attribute interestPaid
    @property
    def interestPaid(self):
        return self._interestPaid

    # Decorator to set interestPaid value
    @interestPaid.setter
    def interestPaid(self, iinterestPaid, t):
        self._interestPaid[t] = iinterestPaid  # Set instance variable interestPaid from input

    # Decorator to create a property function to define the attribute interestShortFall
    @property
    def interestShortFall(self):
        return self._interestShortFall

    # Decorator to set interestShortFall value
    @interestShortFall.setter
    def interestShortFall(self, iinterestShortFall, t):
        self._interestShortFall[t] = iinterestShortFall  # Set instance variable interestShortFall from input

    # Decorator to create a property function to define the attribute principalDue
    @property
    def principalDue(self):
        return self._principalDue

    # Decorator to set principalDue value
    @principalDue.setter
    def principalDue(self, iprincipalDue, t):
        self._principalDue[t] = iprincipalDue  # Set instance variable principalDue from input

    # Decorator to create a property function to define the attribute principalPaid
    @property
    def principalPaid(self):
        return self._principalPaid

    # Decorator to set principalPaid value
    @principalPaid.setter
    def principalPaid(self, iprincipalPaid, t):
        self._principalPaid[t] = iprincipalPaid  # Set instance variable principalPaid from input

    # Decorator to create a property function to define the attribute principalShortFall
    @property
    def principalShortFall(self):
        return self._principalShortFall

    # Decorator to set principalShortFall value
    @principalShortFall.setter
    def principalShortFall(self, iprincipalShortFall, t):
        self._principalShortFall[t] = iprincipalShortFall  # Set instance variable principalShortFall from input

    # Decorator to create a property function to define the attribute notionalBalance
    @property
    def notionalBalance(self):
        return self._notionalBalance

    # Decorator to set notionalBalance value
    @notionalBalance.setter
    def notionalBalance(self, inotionalBalance, t):
        self._notionalBalance[t] = inotionalBalance  # Set instance variable notionalBalance from input

    # Decorator to create a property function to define the attribute timePeriod
    @property
    def timePeriod(self):
        return self._timePeriod

    # Decorator to set timePeriod value
    @timePeriod.setter
    def timePeriod(self, itimePeriod):
        self._timePeriod = itimePeriod  # Set instance variable timePeriod from input
    ##########################################################
    # Add instance methods

    # Increase the current time period of the object
    def increaseTimePeriod(self):
        self.timePeriod += 1
        return self.timePeriod

    # Record principal due, payment and shortfall for the current tranche time period
    # Can only be called once, otherwise raised an error
    @calledOnce  # Decorator to make sure the method only called once
    def makePrincipalPayment(self, t, prinDue, prinPaid, prinShortFall):
        self.principalDue[t] = prinDue  # Record principal due for the period
        self.principalPaid[t] = prinPaid  # Record principal paid for the period
        self.principalShortFall[t] = prinShortFall  # Record principal short fall for the period

        if self.calc_notionalBalance(t) == 0:
            raise Exception('Zero balance. All paid.')

    # Record interest payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    # If the interest amount is less than the current interest due:
    #   In this case, the missing amount needs to be recorded separately as an interest shortfall.
    @calledOnce  # Decorator to make sure the method only called once
    def makeInterestPayment(self, t, paidAmount):
        self.interestDue[t] = self.calc_interestDue(t)  # Record interest due for the period
        self.interestPaid[t] = paidAmount  # Record interest paid for the period
        self.interestShortFall[t] = self.interestDue[t] - paidAmount  # Record interest short fall for the period

        if self.interestDue[t] == 0:
            raise Exception('Zero Balance. All Paid.')

    # Return the amount of notional still owed to the tranche for the current time period (after any payments made).
    # You can calculate this based on the original notional,
    # the sum of all the principal payments already made, and any interest shortfalls.
    def calc_notionalBalance(self, t):
        if not t == 0:
            self.notionalBalance[t] = self.notional - sum([val for val in self.principalPaid.values()])
        return self.notionalBalance[t]

    # Return the amount of interest due for the current time period.
    def calc_interestDue(self, t):
        if not t == 0:
            self.interestDue[t] = self.calc_notionalBalance(t-1) * self.monthlyRate(self.rate) + \
                                   self.interestShortFall[t-1]
        return self.interestDue[t]

    # Reset the tranche to time t=0
    def reset(self):
        self.principalPaid = {0: 0}  # Record principal payment
        self.principalShortFall = {0: 0}  # Record principal payment
        self.principalDue = {0: 0}  # Record principal due for each period
        self.interestPaid = {0: 0}  # Record interest payment
        self.interestShortFall = {0: 0}  # Record interest shortfall
        self.interestDue = {0: 0}  # Record interest due for each period
        self.notionalBalance = {0: self.notional}  # Record notional balance owed to the tranche
        self.timePeriod = 1

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
