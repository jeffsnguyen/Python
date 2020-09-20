# Type: Homework
# Level: 4
# Section: 4.3 File I/O
# Exercise: 4
# Description: Contains the tests for various filepath operations
#   Open a brand-new file and write to it (should write several lines).
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
    #       1. Open a brand-new file and write to it (should write several lines).

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')

    # Create 1 text files
    # Get current working directory
    logging.debug('Getting current working directory')
    cWD = os.getcwd()

    # Generate new file path
    logging.debug('Creating file 1')
    fName1 = 'babyShark.txt'
    fp1 = os.path.join(cWD, fName1)
    logging.debug(f'New file path: {fp1}')

    logging.debug(f'Creating new file at {fp1}.')
    with open(fp1, 'w') as file1:
        file1.write('File creation success.\n')
        file1.write('Baby shark, doo, doo, doo, doo, doo, doo\n')
        file1.write('Baby shark, doo, doo, doo, doo, doo, doo\n')
        file1.write('Baby shark, doo, doo, doo, doo, doo, doo\n')
        file1.write('Baby shark')

    logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

###############################################

#######################
if __name__ == '__main__':
    main()