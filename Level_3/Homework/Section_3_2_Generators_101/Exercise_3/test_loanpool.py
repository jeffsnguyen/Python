# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 3
# Description: Contains the tests to modified LoanPool class
#   Modify your LoanPool class to be an iterable. To do this, you will need to define an __iter__ method
#       within the class; this method should be a generator, that returns one Loan at a time. Effectively, the
#       result will be that you should be able to loop over a LoanPool object’s individual Loan objects. For
#       example, the following should now work:
#           for loan in loanPool:
#               print(loan.notional)

#######################
# Importing necessary packages
from loan.loanpool import LoanPool
from loan.loan_base import Loan
from asset.asset import Asset

#######################

###############################################
def main():
    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test the modified LoanPool class

    ###############################################

    # Test 1
    # 1. Test the modified LoanPool class
    # Scenario: Test iterability of modified LoanPool by using a for loop and print out notional value of loans
    #   in a loanpool objects that consist of multiple Loan objects
    print('Test 1. Test the modified LoanPool class')
    # Initialize values
    loan1 = Loan(100000, .050, 30, Asset(100000))
    loan2 = Loan(200000, .050, 30, Asset(100000))
    loan3 = Loan(1000000, .050, 30, Asset(100000))
    loan4 = Loan(90000, .050, 30, Asset(100000))
    loans = [loan1, loan2, loan3, loan4]
    loanpool1 = LoanPool(loans)

    # For loop to test
    for loan in loanpool1:
        print(loan.notional)
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
