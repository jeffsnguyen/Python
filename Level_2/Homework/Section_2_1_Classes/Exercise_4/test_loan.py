# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 4
# Description: This contains the test function for the Exercise 4, Loan class and its methods
#   To demonstrate understanding of class-level methods, do the following:
#       a. Implement a class-level method called calcMonthlyPmt, in the Loan base class. This should
#           calculate a monthly payment based on three parameters: face, rate, and term.
#       b. Create a class-level function, in the Loan base class, which calculates the balance
#           (calcBalance). Input parameters should be face, rate, term, period.
#       c. Test the class-level methods in main.
#       d. Modify the object-level methods for monthlyPayment and balance to delegate to the class-level methods.
#       e. Test the object-level methods to ensure they still work correctly.
#       f. What are the benefits of class-level methods? When are they useful?

# Importing necessary packages

from loan.loan_base import Loan

#######################


def main():
    # Testing block
    # Scenario:
    #   This block will, using class methods:
    #       1. Calculate monthly payment (calcMonthlyPmt)
    #       2. Calculate outstanding balance at a given period (calcBalance)
    #       3. Test the revised monthlyPayment function
    #       4. Test the revised balance function
    ###############################################
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside loan() but not the loan1 variable name.
    loan1 = Loan(100000, 0.050, 30)
    face = 100000
    rate = 0.050
    term = 30
    period = 12
    #### Your test code goes here - END ####
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using class methods
    # Desired Result: Print out correct monthly payment value.
    # 4.a Demo calcMonthlyPmt function
    print('The monthly payment of this loan is: ', Loan.calcMonthlyPmt(face, rate, term))
    ###############################################

    # Scenario: This test demonstrate how to calculate the outstanding balance of the loan at a given period.
    # Desired Result: Print out correct outstanding balance due value.
    # 4.b Demo calcBalance function
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(Loan.calcBalance(face, rate, term, period)))

    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using class methods using
    # the revised monthlyPmt function that delegates to class-level methods
    # Desired Result: Print out correct monthly payment value.
    # 4.d Demo calcBalance function
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())

    # Scenario: This test demonstrate how to calculate the outstanding balance of the loan at a given period using
    # the revised balance  function that delegates to the class-level methods.
    # Desired Result: Print out correct outstanding balance due value.
    # 4.e Demo calcBalance function
    print('The outstanding balance of this loan at period ' + str(period) + ' months is: ' +
          str(loan1.balance(period)))

    ###############################################
    # Benefits of class methods:
    # 1. Useful for methods that are related to the class but not meant to perform on an instantiated object.
    # 2. Provide a secured architectural solution as every time an object of a class is instantiated,
    #   a copy of all attributes, structures and functions are retained and this copy will only work with the dataset
    #   related to the task.

    ###############################################

#######################
if __name__ == '__main__':
    main()
