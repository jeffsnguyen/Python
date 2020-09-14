# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 1
# Description: This contains Loan class methods: FixedRateLoan, VariableRateLoan, getRate
#   As shown in the lecture, create derived classes as follows:
#       a. A FixedRateLoan class which derives from Loan.
#       b. A VariableRateLoan class which derives from Loan. This will differ from a FixedRateLoan in
#           that it has a rate dict instead of a single rate value. This dict will contain startPeriod as key
#           and rate as value. This should have its own __init__ function that does the following:
#               i. Validates that the rate parameter is indeed a dict (if not, print an error).
#               ii. Invokes the super-class’ __init__ function with all the parameters.
#
#           The result of the above is that a VariableRateLoan's _rate attribute, as well as its rate
#           property getters/setters will be a dict instead of a value. However, the functions that use
#           the rate (i.e. balance) does not yet know how to handle a dict of rates. To handle this, do the
#           following:
#               i. Create a getRate function in the base Loan class. This should take a period
#                   parameter. and return the result of the rate property.
#               ii. Override the getRate function in VariableRateLoan. This version will calculate the
#                   rate from the dict based on the period argument. Tip: Keep in mind that the dict
#                   only contains startPeriod for each rate -- the code will need to infer the rate for any
#                   period in between.
#
#           Then, modify the Loan class functions (i.e. balance) to use the getRate function to get the
#           rate for the current period.
#
#           Note that the monthly payment and balance formulas are technically different in this
#           Variable case, but we will avoid changing it for simplicity (the focus of the remaining
#           exercises and case study are on fixed rate loans only).

# Importing packages


# loan class
# This class object takes on the arguments asset, face, rate, term
class Loan(object):

    # Initialization function with asset, face, rate, term
    # Also included in this function is ability to set the arguments to 0 if they don't already exists
    def __init__(self, notional, rate, term):
        # Main attributes
        self._notional = notional
        self._rate = rate
        self._term = term

    ##########################################################
    # Decorators to define and set values for instance variables
    # Decorator to create a property function to define the argument notional
    @property
    def notional(self):
        return self._notional

    # Decorator to set notional value
    @notional.setter
    def notional(self, inotional):
        self._notional = inotional  # Set instance variable notional from input

    # Decorator to create a property function to define the argument rate
    @property
    def rate(self):
        return self._rate

    # Decorator to set interest rate
    @rate.setter
    def rate(self, irate):
        self._rate = irate  # Set instance variable rate from input

    # Decorator to create a property function to define the argument term
    @property
    def term(self):
        return self._term

    # Decorator to set loan term
    @term.setter
    def term(self, iterm):
        self._term = iterm  # Set instance variable term from input
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    # Instance method to calculate monthly payments
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, period=None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            return self.calcMonthlyPmt(self._notional, self.getRate(period), self._term)
        except ZeroDivisionError:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Instance method to calculate total payments
    def totalPayments(self):
        # Calculate total payment using the formula total = monthlyPayment * term * 12
        # r = monthly rate, P = notional value, N = term in months
        try:
            return self.monthlyPayment() * self._term * 12
        except:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Instance method to calculate total interest over the entire loan
    def totalInterest(self):
        # Calculate payment using the formula total_interest = totalpayment = notional value
        try:
            return self.totalPayments() - self._notional
        except:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Instance method to calculate interest due at time t
    # This method use the given formula
    def interestDue(self, t):
        # Calculate payment using the formula interestDue = r * loan balance bal
        # r = monthly rate, P = notional value, N = term in months
        return Loan.monthlyRate(self.getRate(t)) * self.balance(t - 1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return Loan.monthlyPayment(t) - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    # Modified to delegate to calcBalance(face, rate, term, period)
    # Notional is equivalent to face
    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self.calcBalance(self._notional, self.getRate(t), self._term, t)

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional * Loan.monthlyRate(self.getRate(t))
        else:
            return self.balanceRecursive(t - 1) * Loan.monthlyRate(self.getRate(t))

    # Instance method to calculate principal due at time t
    # This method use the recursive function
    def principalDueRecursive(self, t):
        # Calculate payment using recursive functions
        return self.monthlyPayment() - self.interestDueRecursive(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the recursive function
    def balanceRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional - self.principalDueRecursive(t)
        else:
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)

    # Instance method to get interest rate from Loan object.
    def getRate(self, period=None):
        return self._rate
    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    # Class method to calculate the monthly payment of the given loan
    # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        try:
            return (Loan.monthlyRate(rate) * face * (1 + Loan.monthlyRate(rate)) ** (term * 12)) / \
                   (((1 + Loan.monthlyRate(rate)) ** (term * 12)) - 1)
        except ZeroDivisionError:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        return face * ((1 + Loan.monthlyRate(rate)) ** period) - \
               (Loan.calcMonthlyPmt(face, rate, term) * (((1 + Loan.monthlyRate(rate)) ** period - 1) /
                                                         Loan.monthlyRate(rate)))

    ##########################################################
    # Add static method functionalities to loan class

    # Static method to return monthly rate for a passed in annual rate
    # Monthly rate = Annual Rate / 12
    @staticmethod
    def monthlyRate(annual_rate):
        return annual_rate / 12

    # Static method to return annual rate for a passed in monthly rate
    # Annual rate = Monthly Rate * 12
    @staticmethod
    def annualRate(monthly_rate):
        return monthly_rate * 12
    ##########################################################
