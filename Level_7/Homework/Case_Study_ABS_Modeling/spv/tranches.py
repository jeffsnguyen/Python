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
        '''
        self._principalPaid = {0: 0}  # Record principal payment
        self._interestPaid = {0: 0}  # Record interest payment
        self._interestShortFall = {0: 0}  # Record interest shortfall
        self._interestDue = {0: 0}  # Record interest due for each period
        self._notionalBalance = {0: notional}  # Record notional balance owed to the tranche
        self._timePeriod = 1
        '''
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
        self._principalDue[t] = prinDue  # Record principal due for the tranche
        logging.debug(f'{self} recorded principal due at t={t} = {self._principalDue[t]}')
        self._principalShortFall[t] = prinShortFall
        logging.debug(f'{self} recorded principal shortfall at t={t} = {self._principalShortFall[t]}')
        self._principalPaid[t] = prinPaid
        logging.debug(f'{self} recorded principalPaid at t={t} = {self._principalPaid[t]}')

        if self.notionalBalance(t) == 0:
            raise Exception('Zero balance. All paid.')

    # Record interest payment for the current tranche time period
    # Can only be called once, otherwise raised an error
    # If the interest amount is less than the current interest due:
    #   In this case, the missing amount needs to be recorded separately as an interest shortfall.
    @calledOnce  # Decorator to make sure the method only called once
    def makeInterestPayment(self, t, paidAmount):
        self._interestDue[t] = self.interestDue(t)
        logging.debug(f'Tranche {self} recorded interest due at t={t} = {self._interestDue[t]}')
        self._interestShortFall[t] = self._interestDue[t] - paidAmount
        logging.debug(f'Tranche {self} recorded interest short fall at t={t} = {self._interestShortFall[t]}')
        self._interestPaid[t] = paidAmount
        logging.debug(f'Tranche {self} recorded interest paid at t={t} = {self._interestPaid[t]}')

        if self._interestDue[t] == 0:
            raise Exception('Zero Balance. All Paid.')

    # Return the amount of notional still owed to the tranche for the current time period (after any payments made).
    # You can calculate this based on the original notional,
    # the sum of all the principal payments already made, and any interest shortfalls.
    def notionalBalance(self, t):
        if not t == 0:
            self._notionalBalance[t] = self._notional - sum([val for val in self._principalPaid.values()])
            logging.debug(f'{self} shows notionalBalance[{t}] = {self._notional} - {sum([val for val in self._principalPaid.values()])} = {self._notionalBalance[t]}')
        return self._notionalBalance[t]

    # Return the amount of interest due for the current time period.
    def interestDue(self, t):
        if not t == 0:
            self._interestDue[t] = self.notionalBalance(t-1) * self.monthlyRate(self._rate) + \
                                   self._interestShortFall[t-1]
            logging.debug(f'{self} shows interestDue formula = {self.notionalBalance(t-1)} * {self.monthlyRate(self._rate)} + {self._interestShortFall[t-1]} = {self._interestDue[t]}')
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

    # Method to get the tranch notional value
    def getNotional(self):
        return self._notional
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    # Calculate monthly rate based on annual rate
    @staticmethod
    def monthlyRate(annual_rate):
        return annual_rate / 12
    ##########################################################
