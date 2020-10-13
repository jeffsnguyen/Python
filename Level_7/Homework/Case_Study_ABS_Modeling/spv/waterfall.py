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
import math
import numpy
import multiprocessing
import functools

#######################

#######################


# Run the Monte Carlo nsim number of  time, using multiprocessing
# Each simulation:
#   Inner simulation: calculate the average DIR and AL across all Monte Carlo scenarios (in LoanPool checkDefaults())
#   Outer simulation: calculate yield from specific yield curve (using DIRR and AL from inner sim) to arrive at
#       a new rate for each tranches.
# Rinse and repeat until the yield curve converges
@Timer
def runMonte(loans, tranches, tolerance, nsim, numProcesses):
    coeffList = [1.2, 0.8]  # 1.2 for A and 0.8 for B, list is in descending subordination order
    trancheNotional = [tranche.notional for tranche in tranches.tranches]
    print(f'trancheNotional = {trancheNotional}')
    oldTrancheRate = [tranche.rate for tranche in tranches.tranches]
    print(f'oldTrancheRate = {oldTrancheRate}')
    while True:
        print(f'Optimizing new rate, end when diff < {tolerance}.')
        tranchesMetrics = runSimulationParallel(loans, tranches, nsim, numProcesses)
        # Calculate yield
        # Return a list of yield, each list item represents a yield for a tranche
        yieldVal = [calculateYield(tranche[0], tranche[1]) for tranche in tranchesMetrics]
        newTrancheRate = \
            [getNewRate(oldTrancheRate[i], coeffList[i], yieldVal[i]) for i, tranche in enumerate(oldTrancheRate)]

        diff = calculateDiff(trancheNotional[0], trancheNotional[1],
                             oldTrancheRate[0], oldTrancheRate[1],
                             newTrancheRate[0], newTrancheRate[1])

        print(f'Metrics:\n'
              f' yieldVal = {yieldVal}\n'
              f' newTrancheRate = {newTrancheRate}\n'
              f' diff = {round(diff, 3)}\n')

        # If diff <= tolerance, finish Monte Carlo and break the loop
        # If diff > tolerance, reassign tranche rate to newly calculate rate and loop again.
        if round(diff, 3) < tolerance:
            break
        else:
            oldTrancheRate = newTrancheRate
            for i, tranche in enumerate(tranches.tranches):
                tranche.rate = newTrancheRate[i]

    print(f'Monte Carlo simulation for yield converge completed.')

    return newTrancheRate


# Run Waterfall on multiprocessing
def runSimulationParallel(loans, tranches, nsim, numProcesses):
    # Create input/output queue
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    jobs = []  # Job list for each process
    ####################

    # Create child processes
    print(f'Running {nsim} simulation with {numProcesses} processes...')
    for i in range(numProcesses):
        # Each item in the queue to have a tuple of a function simulateWaterfall
        #   and a list of arguments
        input_queue.put((simulateWaterfall, (loans, tranches, int(nsim / numProcesses))))

        # target = doWork is the function for the process to call. doWork handling processing of the iterations
        # args = arguments to get passed to the target = doWork()
        p = multiprocessing.Process(target=doWork, args=(input_queue, output_queue))
        p.start()
        jobs.append(p)  # Add each process to the job list

    ####################
    # Create an infinite loop and monitor output queue
    # Final resultList is a list with nsim * 0.5 pair of tuple
    #   Each pair has the format (avgDIRR_A, avgAL_A), (avgDIRR_B, avgAL_B)
    resultList = []
    while len(resultList) < numProcesses*2:
        r = output_queue.get()  # Take something off the queue, if queue has nothing, it will block (wait)
        # until the queue has something, while other processes running in the background
        # when it has something, add it to the list resultList = []
        resultList.extend(r)  # When done, break the loop
        print(f'Currently at {len(resultList)} results. Completion at {numProcesses*2} results.')

    # Get trancheA data by using list comp on even number index in resultList
    # Remaining data go to trancheB
    trancheA_data = [resultList[i] for i in range(len(resultList)) if i % 2 == 0]
    trancheB_data = [item for item in resultList if item not in trancheA_data]

    results = [functools.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), trancheA_data),
               functools.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), trancheB_data)]

    # Aggregating results and add to results list
    res = [(results[0][0] / len(trancheA_data), (results[0][1] / len(trancheA_data))),
           (results[1][0] / len(trancheB_data), (results[1][1] / len(trancheB_data)))]

    # Clean up crew
    for job in jobs:
        job.terminate()
        job.join()

    return res


# Function to process the iteration
def doWork(input, output):  # 2 parameters input queue and output queue
    f, args = input.get(timeout=1)
    resLedger, resTranchesMetrics = f(*args)
    output.put(resTranchesMetrics)


# Run Waterfall nsim time
def simulateWaterfall(loans, tranches, nsim):
    # Init 2 tuples of 2 list, each list store a tranche metric, in descending subordination order
    dirr_trancheA = []
    dirr_trancheB = []
    al_trancheA = []
    al_trancheB = []

    for i in range(nsim):
        ledger, metrics = doWaterfall(loans, tranches)

        # Save the metrics from doWaterfall() result.
        # Metrics is a list of n tuples of 4, each tuple represents a tranche, in descending subordination order
        # Tuple values: (irr, dirr, dirr letter rating, and al)
        dirrA = metrics[0][1]
        alA = metrics[0][3]
        dirrB = metrics[1][1]
        alB = metrics[1][3]
        if not numpy.isnan(metrics[0][1]):
            dirr_trancheA.append(dirrA)
        if not numpy.isnan(metrics[1][1]):
            dirr_trancheB.append(dirrB)
        if alA is not None:
            al_trancheA.append(alA)
        if alB is not None:
            al_trancheB.append(alB)

    # Create a list of 2 tuple, each tuple has 2 elements representing: (average DIRR, averageAL) for each tranche
    tranchesMetrics = [(numpy.mean(dirr_trancheA), numpy.mean(al_trancheA)),
                       (numpy.mean(dirr_trancheB), numpy.mean(al_trancheB))]

    return ledger, tranchesMetrics


def doWaterfall(loans, tranches):
    tranches.reset()
    loans.reset()

    logging.debug(f'Doing work on {tranches.__repr__()}')

    ledger = [tranches.getWaterfall(0)]
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

    # For each tranches, save its metrics as a tuple of 4 values
    # Method is to call these tranche's methods. Calling these methods also save the metric in the tranche's params
    # For a 2 tranches securities, the metrics list will be a list of 2 tuples, each tuples has 4 values
    # The metrics to be saved are: IRR, DIRR, letter DIRR rating, and AL
    metrics = [(tranche.IRR(), tranche.DIRR(), tranche.DIRRLetter(), tranche.AL()) for tranche in tranches.tranches]

    return ledger, metrics


def calculateDiff(nA, nB, lastARate, lastBRate, newARate, newBRate):
    return (nA * abs((lastARate - newARate) / lastARate) + nB * abs((lastBRate - newBRate) / lastBRate)) / (nA + nB)


def getNewRate(oldTrancheRate, coeff, yieldVal):
    return oldTrancheRate + coeff * (yieldVal - oldTrancheRate)


def calculateYield(dirrAvg, alAvg):
    return ((7 / (1 + 0.08 * math.e**(-0.19 * alAvg / 12))) + (0.019 * math.sqrt((alAvg / 12) * dirrAvg * 100))) / 100
