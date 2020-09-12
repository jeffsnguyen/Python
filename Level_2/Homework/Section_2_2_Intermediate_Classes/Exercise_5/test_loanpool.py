# Type: Homework
# Level: 2
# Section: 2.2: Intermediate Classes
# Exercise: 5
# Description: This contains test for LoanPool class methods.
#   Create a LoanPool class that can contain and operate on a pool of loans (composition). Provide the
#       following functionality:
#   a. A method to get the total loan principal.
#   b. A method to get the total loan balance for a given period.
#   c. Methods to get the aggregate principal, interest, and total payment due in a given period.
#   d. A method that returns the number of ‘active’ loans. Active loans are loans that have a
#       balance greater than zero.
#   e. Methods to calculate the Weighted Average Maturity (WAM) and Weighted Average Rate
#       (WAR) of the loans. You may port over the previously implemented global functions.

# Importing necessary packages
from loan.loanpool import LoanPool
#######################


def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the init function of LoanPool
    #

    ###############################################
    # 1.1 Testing MortgageMixin class
    # Scenario: Assign a LoanPool class variable
    # Desire result: Print correct result as assigned
    loans = [(100000, .050, 30), (200000, .050, 30), (150000, .050, 30)]
    loanpool1 = LoanPool(loans)
    print('Test block 1: LoanPool')
    print('Test 1.1')
    print('The loans are: ', loanpool1.__repr__())
    print()

    # 1.2 Testing total loan principal
    # Scenario: Calculate the total loan principal
    # Desire result: Print sum of loan notionals
    print('Test 1.2')
    print('The total loan principal is: ', loanpool1.totalPrincipal())
    print()

    # 1.3 Testing total loan balance for a given period
    # Scenario: Calculate the total loan balance for a period t
    # Desire result: Print sum of loan balance of period t
    print(loanpool1._loan)
    print('Test 1.3')
    print('The total loan principal is: ', loanpool1.balance(12))
    print()

    ###############################################
#######################
if __name__ == '__main__':
    main()
