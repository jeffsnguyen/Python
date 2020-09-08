# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 4
# Description: This contains the Loan class and its methods as outlined in Exercise 4
#   To demonstrate understanding of class-level methods, do the following:
#       a. Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should
#           calculate a monthly payment based on three parameters: face, rate, and term.
#       b. Create a class-level function, in the Loan base class, which calculates the balance
#           (calcBalance). Input parameters should be face, rate, term, period.
#       c. Test the class-level methods in main.
#       d. Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods.
#       e. Test the object-level methods to ensure they still work correctly.
#       f. What are the benefits of class-level methods? When are they useful?

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
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    def monthlyPayment(self, period = None):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            return self.calcMonthlyPmt(self._notional, self._rate, self._term)
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
        return (self._rate / 12) * self.balance(t - 1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return self.monthlyPayment() - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    # Modified to delegate to calcBalance(face, rate, term, period)
    # Notional is equivalent to face
    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self.calcBalance(self._notional, self._rate, self._term, t)

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
            return self.balanceRecursive(t - 1) - self.principalDueRecursive(t)
    ##########################################################

    ##########################################################
    # Add class method functionalities to loan class

    # Class method to calculate the monthly payment of the given loan
    # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcMonthlyPmt(cls, face, rate, term):
        try:
            return ((rate / 12) * face * (1 + (rate / 12)) ** (term * 12)) / \
                   (((1 + (rate / 12)) ** (term * 12)) - 1)
        except ZeroDivisionError:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, face, rate, term, period):
        return face * ((1 + rate / 12) ** period) - \
               (Loan.calcMonthlyPmt(face, rate, term) * (((1 + (rate / 12)) ** period - 1) / (rate / 12)))
    ##########################################################
