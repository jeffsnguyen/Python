# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 2
# Description: This contains the Loan class and its functionalities as outlined in Exercise 2
#   Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property
#   methods). Then, extend it with methods that return the following (refer to the slides for any
#   necessary formulas):
#       a. The monthly payment amount of the Loan (monthlyPayment). Even though
#           monthlyPayment is likely to be equal for all months, you should still define this with a
#           dummy ‘period’ parameter, since it’s possible some loan types will have a monthly payment
#           dependent on the period.
#       b. The total payments over the entire Loan (totalPayments). This is principal plus interest.
#       c. The total interest over the entire Loan (totalInterest).

# Importing packages


# Loan class
# This class object takes on the arguments asset, face, rate, term
class Loan(object):

    # Initialization function with asset, face, rate, term
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, notional, rate, term):
        self._notional = notional
        self._rate = rate
        self._term = term

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the argument notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set minutes
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the argument rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set seconds
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the argument term
    @property
    def term(self):
        return self._term

    # Decorator to set seconds
    @term.setter
    def term(self, iterm):
        self._term = iterm  # Set instance variable rate from input

        # Class method to configure format of timer

    ##########################################################

    ##########################################################
    # Add instance method functionalities to Loan class
    # Instance method to calculate monthly payments
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, period = None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        self.monthly_payment = (self._rate * self._notional * (1 + self._rate)**self._term) / \
                                ((1 + self._rate) ** self._term - 1)
        return self.monthly_payment

    # Instance method to calculate total payments
    def totalPayments(self):
        # Calculate payment using the formula total = P(1 + r)**N
        # r = monthly rate, P = notional value, N = term in months
        self.total_payment = self._notional * (1 + self._rate)**self._term
        return self.total_payment

    # Instance method to calculate total interest over the entire loan
    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment = notional value
        self.total_interest = self.total_payment - self._notional
        return self.total_interest
    ##########################################################


