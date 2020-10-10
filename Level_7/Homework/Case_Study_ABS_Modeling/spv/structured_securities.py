# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the base StructuredSecurities class
#   Create an abstract base class called Tranche. It should be initialized with notional and rate. Additionally,
#       it should have a subordination flag. This flag can either be letters of the alphabet or numbers.

# Importing packages
import logging
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
import operator
#######################

#######################


# StructuredSecurities Base class
# Consists of Tranche objects (composition)
class StructuredSecurities(object):
    def __init__(self, notional):
        self._tranches = []
        self._notional = notional
        self._mode = None
        self._timePeriod = 0
        self._principalCollected = {0: 0}
        self._totalCollected = {0: 0}
        self._reserve = {0: 0}

    def __repr__(self):
        return [f'{tranche.__class__.__name__}'
                f'({tranche.notional}, {tranche.rate}, {tranche.subordinationFlag})'
                for tranche in self.tranches]

    ##########################################################
    # Decorators to define and set values for instance variables

    # Decorator to create a property function to define the attribute tranches
    @property
    def tranches(self):
        return self._tranches

    # Decorator to set tranches value
    @tranches.setter
    def tranches(self, itranches):
        self._tranches = itranches  # Set instance variable tranches from input

    # Decorator to create a property function to define the attribute notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set notional value
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the attribute mode
    @property
    def mode(self):
        return self._mode

    # Decorator to set mode value
    @mode.setter
    def mode(self, imode):
        self._mode = imode  # Set instance variable mode from input

    # Decorator to create a property function to define the attribute timePeriod
    @property
    def timePeriod(self):
        return self._timePeriod

    # Decorator to set timePeriod value
    @timePeriod.setter
    def timePeriod(self, itimePeriod):
        self._timePeriod = itimePeriod  # Set instance variable timePeriod from input

    # Decorator to create a property function to define the attribute totalCollected
    @property
    def totalCollected(self):
        return self._totalCollected

    # Decorator to set totalCollected value
    @totalCollected.setter
    def totalCollected(self, itotalCollected, t):
        self._totalCollected[t] = itotalCollected  # Set instance variable totalCollected from input

    # Decorator to create a property function to define the attribute principalCollected
    @property
    def principalCollected(self):
        return self._principalCollected

    # Decorator to set principalCollected value
    @principalCollected.setter
    def principalCollected(self, iprincipalCollected, t):
        self._principalCollected[t] = iprincipalCollected  # Set instance variable principalCollected from input

    # Decorator to create a property function to define the attribute reserve
    @property
    def reserve(self):
        return self._reserve

    # Decorator to set reserve value
    @reserve.setter
    def reserve(self, ireserve, t):
        self._reserve[t] = ireserve  # Set instance variable principalCollected from input
    ##########################################################
    # Add instance methods

    # Factory method to add tranche to StructuredSecurity object
    # Assume all inputs are type 'str'
    def addTranche(self, nameClass, notionalPct, rate, subordinationLvl):
        try:  # Handle instantiation of tranche object
            trancheObject = \
                eval(nameClass)((float(notionalPct) * self.notional), float(rate), int(subordinationLvl))
        except NameError as nameEx:
            logging.error(f'Failed to add. {nameEx}')
            print(f'Failed to add. {nameEx}')
        except ValueError as valEx:
            logging.error(f'Failed to add. {valEx}')
            print(f'Failed to add. {valEx}')
        except Exception as Ex:
            logging.error(f'Failed to add. {Ex}')
            print(f'Failed to add. {Ex}')
        else:
            self.tranches.append(trancheObject)  # Add new tranche object to the StructuredSecurities object
            self.tranches = sorted(self.tranches, key=operator.attrgetter("subordinationFlag"))  # Sort

    # Instance method to flag 'Sequential' or 'Pro Rata' mode on the StructuredSecurity object
    def setMode(self, mode):
        modeList = ['Sequential', 'Pro Rata']
        if mode not in modeList:
            raise TypeError('Incorrect Structured Security Mode')
        else:
            self.mode = mode
            return self.mode

    # Instance method to increase the current time period for each tranche object
    def increaseTranchesTimePeriod(self):
        for tranche in self.tranches:
            tranche.increaseTimePeriod()
        self.timePeriod += 1

    # Instance factory method to make payments to tranches in the StructuredSecurity object
    def makePayments(self, cash_amount):
        self.totalCollected[self.timePeriod] = cash_amount  # Save the total collected cash for each period
        # Making interest payments
        cash_amount = self.makeInterestPayments(cash_amount)
        # Making principal payments based on mode
        if self.mode == 'Sequential':
            self.makeSeqPrinPayments(cash_amount)
        elif self.mode == 'Pro Rata':
            self.makeProRataPrinPayments(cash_amount)

    # Instance method to make interest payments to tranches in the StructuredSecurity object
    def makeInterestPayments(self, cash_amount):
        # Add reserve from previous period to passed-in cash amount (collections from assets)
        cash_amount += self.reserve[self.timePeriod-1]
        self.reserve[self.timePeriod] = 0  # Set reserve account for current period to be 0
        # Cycle through the tranches:
        #   1. Call each tranche's calc_interestDue() method to get interest due amount, this is the amount to be paid.
        #   2. Determine the payment amount, it is the lesser amount between the availableFunds and the interest
        #       due amount.
        #   3. Call the tranche's makeInterestPayment() method to record the payment
        #   4. Determine the remaining availableFund by subtracting the paidAmount,
        for tranche in self.tranches:
            # Ask the tranche about the interest due in the current period
            interestDue = tranche.calc_interestDue(self.timePeriod)

            # The amount to be paid is the lesser amount between interest due amount and cash available
            cash_paid = min(cash_amount, interestDue)

            # Catch any exception when calling tranche to record interest payment
            #   (e.g. if interest balance is fully paid)
            try:
                tranche.makeInterestPayment(self.timePeriod, cash_paid)
            except Exception as Ex:
                logging.warning(f'{Ex}')

            cash_amount -= cash_paid  # Deduct interest payment from cash amount

        return cash_amount

    # Instance method to make payments to tranches in 'Sequential' mode StructuredSecurity object
    def makeSeqPrinPayments(self, cash_amount):

        # Cycle through the tranches:
        #   1. Call calc_notionalBalance(t) method for each tranche to get their principal balance at time t.
        #       Compare this with the principal collected from the LoanPool collection (passed in).
        #       The lesser amount is the principalDue for the tranche.
        #   2. Determine the paidAmount: the lesser value between the available cash and principalDue is what to
        #       be paid out.
        #   3. Call the tranche's makePrincipalPayment() method to record the payment in the tranches' dicts
        #   4. Return the available fund post-payment
        for tranche in self.tranches:

            # Calculate principalDue = min(principal received + prior principal shortfalls, available cash, balance)
            principalDue = \
                min(self.principalCollected[self.timePeriod] + tranche.principalShortFall[self.timePeriod - 1],
                    cash_amount, tranche.calc_notionalBalance(self.timePeriod)) if not cash_amount == 0 else 0

            # Calculate principal amount to be paid as well as short fall
            principalPaid = min(cash_amount, principalDue)
            prinShortFall = principalDue - principalPaid

            # Handle exception when recording principal payment in tranches
            #   e.g: tranche's principal is fully paid (notional balance = 0)
            try:
                tranche.makePrincipalPayment(self.timePeriod, principalDue, principalPaid, prinShortFall)
            except Exception as Ex:
                logging.warning(f'{Ex}')

            cash_amount -= principalPaid  # Deduct principal payment from cash available

            # If the tranche's notional balance is not fully paid:
            #   1. Record reserve amount to be remaining cash.
            #   2. Set available cash_amount to be 0 to record payment of 0 to other tranches
            if not tranche.calc_notionalBalance(self.timePeriod) == 0:
                self.reserve[self.timePeriod] += cash_amount
                cash_amount = 0

        # Check if cash reserve has been recorded
        #   1. If it's not 0: no tranches were fully paid in the period.
        #       Reserve has already been recorded. Do nothing here
        #   2. If it's 0: there was a fully paid tranches.
        #       Reserve has not been recorded. Record leftover cash here.
        if self.reserve[self.timePeriod] == 0:
            self.reserve[self.timePeriod] = cash_amount

        return self.reserve[self.timePeriod]

    # Instance method to make payments to tranches in 'Pro Rata' mode StructuredSecurity object
    def makeProRataPrinPayments(self, cash_amount):
        # Cycle through the tranches:
        #   1. Call calc_notionalBalance(t) method for each tranche to get their principal balance at time t.
        #       Compare this with the principal collected from the LoanPool collection (passed in).
        #       The lesser amount is the principalDue for the tranche.
        #   2. Determine the paidAmount: the lesser value between the available cash and principalDue is what to
        #       be paid out.
        #   3. Call the tranche's makePrincipalPayment() method to record the payment in the tranches' dicts
        #   4. Return the available fund post-payment
        for tranche in self.tranches:
            # Calculate principalDue = min(principal received + prior principal shortfalls, available cash, balance)
            principalDue = \
                min((self.principalCollected[self.timePeriod] * tranche.notional / self.notional)
                    + tranche.principalShortFall[self.timePeriod - 1],
                    cash_amount, tranche.calc_notionalBalance(self.timePeriod)) if not cash_amount == 0 else 0

            # Calculate principal amount to be paid as well as short fall
            principalPaid = min(cash_amount, principalDue)
            prinShortFall = principalDue - principalPaid

            # Handle exception when recording principal payment in tranches
            #   e.g: tranche's principal is fully paid (notional balance = 0)
            try:
                tranche.makePrincipalPayment(self.timePeriod, principalDue, principalPaid, prinShortFall)
            except Exception as Ex:
                logging.warning(f'{Ex}')

            cash_amount -= principalPaid  # Deduct principal payment from cash available

        self.reserve[self.timePeriod] += cash_amount  # Increment reserve account with leftover cash

        return self.reserve[self.timePeriod]

    # Pass on the principalDue amount from LoanPool collection
    def save_principalCollected(self, t, prinCollections):
        self.principalCollected[t] = prinCollections
        return self.principalCollected[t]

    # Get the following values from each tranches for each time period t
    #   interestDue, interestPaid, interestShortFall, principalPaid, notionalBalance
    def getWaterfall(self, t):
        master = [self.totalCollected[t]]
        for tranche in self.tranches:
            slave = [tranche.interestDue[t], tranche.interestPaid[t], tranche.interestShortFall[t],
                     tranche.principalDue[t], tranche.principalPaid[t], tranche.principalShortFall[t],
                     tranche.notionalBalance[t]]
            master.append(slave)
        master.append(self.reserve[t])
        return master

    # Reset structured securities
    def reset(self):
        self._timePeriod = 0
        self._principalCollected = {0: 0}
        self._totalCollected = {0: 0}
        self._reserve = {0: 0}
    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
