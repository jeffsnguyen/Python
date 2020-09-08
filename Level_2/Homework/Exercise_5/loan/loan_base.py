# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 5
# Description: This contains the loan class and its functionalities as outlined in Exercise 5
#   To demonstrate understanding of static-level methods, do the following:
#       a. Create a static-level method in Loan called monthlyRate. This should return the monthly
#           interest rate for a passed-in annual rate.
#       b. Create another static-level method that does the opposite (returns an annual rate for a
#           passed-in monthly rate).
#       c. Test the static-level method in main.
#       d. Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
#       e. What are the benefits of static-level methods? When are they useful?

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
    ##########################################################

    ##########################################################
    # Add instance method functionalities to loan class

    # Instance method to calculate monthly payments
    # Now modified to delegate to calcMonthlyPmt() which is a class method
    # Add dummy period argument to handle exceptions where some loan type
    # can have monthly payment dependent on the period
    def monthlyPayment(self):
        # Calculate payment using the formula pmt  = (r * P * (1 + r)**N) / ((1 + r)**N - 1)
        # r = monthly rate, P = notional value, N = term in months
        # DIV/0 exception handling: print and warning message and return value of None
        try:
            return self.calcMonthlyPmt(self)
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
        return Loan.monthlyRate(self.rate) * self.balance(t - 1)

    # Instance method to calculate principal due at time t
    # This method use the given formula
    def principalDue(self, t):
        # Calculate payment using the formula principalDue = monthlyPayment - interestDue
        # r = monthly rate, P = notional value, N = term in months
        return Loan.monthlyPayment() - self.interestDue(t)

    # Instance method to calculate remaining loan balance due at time t
    # This method use the given formula
    def balance(self, t):
        # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
        # r = monthly rate, P = notional value, N = term in months
        return self.calcBalance(self, t)

    # Instance method to calculate interest due at time t
    # This method use the recursive function
    def interestDueRecursive(self, t):
        # Calculate payment using recursive functions
        if t == 1:
            return self._notional * Loan.monthlyRate(self._rate)
        else:
            return self.balanceRecursive(t - 1) * Loan.monthlyRate(self._rate)

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
    def calcMonthlyPmt(cls, cloan):
        try:
            return (Loan.monthlyRate(cloan.rate) * cloan.notional * (1 + Loan.monthlyRate(cloan.rate)) **
                    (cloan.term * 12)) / (((1 + Loan.monthlyRate(cloan.rate)) ** (cloan.term * 12)) - 1)
        except ZeroDivisionError:
            print('Term value cannot be 0. Division by 0 exception. Not possible to calculate')
            return None

    # Class method to calculate outstanding balance of the given loan at given period
    # Calculate payment using the formula bal = P(1+r)**n - pmt*[((1+r)**n -1)/r]
    # r = monthly rate, P = notional value, N = term in months
    @classmethod
    def calcBalance(cls, cloan, t):
        return cloan.notional * ((1 + Loan.monthlyRate(cloan.rate)) ** t) - Loan.calcMonthlyPmt(cloan) * \
               (((1 + Loan.monthlyRate(cloan.rate)) ** t - 1) / Loan.monthlyRate(cloan.rate))

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
