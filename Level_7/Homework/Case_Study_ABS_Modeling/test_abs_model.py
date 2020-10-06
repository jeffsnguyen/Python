# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: Contains the code to test the ABS Model

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
from spv.structured_securities import StructuredSecurities
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


def runWaterfall(loans, tranches):
    structuredSecurities = StructuredSecurities(tranches)
    print(f'Doing work on {structuredSecurities.__repr__()}')

    maxTerm = max(loans.get_term())

    # Set mode Pro Rata or Sequential
    structuredSecurities.mode('Sequential')

    for i in range(1, maxTerm+1):
        collections = loans.paymentDue(i)
        principalCollected = loans.principalDue(i)
        structuredSecurities.get_principalCollected(i, principalCollected)
        structuredSecurities.makePayments(collections)

    # Result
    for tranche in tranches:
        print(f'{tranche} interest due = {tranche.getDict_interestDue()}')
        print(f'{tranche} interest paid = {tranche.getDict_interestPaid()}')
        print(f'{tranche} interest short fall = {tranche.getDict_interestShortFall()}')
        print(f'{tranche} principal due = {tranche.getDict_principalDue()}')
        print(f'{tranche} principal paid = {tranche.getDict_principalPaid()}')
        print(f'{tranche} principal short fall = {tranche.getDict_principalShortFall()}')
        print()

    print(f'Cash reserve account: {structuredSecurities.getDict_reserve()}')


###############################################
def main():

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])
    trancheA = StandardTranche(loans.totalPrincipal() * 0.8, 0.05, 1)
    trancheB = StandardTranche(loans.totalPrincipal() * 0.2, 0.08, 2)
    tranches = [trancheB, trancheA]

    runWaterfall(loans, tranches)
    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
