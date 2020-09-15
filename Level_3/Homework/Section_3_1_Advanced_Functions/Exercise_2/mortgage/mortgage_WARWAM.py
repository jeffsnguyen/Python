# Type: Homework
# Level: 3
# Section: 3.1: Advanced Functions
# Exercise: 2
# Description: Contains the methods to calculate WAR, WAM using reduce
#  This exercise is a modification of Exercise 1.5.8, to use the reduce function. In Exercise 1.5.8, we
#       created functions to calculate the WAM and WAR of a list of mortgage tuples.
#   a. Create an alternate version of WAM, which takes a list of mortgage tuples; for this version,
#       use the reduce function, with a regular function as its callable, to calculate the WAM.
#   b. Create an alternate version of WAR, which takes a list of mortgage tuples; for this version,
#       use the reduce function, with a lambda as its callable, to calculate the WAR of the list of rates.
#   c. Modify your WAR and WAM functions in your LoanPool class to take the above reduce
#       approach instead of the previous approach.

# Importing necessary packages
from functools import reduce


###############################################
# Return the Weighted Average Rate of the mortgage pool
# Modified to use lambda function
def WAR_mortgage(pool):
    # Start from warValue = 0
    # For each value pair inside pool list, multiply notional [0] with term [2]
    #   and divided by sum of notionals (using a generator).
    #   Add to wamValue and iterate through the next on the list pool
    return reduce(lambda warValue, weighted_rate: warValue + (weighted_rate[0] * weighted_rate[1] /
                                                              sum(weighted_rate[0] for weighted_rate in pool)), pool, 0)


# Return the Weighted Average Maturity of the mortgage pool
# Modified to use lambda function
def WAM_mortgage(pool):
    # Start from wamValue = 0
    # For each value pair inside pool list, multiply notional [0] with term [2]
    #   and divided by sum of notionals (using a generator).
    #   Add to wamValue and iterate through the next on the list pool
    return reduce(lambda wamValue, weighted_rate: wamValue + (weighted_rate[0] * weighted_rate[2] /
                                                              sum(weighted_rate[0] for weighted_rate in pool)), pool, 0)

###############################################
