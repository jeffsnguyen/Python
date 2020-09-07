# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 3
# Description: This contains the test function for the Exercise 3, Loan class
#   Interest due at time T on a loan depends on the outstanding balance. Principal due is the monthly
#   payment less the interest due. Conceptually, these are recursive calculations as one can determine
#   the interest/principal due at time T if one knows the balance at time T-1 (which, in turn, can be
#   determined if one knows the balance at time T-2).
#   For each of the below functions, implement two versions: A recursive version (per the above
#   statement) and a version that uses the formulas provided in the slides:
#       a. The interest amount due at a given period (interestDue).
#       b. The principal amount due at a given period (principalDue).
#       c. The balance of the loan at a given period (balance).

# Importing necessary packages

from Loan.loan_base import Loan

#######################


def main():
    # Initialize a loan
    #######################
    loan1 = Loan(100000, .045, 30)
    #######################
    print('Loan info: ' + str(loan1.notional) + ' loan, at monthly rate of ' + str(loan1.rate) + ' over '
          + str(loan1.term) + ' months.')

    #######################
    # 2.a Demo monthlyPayment function
    print('The monthly payment of this loan is: ', loan1.monthlyPayment())
    #######################

    #######################
    # 2.b Demo totalPayments function
    print('The total payment (principal + interest) of this loan is: ', loan1.totalPayments())
    #######################

    #######################
    # 2.c Demo totalInterest function
    print('The total interest payment of this loan is: ', loan1.totalInterest())
    #######################


#######################
if __name__ == '__main__':
    main()
