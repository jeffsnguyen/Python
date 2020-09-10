# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 2
# Description: This contains the test functions for the Exercise 2, Loan class
#   Create a basic loan class exactly as demonstrated in the lecture (including the setter/getter property
#   methods). Then, extend it with methods that return the following (refer to the slides for any
#   necessary formulas):
#       a. The monthly payment amount of the loan (monthlyPayment). Even though
#           monthlyPayment is likely to be equal for all months, you should still define this with a
#           dummy ‘period’ parameter, since it’s possible some loan types will have a monthly payment
#           dependent on the period.
#       b. The total payments over the entire loan (totalPayments). This is principal plus interest.
#       c. The total interest over the entire loan (totalInterest).

# Importing necessary packages

from loan.loan_base import Loan


#######################


def main():
    # Testing block 1
    ###############################################
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside loan() but not the loan1 variable name.
    loan1 = Loan(100000, .050, 30)
    #### Your test code goes here - END ####
    print('Loan info: ' + str(loan1._notional) + ' loan, at an annual rate of ' + str(loan1._rate) + ' over '
          + str(loan1._term) + ' years.')

    # Test 1
    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using
    #   the monthlyPayment function
    # Desired Result: Print out correct monthly payment value.
    # 2.a Demo monthlyPayment function
    print('Test 1')
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())
    print()

    # Test 2
    # Scenario: This test demonstrate how to calculate the given loan's total payment using
    #   the totalPayments function
    # Desired Result: Print out correct total payment value.
    # 2.b Demo totalPayments function
    print('Test 2')
    print('The total payment (principal + interest) of this loan is: ', loan1.totalPayments())
    print()

    # Test 3
    # Scenario: This test demonstrate how to calculate the given loan's total interests using
    #   the totalInterest function
    # Desired Result: Print out correct total interest value.
    # 2.c Demo totalInterest function
    print('Test 3')
    print('The total interest payment of this loan is: ', loan1.totalInterest())
    print()
    ###############################################

    # Testing block 4
    ###############################################
    # Scenario: This test all the functionalities with edge case where the term is negative.
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside loan() but not the loan1 variable name.
    print('Test 4')
    loan2 = Loan(200000, -.045, 0)
    #### Your test code goes here - END ####
    print('Loan info: ' + str(loan2._notional) + ' loan, at an annual rate of ' + str(loan2._rate) + ' over '
          + str(loan2._term) + ' years.')
    print()

    # Test 5
    # Scenario: This test demonstrate how to calculate the given loan's monthly payment using
    #   the monthlyPayment function
    # Desired Result: Print out correct monthly payment value. Since it is not possible to calculate,
    #   print out a division by zero warning message to user and return None as value.
    # 2.a Demo monthlyPayment function
    print('Test 5')
    print('The monthly payment of this loan is: ', loan2.monthlyPayment())
    print()

    # Test 6
    # Scenario: This test demonstrate how to calculate the given loan's total payment using
    #   the totalPayments function
    # Desired Result: Print out correct total payment value.
    # 2.b Demo totalPayments function
    print('Test 6')
    print('The total payment (principal + interest) of this loan is: ', loan2.totalPayments())
    print()

    # Test 7
    # Scenario: This test demonstrate how to calculate the given loan's total interests using
    #   the totalInterest function
    # Desired Result: Print out correct total interest value.
    # 2.c Demo totalInterest function
    print('Test 7')
    print('The total interest payment of this loan is: ', loan2.totalInterest())
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
