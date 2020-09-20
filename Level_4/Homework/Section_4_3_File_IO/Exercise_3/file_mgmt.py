# Type: Homework
# Level: 4
# Section: 4.3 File I/O
# Exercise: 3
# Description: Contains the tests for various filepath operations
#   Write code that searches your entire computer for all pdf files which reside in any directory (at any
#       level) that contains the string ‘gr’ in its name.
#######################
# Importing necessary packages
import os
import logging
from utils.timer import Timer
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
    #       1. searches your entire computer for all pdf files which reside in any directory (at any
    #          level) that contains the string ‘gr’ in its name.

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')

    # Get current working directory
    cWD = os.getcwd()
    logging.debug(f'Current working directory is: {cWD}.')

    # Set walking path
    walkD = 'C:\\'
    logging.info(f'Path to start walking: {cWD}.')

    # Create empty file list
    fileList = []
    logging.debug(f'Generate empty file list {fileList}.')

    # Set keystring and file extension
    keystr = 'gr'
    fileExt = '.pdf'
    logging.debug(f'Setting key string to be {keystr}.')
    logging.debug(f'Setting file extension to be {fileExt}.')

    # Walking with timer to start search
    with Timer('searchPDF'):
        count = 0  # Count # of files found
        for root, dirs, files in os.walk(walkD):  # walk top down from the preset top directory
            for file in files:
                # If file extension match, and key string found in file name add to list and increase count.
                if file.endswith(fileExt) and (keystr in file):
                    logging.debug(f'Found matching: {file}.')
                    fileList.append(file)
                    count += 1

    logging.info(f'Found {count} files')
    logging.info(f'{fileList}')
    logging.info(f'Success.')
    logging.info(f'#######################{testNum} Completed.')
    #######################

###############################################

#######################
if __name__ == '__main__':
    main()