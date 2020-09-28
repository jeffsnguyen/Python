# Type: Homework
# Level: 6
# Section: 6.1: Random Number Generation
# Exercise: 2
# Description: Contains the code to write RNGs to CSV
#   Do the same thing as Exercise 1, but this time we are going to print the distribution in the Python
#       shell output. You can do this using horizontal dashes (-). The naive approach would be to print one
#       dash for each time a certain number appears (each number getting its own row of dashes).
#       However, the frequencies will be in the thousands, so using one dash per frequency will overflow
#       the screen. Therefore, to do this properly, you need to scale all the frequencies down (this is called
#       normalizing the curve). We wish to scale each frequency in the histogram to have a min of 1 dash
#       and a max of 100 dashes. We can do so using the following formula:
#
#           \frac{max_{new} - min_{new}}{max_{old} - min_{old}} * (freq - max_{old}) + max_{new}
#       where
#           max_{new} = 100
#           min_{new} = 1
#           max_{old} is the original maximum
#           min_{old} is the original minimum
#   Also, note that you will need to round each decimal value to the nearest integer (we don’t wish to
#       have a separate frequency entry for every decimal). Example output:
#           1: ---
#           2: --------
#           4: -----------
#           7: -------
#           8: --
#           11: -

#######################
# Importing necessary packages
import random
import logging
import statistics
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


# Function to return a list of 200,000 uniform random number in range (1,20)
def uniformRand(lower, upper, size):
    return [random.uniform(lower, upper) for num in range(size)]


# Function to return a list of 200,000 normally distributed random number
def normdistRand(mu, sigma, size):
    return [random.normalvariate(mu, sigma) for num in range(size)]


# Function to return a list of 200,000 normally distributed random number
def lognormdistRand(mu, sigma, size):
    return [random.lognormvariate(mu, sigma) for num in range(size)]


# Frequency count
# Generator to count the number of appearances meeting the given condition
def freq(condition, data):
    return sum(1 for item in data if condition(item))


# Printing scaled distribution
def printDist(distL):
    binned_distL = {}  # Empty dict to house bin values
    n = len(distL)
    sd = statistics.stdev(distL)  # Calculate standard deviation of the sample
    binSize = 3.49 * sd / (n ** (1 / 3))  # calculate bin size using Scott's Rule
    bin_min = min(distL)  # Choosing starting bin min, this is the min of the observation
    bin_max = 1 + binSize  # Choosing starting bin max

    #  Calculating the frequency inside each bin based on the bin size by calling freq()
    while bin_max < max(distL):
        binLabel = str(bin_min) + ', ' + str(bin_max)
        binned_distL[binLabel] = freq(lambda x: bin_min < x < bin_max, distL)
        bin_min += binSize
        bin_max += binSize

    max_new = 100  # Set max number of '-' to print
    min_new = 1  # Set min number of '-' to print
    max_old = max(binned_distL.values())  # Get max value in the dict
    min_old = min(binned_distL.values())  # Get min value in the dict
    scaled_binned_distL = {}  # empty dict to house scaled bin value
    print()

    for key in binned_distL:
        # Scale down the bin using \frac{max_{new} - min_{new}}{max_{old} - min_{old}} * (freq - max_{old}) + max_{new}
        scaledbinFreq = round((((max_new - min_new) / (max_old - min_old)) * (binned_distL[key] - max_old)) + max_new)
        scaled_binned_distL[key] = scaledbinFreq  # Add entry to the dict
        print(f'{key}', end='')  # Print the bin key
        # Print the histogram based on the scaled frequency of each bin
        for i in range(scaledbinFreq):
            print('-', end='')
        print()


###############################################
def main():
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    random.seed(1)  # Set seed

    # Generate list of number
    n = 200000  # number of observations
    uniformL = uniformRand(lower=1, upper=20, size=n)
    normdistL = normdistRand(mu=10, sigma=7, size=n)
    lognormdistL = lognormdistRand(mu=1, sigma=0.5, size=n)

    # Printing uniform distribution
    print(f'Uniformly Distributed Random Numbers from 1-20')
    printDist(uniformL)
    print()

    # Printing normal distribution
    print(f'Normally Distributed Random Numbers mu=10, sigma =7')
    printDist(normdistL)
    print()

    # Printing lognormal distribution
    print(f'Log-normally Distributed Random Numbers mu=1 sigma = 0.5')
    printDist(lognormdistL)
    print()
###############################################


#######################
if __name__ == '__main__':
    main()
