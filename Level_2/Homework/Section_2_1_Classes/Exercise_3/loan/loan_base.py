# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 3
# Description: This contains the Loan class and its methods as outlined in Exercise 3
#   Interest due at time T on a loan depends on the outstanding balance. Principal due is the monthly
#   payment less the interest due. Conceptually, these are recursive calculations as one can determine
#   the interest/principal due at time T if one knows the balance at time T-1 (which, in turn, can be
#   determined if one knows the balance at time T-2).
#
#   For each of the below functions, implement two versions: A recursive version (per the above
#   statement) and a version that uses the formulas provided in the slides:
#       a. The interest amount due at a given period (interestDue).
#       b. The principal amount due at a given period (principalDue).
#       c. The balance of the loan at a given period (balance).
# Use your Timer class to time each version of each function; what do you observe? What happens as
# the time period increases?

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
        self._term = iterm  # Set instance variable rate from input

    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class
    # Instance method to calculate monthly payments
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self, period=None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            return ((self._rate/12) * self._notional * (1 + (self._rate/12))**(self._term*12)) \
                   / (((1 + (self._rate/12))**(self._term*12)) - 1)
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
        return (self._rate/12) * self.balance(t-1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return self.monthlyPayment() - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self._notional * ((1+self._rate/12)**t) - \
               (self.monthlyPayment() * (((1 + (self._rate/12))**t - 1)/(self._rate/12)))

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional * (self._rate / 12)
        else:
            return self.balanceRecursive(t - 1) * (self._rate / 12)

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
            return self.balanceRecursive(t-1) - self.principalDueRecursive(t)
    ##########################################################
