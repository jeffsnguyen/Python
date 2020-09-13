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
from loan.loan_base import Loan
#######################


def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the totalPrincipal() method of LoanPool to get total loan principal.
    #       2. Test the balance(t) method of LoanPool to get aggregate loan balance for a given period.
    #       3. Test the paymentDue(t) method of LoanPool to get aggregate payment due for a given period.
    #       4. Testing totalInterest(t) method of LoanPool to get aggregate total Interest due for a given period.
    #       5. Testing Loanpool.principalDue(t) method to get aggregate principal due for a given period.
    #       6. Testing Loanpool.activeLoanCount(t) method to get the count of loan with positive balance for a given
    #           period.
    #       7.  Testing Loanpool.WAM() to calculate the Weighted Average Maturity of loans in the pool.
    #       8.  Testing Loanpool.WAR() to calculate the Weighted Average Rate of loans in the pool.
    ###############################################
    # 1.1 Testing Loanpool.totalprincipal()
    # Scenario: Calculate the total Principal of all loans
    loan1 = Loan(100000, .050, 30)
    loan2 = Loan(100000, .050, 30)
    loan3 = Loan(100000, .050, 30)
    loan4 = Loan(100000, .050, 30)
    loans = [loan1, loan2, loan3, loan4]
    loanpool1 = LoanPool(loans)
    print('Test block 1: LoanPool')
    print('Test 1.1')
    print('The total loan principal is: ', loanpool1.totalPrincipal())
    print()

    # 1.2 Testing Loanpool.balance(t)
    # Scenario: Calculate the aggregate remaining loan balances for a given period t
    print('Test 1.2')
    print('The total loan balance is: ', loanpool1.totalPayments(26))
    print()

    # 1.3 Testing Loanpool.paymentDue(t)
    # Scenario: Calculate the aggregate loan payment due for a period t
    print('Test 1.3')
    print('The aggregate loan payment due is: ', loanpool1.paymentDue(26))
    print()

    # 1.4 Testing Loanpool.totalInterest(t)
    # Scenario: Calculate the aggregate loan interest due for a period t
    print('Test 1.4')
    print('The aggregate interest due is: ', loanpool1.totalInterest(26))
    print()

    # 1.5 Testing Loanpool.principalDue(t)
    # Scenario: Calculate the aggregate loan interest due for a period t
    print('Test 1.5')
    print('The aggregate principal due is: ', loanpool1.principalDue(26))
    print()

    # 1.6 Testing Loanpool.activeLoanCount(t)
    # Scenario: Calculate the aggregate number of active loan with balance > 0 for a period t
    print('Test 1.6')
    print('The number of active loans is: ', loanpool1.activeLoanCount(26))
    print()

    # 1.7 Testing Loanpool.WAM()
    # Scenario: Calculate the Weighted Average Maturity of loans in the pool
    print('Test 1.7')
    print('The Weighted Average Maturity is: ', loanpool1.WAM())
    print()

    # 1.8 Testing Loanpool.WAR()
    # Scenario: Calculate the Weighted Average Rate of loans in the pool
    print('Test 1.8')
    print('The Weighted Average Maturity is: ', loanpool1.WAR())
    print()
    ###############################################
#######################
if __name__ == '__main__':
    main()
