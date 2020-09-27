# Type: Homework
# Level: 6
# Section: 6.1: Random Number Generation
# Exercise: 1
# Description: Contains the code to write RNGs to CSV
#   Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20.
#       Additionally, generate 200,000 normally distributed random numbers (mu=10, sigma=7) and 200,000
#       lognormally distributed random numbers (mu=1, sigma=0.5).
#       Export these lists of numbers to a single CSV file (should have 200,000 rows and three columns):
#
#       a. Open this CSV file in Excel.
#       b. Create three additional Excel Worksheets (named ‘Uniform’, ‘Normal’, and ‘Lognormal’).
#           Name the original Worksheet ‘Input’.
#       c. In each Worksheet, create a Histogram corresponding to its input data column (Insert->Histogram).
#       d. Notice how the Uniform graph appears almost flat, the normal graph appears to be a bell curve,
#           and the lognormal graph appears to be a bell curve with a large tail.
#
#   This is an example of convergence due to the Law of Large Numbers:
#       If you generate enough random numbers using a certain distribution,
#       it will always start to converge to the distribution.
#
#   Note that you will need to save the result as an Excel spreadsheet (.xlsx) instead of .csv for submission.
#######################
# Importing necessary packages
import random
import logging
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


# Function to return a list of 200,000 uniform random number in range (1,20)
def uniformRand(lower, upper):
    return [random.uniform(lower, upper) for num in range(200000)]


# Function to return a list of 200,000 normally distributed random number
def normdistRand(mu, sigma):
    return [random.normalvariate(mu, sigma) for num in range(200000)]


# Function to return a list of 200,000 normally distributed random number
def lognormdistRand(mu, sigma):
    return [random.lognormvariate(mu, sigma) for num in range(200000)]


###############################################
def main():
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    random.seed(1)  # Set seed

    # Generate list of number
    uniformL = uniformRand(1, 20)
    normdistL = normdistRand(mu=10, sigma=7)
    lognormdistL = lognormdistRand(mu=1, sigma=0.5)

    masterL = list(zip(uniformL, normdistL, lognormdistL))  # Zip together for CSV export

    fileExport = 'rng.csv'  # Set export file name
    count = 0  # count lines
    with open(fileExport, 'w') as f:  # open file to write
        for item in masterL:  # write 1 tuple of the list at a time
            logging.debug(f'Writing {item} to CSV')
            f.write(f'{item[0]}, {item[1]}, {item[2]}\n')
            count += 1

    print(f'Exported {count} lines to {fileExport}')


###############################################


#######################
if __name__ == '__main__':
    main()
