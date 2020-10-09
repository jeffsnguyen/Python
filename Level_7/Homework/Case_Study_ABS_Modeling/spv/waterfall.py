# Type: Homework
# Level: 7
# Section: Case Study: Asset Backed Security Modeling
# Exercise: 1
# Description: This contains the Waterfall function
#   Create a standalone function called doWaterfall. This function should take two parameters: A LoanPool
#       object and a StructuredSecurities object. The function should loop through time periods, starting from
#       0, and keep going until the LoanPool has no more active loans (no more payments coming from the
#       LoanPool). At each time period iteration:
#
#       o Increase the time period on the StructuredSecurities object (which will, in turn, increase for all
#           the tranches).
#       o Ask the LoanPool for its total payment for the current time period.
#       o Pay the StructuredSecurities with the amount provided by the LoanPool.
#       o Call getWaterfall on both the LoanPool and StructuredSecurities objects and save the info into
#           two variables.
#
#   After the loop completes (when all loans in the loan pool have zero balance), return all the results saved
#       down from the getWaterfall function (from both variables) as well as any amount left in the reserve account.

# Importing packages
import logging
from utils.timer import Timer
from spv.tranche_base import Tranche
from spv.structured_securities import StructuredSecurities
#######################

#######################


# Initialize StructuredSecurities tranches
def tranchesInit(loans):
    tranches = StructuredSecurities(loans.totalPrincipal())
    tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    tranches.addTranche('StandardTranche', '0.2', '0.08', '2')
    return tranches


# Run the sequential mode Waterfall one time
def runSequentialSim(loans):
    tranches = tranchesInit(loans)
    tranches.setMode('Sequential')
    return doWaterfall(loans, tranches)


# Run the Pro Rata mode Waterfall one time
def runProRataSim(loans):
    tranches = tranchesInit(loans)
    tranches.setMode('Pro Rata')
    return doWaterfall(loans, tranches)


@Timer
def doWaterfall(loans, tranches):
    print(f'Doing work on {tranches.__repr__()}')
    logging.debug(f'Doing work on {tranches.__repr__()}')

    ledger = [tranches.getWaterfall(0)]
    reserve = []
    t = 0
    while loans.activeLoanCount(t) > 0:
        # Increase the time period on the StructuredSecurities object (which will, in turn, increase for all
        # the tranches).
        tranches.increaseTranchesTimePeriod()
        t += 1

        # Ask the LoanPool for its total payment for the current time period.
        # This is the paymentDue amount plus asset recovery value from defaults
        collections = loans.paymentDue(t)
        recoveries = loans.checkDefaults(t)

        # Ask the LoanPool for its total principal due for the current time period.
        principalCollected = loans.principalDue(t)
        tranches.save_principalCollected(t, principalCollected)  # Save the principal due

        # Pay the StructuredSecurities with the amount provided by the LoanPool.
        tranches.makePayments(collections + recoveries)

        # Call getWaterfall on both the LoanPool and StructuredSecurities objects and save the info into
        # two variables.
        ledger.append(tranches.getWaterfall(t))
        reserve.append(tranches.reserve[t])

    for tranche in tranches.tranches:
        r = tranche.IRR()
        dirr = tranche.getRating(tranche.DIRR())
        al = tranche.AL()
        print(f'{tranche}\nIRR = {r}\nDIRR = {dirr}\nAL = {al}')


    return ledger, reserve
