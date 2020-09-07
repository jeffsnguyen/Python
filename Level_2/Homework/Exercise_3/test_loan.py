# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 2
# Description: This contains the test function for the Exercise 2, loan class
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
from utils.timer import Timer

#######################


def main():
    # Testing block
    ###############################################
    # Scenario:
    #   This block will:
    #       1. Calculate interest due, principal due and balance of a loan using given formula.
    #       2. Check how long it takes to run each function.
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside loan() but not the loan1 variable name.
    loan1 = Loan(100000, 0.050, 30)
    t = 20
    run_time = Timer(0, 0, 0)
    #### Your test code goes here - END ####
    print('Calculation using formulas:')
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # Scenario: This test demonstrate how to calculate the given loan's monthly interest due at time t using
    #   the interestDue function (calculating using given formula and not recursive function).
    # Desired Result: Print out correct monthly interest due value.
    # 3.a Demo interestDue function
    run_time.start()
    print('The interest due of this loan is: ', loan1.interestDue(t))
    run_time.end()

    # Scenario: This test demonstrate how to calculate the given loan's monthly principal due at time t using
    #   the principalDue function (calculating using given formula and not recursive function).
    # Desired Result: Print out correct monthly principal due value.
    # 3.b Demo principalDue function
    run_time.start()
    print('The principal due of this loan is: ', loan1.principalDue(t))
    run_time.end()

    # Scenario: This test demonstrate how to calculate the given loan's remaining balance due at time t using
    #   the balance function (calculating using given formula and not recursive function).
    # Desired Result: Print out correct remaining balance at time t value.
    # 3.c Demo balance function
    run_time.start()
    print('The remaining balance of this loan is: ', str(loan1.balance(t)))
    run_time.end()
    print()
    ###############################################

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Calculate interest due, principal due and balance of a loan using recursive function.
    #       2. Check how long it takes to run each function.
    ###############################################
    # Initialize a loan
    #### Your test code goes here - START ####
    # Note: user can change the parameters' value inside loan() but not the loan1 variable name.
    loan1 = Loan(100000, 0.050, 30)
    #### Your test code goes here - END ####
    print('Calculation using recursive functions:')
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    # Scenario: This test demonstrate how to calculate the given loan's monthly interest due at time t using
    #   the interestDueRecursive function.
    # Desired Result: Print out correct monthly interest due value.
    # 3.a Demo interestDue function
    run_time.start()
    print('The interest due of this loan is: ', loan1.interestDueRecursive(t))
    run_time.end()

    # Scenario: This test demonstrate how to calculate the given loan's monthly principal due at time t using
    #   the principalDueRecursive function.
    # Desired Result: Print out correct monthly principal due value.
    # 3.b Demo principalDue function
    run_time.start()
    print('The principal due of this loan is: ', loan1.principalDueRecursive(t))
    run_time.end()

    # Scenario: This test demonstrate how to calculate the given loan's remaining balance due at time t using
    #   the balanceRecursive function.
    # Desired Result: Print out correct remaining balance at time t value.
    # 3.c Demo balanceRecursive function
    run_time.start()
    print('The remaining balance of this loan is: ', loan1.balanceRecursive(t))
    run_time.end()
    ###############################################

    # Comments on run time: Calculations using direct formula takes no time to run at all (0.0 seconds).
    # Calculations using recursive functions takes significantly more time to run. As time period increases,
    # Recursive functions takes exponentially longer to do the calculations.
    # Reason: While calculations using direct formula only attempt one calculation to achieve direct results,
    # recursive functions attempt all calculations from 0 to t before they can reach results in the loan example,
    # thus recursive functions have to make many unnecessary calculations compare to functions using direct formulas.

    ###############################################


#######################
if __name__ == '__main__':
    main()
