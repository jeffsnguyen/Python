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
    def __init__(self, tranches):
        self._tranches = sorted(tranches, key=operator.attrgetter("_subordinationFlag"))  # Sort based on subordination
        self._notional = [tranche.getNotional() for tranche in tranches]
        self._mode = None
        self._timePeriod = 1
        self._principalCollected = {0: 0}
        self._reserve = {0: 0}
        '''
        self._rate = [tranche._rate for tranche in tranches]
        self._term = [tranche._term for tranche in tranches]
        self._subordinationFlag = [tranche._subordinationFlag for tranche in tranches]
        '''
    def __repr__(self):
        return [f'{tranche.__class__.__name__}({tranche._notional}, {tranche._rate}, {tranche._subordinationFlag})'
                for tranche in self._tranches]

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the attribute car

    ##########################################################
    # Add instance methods

    # Factory method to add tranche to StructuredSecurity object
    # Assume all inputs are type 'str'
    def addTranche(self, nameClass, notionalPct, rate, subordinationLvl):
        try:  # Handle instantiation of tranche object
            trancheObject = eval(nameClass)((float(notionalPct) * sum(self.getNotional())), float(rate), int(subordinationLvl))
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
            self._tranches.append(trancheObject)  # Add new object to list of StructuredSecurities

    # Instance method to flag 'Sequential' or 'ProRata' mode on the StructuredSecurity object
    def mode(self, mode):
        modeList = ['Sequential', 'Pro Rata']
        if mode not in modeList:
            raise TypeError('Incorrect Structured Security Mode')
        else:
            self._mode = mode
            return self._mode

    # Instance method to increase the current time period for each tranche object
    def increaseTranchesTimePeriod(self):
        for tranche in self._tranches:
            tranche.increaseTimePeriod()
        self._timePeriod += 1

    # Instance factory method to make payments to tranches in the StructuredSecurity object
    def makePayments(self, cash_amount):
        # Making interest payments
        cash_amount = self.makeInterestPayments(cash_amount)

        # Making principal payments based on mode
        if self._mode == 'Sequential':
            self.makeSeqPrinPayments(cash_amount)
        else:
            self.makeProRataPrinPayments(cash_amount)

    # Instance method to make interest payments to tranches in the StructuredSecurity object
    def makeInterestPayments(self, cash_amount):
        logging.debug(f'SS shows current cash reserve at time {self._timePeriod-1} = {self._reserve[self._timePeriod -1]}')
        logging.debug(f'SS shows CF in amount at t= {self._timePeriod} of {cash_amount}')

        # Add reserve from previous period to passed-in cash amount (collections from assets)
        cash_amount += self._reserve[self._timePeriod-1]
        logging.debug(f'SS shows available Funds to be used at t={self._timePeriod} = {cash_amount}')

        self._reserve[self._timePeriod] = 0  # Set reserve account for current period to be 0
        logging.debug(f'Reset reserve account to 0.')

        # Cycle through the tranches:
        #   1. Call each tranche's interestDue() method to get interest due amount, this is the amount to be paid.
        #   2. Determine the payment amount, it is the lesser amount between the availableFunds and the interest
        #       due amount.
        #   3. Call the tranche's makeInterestPayment() method to record the payment
        #   4. Determine the remaining availableFund by subtracting the paidAmount,
        for tranche in self._tranches:
            # Ask the tranche about the interest due in the current period
            interestDue = tranche.interestDue(self._timePeriod)
            logging.debug(f'SS shows Interest due of {tranche} at t={self._timePeriod} is {interestDue}')

            # The amount to be paid is the lesser amount between interest due amount and cash available
            cash_paid = min(cash_amount, interestDue)
            logging.debug(f'SS shows Interest amount to be paid for {tranche} at t={self._timePeriod} is {cash_paid}')

            # Catch any exception when calling tranche to record interest payment
            #   (e.g. if interest balance is fully paid)
            try:
                tranche.makeInterestPayment(self._timePeriod, cash_paid)
            except Exception as Ex:
                logging.info(f'{Ex}')

            cash_amount -= cash_paid # Deduct interest payment from cash amount

        return cash_amount

    # Instance method to make payments to tranches in 'Sequential' mode StructuredSecurity object
    def makeSeqPrinPayments(self, cash_amount):
        logging.debug(f'SS recorded cash available to be paid to principal is {cash_amount}')
        # Cycle through the tranches:
        #   1. Call notionalBalance(t) method for each tranche to get their principal balance at time t. Compare this
        #       with the principal collected from the LoanPool collection (passed in).
        #       The lesser amount is the principalDue for the tranche.
        #   2. Determine the paidAmount: the lesser value between the available cash and principalDue is what to
        #       be paid out.
        #   3. Call the tranche's makePrincipalPayment() method to record the payment in the tranches' dicts
        #   4. Return the available fund post-payment
        for tranche in self._tranches:

            # Calculate principalDue = min(principal received + prior principal shortfalls, available cash, balance)
            principalDue = min(self._principalCollected[self._timePeriod] + tranche._principalShortFall[self._timePeriod -1], cash_amount, tranche.notionalBalance(self._timePeriod)) if not cash_amount == 0 else 0
            logging.debug(f'SS shows the principal due for {tranche} at t={self._timePeriod} is {principalDue}')

            # Calculate principal amount to be paid as well as short fall
            principalPaid = min(cash_amount, principalDue)
            prinShortFall = principalDue - principalPaid
            logging.debug(f'SS shows the paid amount for {tranche} at t={self._timePeriod} is {principalPaid}')

            # Handle exception when recording principal payment in tranches
            #   e.g: tranche's principal is fully paid (notional balance = 0)
            try:
                tranche.makePrincipalPayment(self._timePeriod, principalDue, principalPaid, prinShortFall)
            except Exception as Ex:
                logging.info(f'{Ex}')

            cash_amount -= principalPaid  # Deduct principal payment from cash available
            logging.debug(f'SS shows the available fund after principal payment of {tranche} is {cash_amount}')

            # If the tranche's notional balance is not fully paid:
            #   1. Record reserve amount to be remaining cash.
            #   2. Set available cash_amount to be 0 to record payment of 0 to other tranches
            if not tranche.notionalBalance(self._timePeriod) == 0:
                self._reserve[self._timePeriod] += cash_amount
                logging.debug(f'Added {cash_amount} to cash reserve totalling = {self._reserve[self._timePeriod]} for next iteration.')
                cash_amount = 0
                logging.debug(f'{tranche} still have a notional balance. Set availableFunds to be 0.')

        # Check if cash reserve has been recorded
        #   1. If it's not 0: no tranches were fully paid in the period.
        #       Reserve has already been recorded. Do nothing here
        #   2. If it's 0: there was a fully paid tranches.
        #       Reserve has not been recorded. Record leftover cash here.
        if self._reserve[self._timePeriod] == 0:
            self._reserve[self._timePeriod] = cash_amount

        return self._reserve[self._timePeriod]

    # Instance method to make payments to tranches in 'Pro Rata' mode StructuredSecurity object
    def makeProRataPrinPayments(self, cash_amount):
        logging.debug(f'SS recorded cash available to be paid to principal is {cash_amount}')

        # Cycle through the tranches:
        #   1. Call notionalBalance(t) method for each tranche to get their principal balance at time t. Compare this
        #       with the principal collected from the LoanPool collection (passed in).
        #       The lesser amount is the principalDue for the tranche.
        #   2. Determine the paidAmount: the lesser value between the available cash and principalDue is what to
        #       be paid out.
        #   3. Call the tranche's makePrincipalPayment() method to record the payment in the tranches' dicts
        #   4. Return the available fund post-payment
        for tranche in self._tranches:

            # Calculate principalDue = min(principal received + prior principal shortfalls, available cash, balance)
            principalDue = min((self._principalCollected[self._timePeriod] * tranche.getNotional() / sum(self._notional)) + tranche._principalShortFall[self._timePeriod -1], cash_amount, tranche.notionalBalance(self._timePeriod)) if not cash_amount ==0 else 0
            logging.debug(f'SS shows the principal due for {tranche} at t={self._timePeriod} is {principalDue}')

            # Calculate principal amount to be paid as well as short fall
            principalPaid = min(cash_amount, principalDue)
            prinShortFall = principalDue - principalPaid
            logging.debug(f'SS shows the paid amount for {tranche} at t={self._timePeriod} is {principalPaid}')

            # Handle exception when recording principal payment in tranches
            #   e.g: tranche's principal is fully paid (notional balance = 0)
            try:
                tranche.makePrincipalPayment(self._timePeriod, principalDue, principalPaid, prinShortFall)
            except Exception as Ex:
                logging.info(f'{Ex}')

            cash_amount -= principalPaid  # Deduct principal payment from cash available
            logging.debug(f'SS shows the available fund after principal payment of {tranche} is {cash_amount}')

        self._reserve[self._timePeriod] +=  cash_amount

        return self._reserve[self._timePeriod]

    # Pass on the principalDue amount from LoanPool collection
    def get_principalCollected(self, t, prinCollections):
        self._principalCollected[t] = prinCollections
        return self._principalCollected[t]

    ##########################################################
    # Add class methods

    ##########################################################
    # Add static methods

    ##########################################################
