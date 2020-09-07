# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 2
# Description: This contains the test function for the Exercise 2, Loan class
#   Create a basic Loan class exactly as demonstrated in the lecture (including the setter/getter property
#   methods). Then, extend it with methods that return the following (refer to the slides for any
#   necessary formulas):
#       a. The monthly payment amount of the Loan (monthlyPayment). Even though
#           monthlyPayment is likely to be equal for all months, you should still define this with a
#           dummy ‘period’ parameter, since it’s possible some loan types will have a monthly payment
#           dependent on the period.
#       b. The total payments over the entire Loan (totalPayments). This is principal plus interest.
#       c. The total interest over the entire Loan (totalInterest).

# Importing necessary packages

from Loan.loan_base import Loan


#######################


def main():
    # Testing block
    ###############################################
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside Loan() but not the loan1 variable name.
    loan1 = Loan(100000, .045, 30)
    #### Your test code goes here - END ####
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using
    #   the monthlyPayment function
    # Desired Result: Print out correct monthly payment value.
    # 2.a Demo monthlyPayment function
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())

    # Scenario: This test demonstrate how to calculate the given loan's total payment using
    #   the totalPayments function
    # Desired Result: Print out correct total payment value.
    # 2.b Demo totalPayments function
    print('The total payment (principal + interest) of this loan is: ', loan1.totalPayments())

    # Scenario: This test demonstrate how to calculate the given loan's total interests using
    #   the totalInterest function
    # Desired Result: Print out correct total interest value.
    # 2.c Demo totalInterest function
    print('The total interest payment of this loan is: ', loan1.totalInterest())
    ###############################################

    # Testing block
    ###############################################
    # Scenario: This test all the functionalities with edge case where the term is negative.
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside Loan() but not the loan1 variable name.
    loan2 = Loan(200000, -.045, 0)
    #### Your test code goes here - END ####
    print('Loan info: ' + str(loan2.notional) + ' loan, at monthly rate of ' + str(loan2.rate) + ' over '
          + str(loan2.term) + ' months.')

    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using
    #   the monthlyPayment function
    # Desired Result: Print out correct monthly payment value. Since it is not possible to calculate,
    #   print out a division by zero warning message to user and return None as value.
    # 2.a Demo monthlyPayment function
    print('The monthly payment of this loan is: ', loan2.monthlyPayment())

    # Scenario: This test demonstrate how to calculate the given loan's total payment using
    #   the totalPayments function
    # Desired Result: Print out correct total payment value.
    # 2.b Demo totalPayments function
    print('The total payment (principal + interest) of this loan is: ', loan2.totalPayments())

    # Scenario: This test demonstrate how to calculate the given loan's total interests using
    #   the totalInterest function
    # Desired Result: Print out correct total interest value.
    # 2.c Demo totalInterest function
    print('The total interest payment of this loan is: ', loan2.totalInterest())
    ###############################################


#######################
if __name__ == '__main__':
    main()
