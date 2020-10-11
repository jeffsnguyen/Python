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
from utils.called_once import calledOnce
from math import e, sqrt
from utils.import_export import spvExportCSV

#######################

#######################


def calculateDiff(nA, nB, lastARate, lastBRate, newARate, newBRate):
    return (nA * abs((lastARate - newARate) / lastARate) + nB * abs((lastBRate - newBRate) / lastBRate)) / (nA + nB)


def getNewRate(oldTrancheRate, coeff, yieldVal):
    return oldTrancheRate + coeff * (yieldVal - oldTrancheRate)


def calculateYield(dirrAvg, alAvg):
    return ((7 / (1 + 0.08 * e**(-0.19 * alAvg / 12))) + (0.019 * sqrt((alAvg / 12) * dirrAvg * 100))) / 100


# Run the Monte Carlo nsim number of  time
# Each simulation:
#   Inner simulation: calculate the average DIR and AL across all Monte Carlo scenarios (in LoanPool checkDefaults())
#   Outer simulation: calculate yield from specific yield curve (using DIRR and AL from inner sim) to arrive at
#       a new rate for each tranches.
# Rinse and repeat until the yield curve converges
@Timer
def runMonte(loans, tranches, tolerance, nsim):
    #tranches.addTranche('StandardTranche', '0.8', '0.05', '1')
    #tranches.addTranche('StandardTranche', '0.2', '0.08', '2')

    coeffList = [1.2, 0.8]  # 1.2 for A and 0.8 for B, list is in descending subordination order

    while True:
        oldTrancheRate = [tranche.rate for tranche in tranches.tranches]
        ledger, reserve, tranchesMetrics = simulateWaterfall(loans, tranches, nsim)  # Save down result
        # Calculate yield
        # Return a list of yield, each list item represents a yield for a tranche
        yieldVal = [calculateYield(tranche[0], tranche[1]) for tranche in tranchesMetrics]
        newTrancheRate = [getNewRate(oldTrancheRate[i], coeffList[i], yieldVal[i]) for i, tranche in enumerate(oldTrancheRate)]
        trancheNotional = [tranche.notional for tranche in tranches.tranches]

        diff = calculateDiff(trancheNotional[0], trancheNotional[1],
                             oldTrancheRate[0], oldTrancheRate[1],
                             newTrancheRate[0], newTrancheRate[1])

        # If diff <= tolerance, finish Monte Carlo and break the loop
        # If diff > tolerance, reassign tranche rate to newly calculate rate and loop again.
        if diff <= tolerance:
            break

        elif diff > tolerance:
            for i, tranche in enumerate(tranches.tranches):
                tranche.rate = newTrancheRate[i]

    print(f'Monte Carlo simulation for yield converge completed.')
    for tranche in tranches.tranches:
        print(f'{tranche}\n'
              f' IRR = {tranche.r}\n'
              f' DIRR = {tranche.dirr}\n'
              f' DIRR(letter) = {tranche.dirrLetter} \n'
              f' AL = {tranche.al}')
    return ledger

# Run Waterfall nsim time
def simulateWaterfall(loans, tranches, nsim):
    # Init 2 tuples of 2 list, each list store a tranche metric, in descending subordination order
    dirrList = ([], [])
    alList = ([], [])

    for i in range(nsim):
        logging.error(f'Currently running simulation # {i}')
        ledger, reserve, metrics = doWaterfall(loans, tranches)

        # Save the metrics from doWaterfall() result.
        # Metrics is a list of n tuples of 4, each tuple represents a tranche, in descending subordination order
        # Tuple values: (irr, dirr, dirr letter rating, and al)
        for j, tranche in enumerate(metrics):
            dirrList[j].append(tranche[1])
            if None not in tranche:
                alList[j].append(tranche[3])

    # Creating a zip element of n tuples,
    #   Each tuple contains 2 lists: 1 of DIRR values and 1 of AL values, in this order
    # Create a list of n tuple, each tuple has 2 elements representing: (average DIRR, averageAL) for each tranche
    #   Data from the zip elements
    tranchesMetrics = \
        [(sum(tranche[0])/len(tranche[0]), sum(tranche[1])/len(tranche[1])) for tranche in zip(dirrList, alList)]

    return ledger, reserve, tranchesMetrics


def doWaterfall(loans, tranches):
    [tranche.reset() for tranche in tranches.tranches]
    tranches.reset()

    #print(f'Doing work on {tranches.__repr__()}')
    #logging.debug(f'Doing work on {tranches.__repr__()}')

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

    # For each tranches, save its metrics as a tuple of 4 values
    # Method is to call these tranche's methods. Calling these methods also save the metric in the tranche's params
    # For a 2 tranches securities, the metrics list will be a list of 2 tuples, each tuples has 4 values
    # The metrics to be saved are: IRR, DIRR, letter DIRR rating, and AL
    metrics = []
    for tranche in tranches.tranches:
        metrics.append((tranche.IRR(), tranche.DIRR(), tranche.DIRRLetter(), tranche.AL()))

    return ledger, reserve, metrics
