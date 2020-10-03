# Type: Homework
# Level: 6
# Section: 6.2: Concurrency
# Exercise: 1
# Description: Contains the code to simulate the Monte Hall problem, using multiprocessing
#   In this exercise, we will look to make the Monty Hall simulation achieve true multi-processing. This is
#       a good segue to financial Monte Carlo as the concepts and approaches are the same.
#
#   a) Create and initialize five processes. Note that starting processes takes some time, and is the
#       upfront cost of using multi-processing.
#   b) Execute all five processes. Give each process 1/5 of the total simulations (2,000,000 each).
#   c) Combine the five returned results lists and take the average, to get the overall result.
#   d) Time all of the above (starting from b). Does total runtime improve from the previous level?
#   e) Try decreasing/increasing the number of processes to determine the optimal runtime.
#
#   BONUS: Try the above using multithreading and compare/contrast the performance vs. multiprocessing.

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
import datetime
from spv.tranche_base import Tranche
from spv.tranches import StandardTranche
from loan.loanpool import LoanPool
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
from loan.mortgage import FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from asset.asset import Car
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


###############################################
def main():

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    dT_start1 = '2018-08-21 12:5:30:123456'
    dT_start1 = datetime.datetime.strptime(dT_start1, '%Y-%m-%d %H:%M:%S:%f')
    dT_end1 = dT_start1 + datetime.timedelta(days=300)

    dT_start2 = '2018-08-21 12:5:30:123456'
    dT_start2 = datetime.datetime.strptime(dT_start2, '%Y-%m-%d %H:%M:%S:%f')
    dT_end2 = dT_start2 + datetime.timedelta(days=240)

    loan1 = AutoLoan(notional=100000, rate=.08, maturity_start=dT_start1, maturity_end=dT_end1, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=.06, maturity_start=dT_start2, maturity_end=dT_end2, car=Car(75000))
    loans = LoanPool([loan1, loan2])

    sum_principal = loans.totalPrincipal()
    # wA = 0.8
    # wB = 0.2
    rateA = 0.05
    rateB = 0.08
    # notionalA = sum_principal * wA
    # notionalB = sum_principal * wB

    notionalA = 100000
    notionalB = 75000

    termA = 10
    termB = 8
    trancheA = StandardTranche(notionalA, rateA, termA, 'A')
    trancheB = StandardTranche(notionalB, rateB, termB, 'B')

    print(trancheA.__repr__())
    print(trancheB.__repr__())

    print(type(trancheA.increaseTimePeriod))
    print(type(trancheA.makePrincipalPayment))
    print(trancheA.makePrincipalPayment(1))
    print(trancheA.makePrincipalPayment(2))

    print()
    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
