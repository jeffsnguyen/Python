# Type: Homework
# Level: 2
# Section: 2.1: Classes
# Exercise: 5
# Description: This contains the test functions for the Exercise 5, Loan class
#   To demonstrate understanding of static-level methods, do the following:
#       a. Create a static-level method in Loan called monthlyRate. This should return the monthly
#           interest rate for a passed-in annual rate.
#       b. Create another static-level method that does the opposite (returns an annual rate for a
#           passed-in monthly rate).
#       c. Test the static-level method in main.
#       d. Modify all the Loan methods that rely on the rate to utilize the static-level rate functions.
#       e. What are the benefits of static-level methods? When are they useful?

# Importing necessary packages

from loan.loan_base import Loan

#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test monthlyRate function to see if it convert to annual rate correctly.
    #       2. Test annualRate function to see if it convert to annual rate correctly.
    #       3. Test the revised monthlyPayment function with static method monthlyRate
    #       4. Test the revised balance function with static method monthRate
    ###############################################
    # Testing monthlyRate
    # Scenario: Assign an annual rate and calculate monthly rate via:
    #   1. Basic math (division by 12)
    #   2. Using Loan.monthlyRate() function
    # Desire result: Equality comparison of both method should return True result.
    annual_rate = .007
    monthly_rate_math = annual_rate / 12
    monthly_rate_function = Loan.monthlyRate(annual_rate)
    print('Does the Loan.monthlyRate() function works? ', monthly_rate_math == monthly_rate_function)

    # Testing annualRate
    # Scenario: Assign a monthly rate and calculate annual rate via:
    #   1. Basic math (multiplication by 12)
    #   2. Using Loan.annualRate() function
    # Desire result: Equality comparison of both method should return True result.
    monthly_rate = .007
    annual_rate_math = annual_rate * 12
    annual_rate_function = Loan.annualRate(monthly_rate)
    print('Does the Loan.annualRate() function works? ', annual_rate_math == annual_rate_function)
    print()

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
    # Benefits of static methods:
    # 1. Useful to group related methods that should be executed at global level.
    # 2. Increase code readability.
    # 3. Eliminates the need to use self argument.
    # 4. Reduce resource usage by eliminating the need to instantiate method for each object
    ###############################################


#######################
if __name__ == '__main__':
    main()
