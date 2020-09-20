# Type: Homework
# Level: 4
# Section: 4.3 File I/O
# Exercise: 5
# Description: Contains the tests for various filepath operations
#   Open the file from 4) and read it. Display each line.
#######################
# Importing necessary packages
import os
import logging
#######################

###############################################
# Add config of log
logging.basicConfig(format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style="{")
###############################################
def main():
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Open the file from 4) and read it. Display each line.

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')

    # Create 1 text files
    # Get current working directory
    logging.debug('Getting current working directory')
    cWD = os.getcwd()

    # Generate new file path
    fName1 = 'babyShark.txt'
    fp1 = os.path.join(cWD, fName1)
    logging.debug(f'New file path: {fp1}')

    logging.info(f'Reading lines from {fp1}.')

    try:  # block to catch if file doesn't exist
        with open(fp1, 'r') as file1:
            for line in file1.readlines():
                logging.info(f'{line}')
    except FileNotFoundError as fnfEx:
        logging.error(f'Failed. {fnfEx}')
    else:
        logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

###############################################

#######################
if __name__ == '__main__':
    main()