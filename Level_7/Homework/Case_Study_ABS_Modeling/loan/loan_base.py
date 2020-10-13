# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains Loan class methods, modified to handle exception

# Importing packages
from asset.asset import Asset
from utils.timer import Timer
from utils.memoize import Memoize
import logging
#######################
#######################


# loan class
# This class object takes on the arguments asset, face, rate, term
class Loan(object):

    # Initialization function with asset, face, rate, term and asset
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, notional, rate, term, asset):

        # Main attributes
        self._notional = notional
        self._rate = rate
        self._term = term
        self._isDefault = False

        if not isinstance(asset, Asset):
            logging.error('Something wrong with parameters type.')   # Log the error prior to raising it
            raise ValueError('asset must be of Asset type.')
        else:
            self._asset = asset

    # Wrapper to display
    def __repr__(self):
        return f'{self.__class__.__name__}({self.notional}, {self.rate}, {self.term}, {self.asset})'

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

    # Decorator to create a property function to define the attribute term
    @property
    def term(self):
        return self._term

    # Decorator to set term
    @term.setter
    def term(self, iterm):
        self._term = iterm  # Set instance variable rate from input

    # Decorator to create a property function to define the attribute asset
    @property
    def asset(self):
        return self._asset

    # Decorator to set loan asset value
    @asset.setter
    def asset(self, iasset):
        self._asset = iasset  # Set instance variable asset from input

    # Decorator to create a property function to define the attribute isDefault
    @property
    def isDefault(self):
        return self._isDefault

    # Decorator to set loan isDefault value
    @isDefault.setter
    def isDefault(self, iisDefault):
        self._isDefault = iisDefault  # Set instance variable isDefault from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    # Instance method to calculate monthly payments
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, t):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            # Capture step/job done to debug
            res = self.calcMonthlyPmt(self.notional, self.getRate(t), self.term)
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
        if (t == 0) or (t > self.term) or self.isDefault:
            return 0
        else:
            return res

    # Instance method to calculate total payments
    def totalPayments(self):
        # Calculate total payment using the formula total = monthlyPayment * term * 12
        # r = monthly rate, P = notional value, N = term in months
        try:
            # Capture step/job done to debug
            return sum(self.monthlyPayment(t) for t in range(1, self.term+1))
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate total interest over the entire loan
    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment = notional value
        try:
            # Capture step/job done to debug
            return self.totalPayments() - self.notional
        except ZeroDivisionError:
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')

    # Instance method to calculate interest due at time t
    # This method use the given formula
    def interestDue(self, t):
        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        res = self.monthlyRate(self.getRate(t)) * self.balance(t - 1)
        if t == 0:
            return 0
        elif t > self.term:
            return 0
        else:
            return res

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        return self.monthlyPayment(t) - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    # Modified to delegate to calcBalance(face, rate, term, period)
    # Notional is equivalent to face
    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        # Capture step/job done to debug
        res = self.calcBalance(self.notional, self.getRate(t), self.term, t)
        return res if res >= 0 else 0

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    @Memoize
    def interestDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            return self.notional * self.monthlyRate(self.getRate(t))
        else:
            # Capture step/job done to debug
            return self.balanceRecursive(t - 1) * self.monthlyRate(self.getRate(t))

    # Instance method to calculate principal due at time t
    # This method use the recursive function
    @Memoize
    def principalDueRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        # Calculate payment using recursive functions
        # Capture step/job done to debug
        return self.monthlyPayment(t) - self.interestDueRecursive(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the recursive function
    @Memoize
    def balanceRecursive(self, t):
        # Warn user when running a recursive function
        # Capture step/job done to debug
        logging.warning('Step: You are running a recursive function. This will take a long time.')

        # Calculate payment using recursive functions
        if t == 1:
            # Capture step/job done to debug
            return self.notional - self.principalDueRecursive(t)
        else:
            # Capture step/job done to debug
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)

    # Instance method to get interest rate from Loan object.
    def getRate(self, period=None):
        # Capture step/job done to debug
        return self.rate

    # Instance method to return the current asset value for the given period times a recovery multiplier of .6
    def recoveryValue(self, t, pct):
        return self.asset.value(t) * pct

    # Instance method to return the available equity (current asset value less current loan balance)
    def equity(self, t):
        return self.asset.value(t) - self.balance(t)

    # Instance method to determine whether or not the loan defaults.
    # Method:
    #   1. If the passed in random number is 0: set isDefault flag, set notional to be 0 and return the recovery value
    #       of the asset at this time period t
    #   2. Else return 0, for the purpose of calculating recovery value in LoanPool
    def checkDefault(self, t, randomNum):
        if randomNum == 0:
            self.isDefault = True
            return self.recoveryValue(t, .6)  # Hardcoded pct = .6 based on Level 2 Exercise
        else:
            return 0

    # Reset default flag
    def reset(self):
        self.isDefault = False
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
            res = (cls.monthlyRate(rate) * face * (1 + cls.monthlyRate(rate)) **
                   term) / (((1 + cls.monthlyRate(rate)) ** term) - 1)
        except ZeroDivisionError:
            logging.error('Something went wrong. Division by 0.')  # Log the error prior to raising it
            raise ZeroDivisionError('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
        else:
            return res

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        # Capture step/job done to debug
        res = face * ((1 + cls.monthlyRate(rate)) ** period) - \
              (cls.calcMonthlyPmt(face, rate, term) *
               (((1 + cls.monthlyRate(rate)) ** period - 1) / cls.monthlyRate(rate)))
        return res

    ##########################################################
    # Add static method functionalities to loan class

    @staticmethod
    def monthlyRate(annual_rate):
        # Capture step/job done to debug
        return annual_rate / 12

    # Static method to return annual rate for a passed in monthly rate
    # Annual rate = Monthly Rate * 12
    @staticmethod
    def annualRate(monthly_rate):
        # Capture step/job done to debug
        return monthly_rate * 12

    # Static method to get the loan's default probability
    # t is the time period
    # Method: sort the lookup dict by key value, find the closest key value to t where t > k
    @staticmethod
    def getDefaultProbability(t):
        # To update this dict, key = top range of time period (for 1-10, use 10 as key), value = default probability
        defaultLookup = {10: 0.0005,
                         59: 0.001,
                         120: 0.002,
                         180: 0.004,
                         210: 0.002,
                         360: 0.001}
        sorted_key = dict(sorted(defaultLookup.items(), key=lambda k: k[0], reverse=False))  # Sort dict
        closest_value = min(sorted_key.keys(), key=lambda k: t > k)  # Smallest key at which t > k
        return defaultLookup[closest_value]
    ##########################################################
