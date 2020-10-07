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


def doWaterfall(loans, tranches):
    print(f'Doing work on {tranches.__repr__()}')

    # Set mode Pro Rata or Sequential
    tranches.mode('Sequential')

    ledger = {}
    reserve = {}
    t = 0
    while loans.activeLoanCount(t) > 0:
        # Increase the time period on the StructuredSecurities object (which will, in turn, increase for all
        # the tranches).
        tranches.increaseTranchesTimePeriod()
        t += 1
        # Ask the LoanPool for its total payment for the current time period.
        collections = loans.paymentDue(t)

        # Ask the LoanPool for its total principal due for the current time period.
        principalCollected = loans.principalDue(t)
        tranches.save_principalCollected(t, principalCollected)  # Save the principal due

        # Pay the StructuredSecurities with the amount provided by the LoanPool.
        tranches.makePayments(collections)

        # Call getWaterfall on both the LoanPool and StructuredSecurities objects and save the info into
        # two variables.
        ledger[t] = tranches.getWaterfall(t)
        reserve[t] = tranches.reserve[t]

    print(f'My ledger is:\n {ledger}')
    print(f'My cash reserve account:\n {reserve}')

    return ledger, reserve

###############################################
def main():

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    loan1 = AutoLoan(notional=100000, rate=0.08, term=10, car=Car(100000))
    loan2 = AutoLoan(notional=75000, rate=0.06, term=8, car=Car(75000))
    loans = LoanPool([loan1, loan2])

    structuredSecurities = StructuredSecurities(loans.totalPrincipal())
    structuredSecurities.addTranche('StandardTranche', '0.8', '0.05', '1')
    structuredSecurities.addTranche('StandardTranche', '0.2', '0.08', '2')

    doWaterfall(loans, structuredSecurities)

    ###############################################

###############################################


#######################
if __name__ == '__main__':
    main()
