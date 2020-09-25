# Type: Homework
# Level: 5
# Section: 5.1: Date/Time
# Exercise: 6
# Description: This contains Loan class methods, modified to handle exception
#   Modify your Loan classes to take a loan start date and loan end (maturity) date instead of a term
#       parameter. Create a term method that calculates and returns the loan term (in months) from the
#       two dates. Assume that a month is 30 days and that you round the fractional month to the nearest integer.

# Importing packages
from asset.asset import Asset
import logging
#######################
#######################

# loan class
# This class object takes on the arguments asset, face, rate, term
class Loan(object):

    # Initialization function with asset, face, rate, maturity start and end date
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, notional, rate, maturity_start, maturity_end, asset):

        # Main attributes
        self._notional = notional
        self._rate = rate
        self._maturity_start = maturity_start
        self._maturity_end = maturity_end

        if not isinstance(asset, Asset):
            logging.error('Something wrong with parameters type.')   # Log the error prior to raising it
            raise ValueError('asset must be of Asset type.')
        else:
            self._asset = asset

    # Wrapper to display
    def __repr__(self):
        return f'Loan({self._notional}, {self._rate}, {self._maturity_start}, {self._maturity_end}, {self._asset})'

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

    # Decorator to set interest rate
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute asset
    @property
    def asset(self):
        return self._asset

    # Decorator to set loan asset value
    @asset.setter
    def asset(self, iasset):
        self._asset = iasset  # Set instance variable asset from input

    # Decorator to create a property function to define the attribute maturity_start
    @property
    def maturity_start(self):
        return self._maturity_start

    # Decorator to set loan maturity start datetime value
    @maturity_start.setter
    def maturity_start(self, imaturity_start):
        self._maturity_start = imaturity_start  # Set instance variable maturity_start from input

    # Decorator to create a property function to define the attribute maturity_end
    @property
    def maturity_end(self):
        return self._maturity_end

    # Decorator to set loan maturity end datetime value
    @maturity_end.setter
    def maturity_end(self, imaturity_end):
        self._maturity_end = imaturity_end  # Set instance variable maturity_end from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    # Instance method to return timedelta of start date and end datetime parameters
    def term(self):
        time_delta = abs(self._maturity_start - self._maturity_end)
        logging.debug(f'Calculated time_delta = {time_delta}')

        # Lookup dict in terms of microseconds
        dT_dictMS = {'months': 2592000000000,
                     'days': 86400000000,
                     'hours': 3600000000,
                     'minutes': 60000000,
                     'seconds': 1000000,
                     'microseconds': 1}

        # Calculate total microseconds as the base
        total_microseconds = time_delta.days * dT_dictMS['days'] + time_delta.seconds * dT_dictMS['seconds'] + time_delta.microseconds
        logging.debug(f'Total base microseconds = {total_microseconds}')

        return round(total_microseconds / dT_dictMS['months'])

    # Instance method to calculate monthly payments
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, period=None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate monthlyPayment')
            return self.calcMonthlyPmt(self._notional, self.getRate(period), self.term())
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate total payments
    def totalPayments(self):
        # Calculate total payment using the formula total = monthlyPayment * term * 12
        # r = monthly rate, P = notional value, N = term in months
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate totalPayments using monthlyPayments and term')
            return self.monthlyPayment() * self.term()
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate total interest over the entire loan
    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment = notional value
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate totalInterest using totalPayments and notional')
            return self.totalPayments() - self._notional
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate interest due at time t
    # This method use the given formula
    def interestDue(self, t):
        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate totalInterest using totalPayments and notional')
        return self.monthlyRate(self.getRate(t)) * self.balance(t - 1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate principalDue using monthlyPayments and interestDue')
        return self.monthlyPayment(t) - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    # Modified to delegate to calcBalance(face, rate, term, period)
    # Notional is equivalent to face
    def balance(self, t):
        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate balance using calcBalance')
        return self.calcBalance(self._notional, self.getRate(t), self.term(), t)

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, return notional * monthlyRate if term = 1')
            return self._notional * self.monthlyRate(self.getRate(t))
        else:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, '
                          'return balanceRecursive(t-1) * monthlyRate if term != 1')
            return self.balanceRecursive(t - 1) * self.monthlyRate(self.getRate())

    # Instance method to calculate principal due at time t
    # This method use the recursive function
    def principalDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate principalDueRecursive, return monthlyPayment - interestDueRecursive')
        return self.monthlyPayment() - self.interestDueRecursive(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the recursive function
    def balanceRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        if t > self.term()/12:
            logging.info('t value is greater than term')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate balanceRecursive, '
                          'return notional - princiaplDueRecursive if term = 1')
            return self._notional - self.principalDueRecursive(t)
        else:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate interestDueRecursive, '
                          'return balanceRecursive(t-1) - principalDueRecursive if term != 1')
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)

    # Instance method to get interest rate from Loan object.
    def getRate(self, period=None):
        # Capture step/job done to debug
        logging.debug('Step: Trying to get rate by simply returning rate parameters.')
        return self._rate

    # Instance method to return the current asset value for the given period times a recovery multiplier of .6
    def recoveryValue(self, t):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate recoveryValue by asset.value(t) * .6.')

        if t > self.term()/12:
            logging.info('t value is greater than term')

        return self._asset.value(t) * .6

    # Instance method to return the available equity (current asset value less current loan balance)
    def equity(self, t):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate equity by asset.value(t) - balance(t).')

        if t > self.term()/12:
            logging.info('t value is greater than term')

        return self._asset.value(t) - self.balance(t)
    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    # Class method to calculate the monthly payment of the given loan
    # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        try:
            # Capture step/job done to debug
            logging.debug('Step: Trying to calculate calcMonthlyPmt')
            return (cls.monthlyRate(rate) * face * (1 + cls.monthlyRate(rate)) **
                    term) / (((1 + cls.monthlyRate(rate)) ** term) - 1)
        except ZeroDivisionError:
            logging.error('Something went wrong. Division by 0.')  # Log the error prior to raising it
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate calcBalance')
        return face * ((1 + cls.monthlyRate(rate)) ** period) - \
               (cls.calcMonthlyPmt(face, rate, term) *
               (((1 + cls.monthlyRate(rate)) ** period - 1) / cls.monthlyRate(rate)))

    ##########################################################
    # Add static method functionalities to loan class

    # Static method to return monthly rate for a passed in annual rate
    # Monthly rate = Annual Rate / 12
    @staticmethod
    def monthlyRate(annual_rate):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate monthlyRate')
        return annual_rate / 12

    # Static method to return annual rate for a passed in monthly rate
    # Annual rate = Monthly Rate * 12
    @staticmethod
    def annualRate(monthly_rate):
        # Capture step/job done to debug
        logging.debug('Step: Trying to calculate annualRate')
        return monthly_rate * 12
    ##########################################################
