# Type: Homework
# Level: 4
# Section: 4.3 File I/O
# Exercise: 1
# Description: Contains the tests for various filepath operations
#   To practice file management, do the following in order (using Python code):
#       a. Create a new directory.
#       b. Rename the above directory.
#       c. Delete the above directory.
#       d. Create another directory and create two text files in this directory.
#       e. Delete one of the text files from the above directory.
#       f. Rename the remaining text file.
#       g. Create a subdirectory within the above created directory.
#       h. Move the remaining text file into the subdirectory.
#       i. Remove the top level directory with all its contents (using a single function call). Be careful!
#######################
# Importing necessary packages
import os
import logging
import shutil
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
    #       1A. Test the 'Create a new directory' exercise
    #       1B. Rename the directory.
    #       1C. Delete the directory
    #       1D. Create another directory and create two text files in this directory.
    #       1E. Delete one of the text files from the above directory.
    #       1F. Rename the remaining text file.
    #       1G. Create a subdirectory within the above created directory.
    #       1H. Move the remaining text file into the subdirectory.
    #       1I. Remove the top level directory with all its contents (using a single function call). Be careful!

    #######################
    # Test 1A
    testNum = 'Test 1A'
    logging.info(f'{testNum}')

    dName = 'New_Directory'

    # Create the new directory
    try:  # try-except block to catch if directory already exist
        logging.debug('Trying to create new directory.')
        os.mkdir(dName)  # create the directory
    except FileExistsError as fileeEx:
        logging.error(f'Failed. {fileeEx}')
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')
    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1B
    testNum = 'Test 1B'
    logging.info(f'{testNum}')

    new_dName = 'Rename_Directory'
    try:  # block to catch if directory already exists.
        logging.debug('Trying to rename directory')
        os.rename(dName, new_dName)
    except FileExistsError as fileeEx:
        logging.error(f'Failed.{fileeEx}')
        pass
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1C
    testNum = 'Test 1C'
    logging.info(f'{testNum}')

    remove_dName = 'Rename_Directory'

    try:  # block to catch if directory already removed.
        logging.debug(f'Trying to remove directory {remove_dName}.')
        os.rmdir(remove_dName)
    except FileNotFoundError as filenfEx:
        logging.error(f'Failed.{filenfEx}')
        pass
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1D
    testNum = 'Test 1D'
    logging.info(f'{testNum}')

    new_dName = 'Another_Directory'

    # Create new directory
    try:  # block to catch if directory already removed.
        logging.debug(f'Trying to create new directory {new_dName}.')
        os.mkdir(new_dName)
    except FileExistsError as fileeEx:
        logging.error(f'Failed.{fileeEx}')
        pass
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
    else:
        logging.info(f'Success.')

    # Create 2 text files inside new directory
    # Get current working directory
    logging.debug('Getting current working directory')
    cWD = os.getcwd()

    # Set master working directory
    masterWD = cWD

    logging.info(f'Current working directory is at {cWD}.')

    # Set new working directory
    logging.debug('Create new working directory path.')
    newWD = os.path.join(cWD, new_dName)
    logging.info(f'New working directory will be at {newWD}.')

    # Change to new working directory
    os.chdir(newWD)
    cWD = os.getcwd()
    logging.debug('Success.')
    logging.info(f'Current working directory is at {cWD}.')

    # Generate new file path
    logging.debug('Creating file 1')
    fName1 = 'file1.txt'
    fp1 = os.path.join(cWD, fName1)
    logging.debug(f'New file path: {fp1}')

    logging.debug(f'Creating new file at {fp1}.')
    with open(fp1, 'w') as file1:
        file1.write('File creation success.')

    logging.debug('Creating file 2')
    fName2 = 'file2.txt'
    fp2 = os.path.join(cWD, fName2)
    logging.debug(f'New file path: {fp2}')

    logging.debug(f'Creating new file at {fp2}.')
    with open(fp2, 'w') as file2:
        file2.write('File creation success.')

    logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1E
    testNum = 'Test 1E'
    logging.info(f'{testNum}')

    remove_fName = 'file1.txt'

    try:  # block to catch if directory already removed.
        logging.debug(f'Trying to remove file {remove_fName}.')
        os.remove(remove_fName)
    except FileNotFoundError as filenfEx:
        logging.error(f'Failed.{filenfEx}')
        pass
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1F
    testNum = 'Test 1F'
    logging.info(f'{testNum}')

    new_fName = 'renamed_file2.txt'
    try:  # block to catch if file already exists.
        logging.debug('Trying to rename file')
        os.rename(fName2, new_fName)
    except FileExistsError as fileeEx:
        logging.error(f'Failed.{fileeEx}')
        pass
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1G
    testNum = 'Test 1G'
    logging.info(f'{testNum}')

    new_dName = 'New_SubDirectory'

    # Create the new directory
    try:  # try-except block to catch if directory already exist
        logging.debug('Trying to create new directory.')
        os.mkdir(new_dName)  # create the directory
    except FileExistsError as fileeEx:
        logging.error(f'Failed. {fileeEx}')
    except Exception as Ex:
        logging.exception(f'Failed {Ex}')
        pass
    else:
        logging.info(f'Success.')
    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1H
    testNum = 'Test 1H'
    logging.info(f'{testNum}')

    # Display current working directory
    cWD = os.getcwd()
    logging.info(f'Your current directory is {cWD}.')

    # Set destination to move files:
    destPath = os.path.join(cWD, new_dName)
    logging.info(f'Content will be moved under {destPath}.')

    # Get list of file to be moved
    files = os.listdir(cWD)
    logging.debug(f'List of files to be moved {files}.')

    # Doing the move
    for file in files:
        try:  # catch any exception of the move
            logging.debug('Doing the move.')
            shutil.move(file, destPath)
        except shutil.Error as shutilEx:
            logging.error(f'Failed. {shutilEx}.')
        except Exception as Ex:
            logging.exception(Ex)
            pass
        else:
            logging.info('Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test 1I
    testNum = 'Test 1I'
    logging.info(f'{testNum}')

    # Display current working directory
    cWD = os.getcwd()
    logging.info(f'Your current directory is {cWD}.')

    # Going back to master directory:
    os.chdir(masterWD)
    cWD = os.getcwd()
    logging.debug(f'Your current directory is {cWD}.')

    delete_dName = 'Another_Directory'
    logging.debug(f'Deleting this {delete_dName}.')

    # Assign the specific path to delete
    delete_dPath = os.path.join(cWD, delete_dName)
    logging.info(f'Deleting everything under {delete_dPath}.')

    try:  # Catching unknown exception
        shutil.rmtree(delete_dPath)
    except Exception as Ex:
        logging.exception(f'Failed. {Ex}')
        pass
    else:
        logging.info('Success.')

    logging.info(f'#######################{testNum} Completed.')
    #######################

###############################################


#######################
if __name__ == '__main__':
    main()
