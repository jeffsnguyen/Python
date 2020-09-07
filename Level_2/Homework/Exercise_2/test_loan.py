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
