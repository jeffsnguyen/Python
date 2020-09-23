# Type: Homework
# Level: 4
# Section: 4.3: File I/O
# Exercise: 7
# Description: This contains tests for Loan classes
#   Create a program which does the following:
#
#   a. Gives the user a choice of two options: (1) Add Loan, (2) Write file and exit.
#       i. If user enters ‘1’, prompt the user for the type of Loan, its asset name/value, its face
#           amount, rate, and term. Each prompt should occur one after the other. After the
#           last prompt, save the entry into a Loan object, notify the user that the loan has been
#           recorded, and return to the main menu.
#       ii. If user enters ‘2’, loop through all the entered loans and write them to a file. The file
#           should be in extension .csv. To do this properly, each sub-entry (loan type, asset
#           name, asset value, amount, rate, and term) should be separate by a comma. Each
#           loan should be separated by a newline.
#
#   b. To verify that your generated .csv is a valid .csv file, try opening it in Excel once it has been
#       generated. You should see six columns and the number of rows should reflect the number
#       of loans.

# Importing necessary packages
from loan.loanpool import LoanPool
from loan.loanIO import loanDataEntry, loanReadCSV
import logging
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################


def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Initiate variable to receive user keyboard input
    master_key = ''
    logging.debug(f'Initiate {master_key} to take user input.')

    loanFile = 'loansRecord.csv'  # Initiate a file name variable

    # Initiate empty lists for export and import
    loans_writeCSV = []
    loans_readCSV = []

    # Master key is the 2 options user are given
    # 1 prompt for data entry
    # 2 export data to CSV file
    # 3 import data from CSV file
    # 4 Display WAR WAM of all the loans

    master_key = 100
    while not master_key == '0':
        master_key = input('Press\n'
                           '1 to enter loan info\n'
                           '2 to write them to CSV. (exit to view result)\n'
                           '3 to import from CSV.\n'
                           '4 to see WAR and WAM of all loans (must run #3 import first)\n'
                           '0 to exit (you will lose all progress\n'
                           'Input = ')

        #######################
        # 1 Execute prompt for data entry
        if master_key == '1':
            logging.debug(f'Initiate {loans_writeCSV} to save loan info.')

            try:
                logging.debug(f'Calling {loanDataEntry} to take user prompt.')
                loan1 = loanDataEntry()  # Call the module to enter data
                loans_writeCSV.append(loan1)  # add the data entry to a list
            except Exception as Ex:
                print(f'Failed. Unknown error. {Ex}')
                pass
            else:
                logging.debug(f'Data entry successful at {loan1}')
                print(f'Loan entry successfully recorded under: {loan1}.')  # Display record to user
                logging.info(f'Current loans are: {loans_writeCSV}')
                print()
        #######################

        #######################
        # 2 Execute prompt for CSV export
        elif master_key == '2':
            try:  # block to catch if file doesn't exist
                fileExport = open(loanFile, 'a')
            except FileNotFoundError as fnfEx:
                logging.error(f'Failed. {fnfEx}')
            else:
                logging.info(f'File founded {fileExport}.')
                count = 0
                for loan in loans_writeCSV:  # loop through the list to write to csv
                    logging.debug(f'Writing {loan} to CSV')
                    # Write to CSV
                    fileExport.write(f'{loan.__class__.__name__}, {loan.asset.__class__.__name__}, '
                                     f'{loan.asset.initialValue}, {loan.notional}, {loan.rate}, {loan.term}\n')
                    count += 1
                print(f'Successfully exported {count} loans to {loanFile}. See log for details.')
                print()
                logging.info(f'Successfully exported {count} loans to {loanFile}.')
                logging.info(f'Exported values are: {loans_writeCSV}')

        #######################

        #######################
        # 3 Execute prompt for CSV import
        elif master_key == '3':
            import_loanFile = input('Enter filepath to import = ')
            logging.info(f'Prompt user to choose path for CSV to import. {import_loanFile}')

            try:  # block to catch if file doesn't exist
                fileImport = open(import_loanFile, 'r')
            except FileNotFoundError as fnfEx:
                logging.error(f'Failed. {fnfEx}')
            else:
                logging.info(f'File founded. {import_loanFile}')
                # Loop through line by line
                count = 0
                for line in fileImport:
                    # For each line in the file:
                    # 1. Strip special characters, replace space with '' and split them to a list
                    # 2. Dissect the list by calling loanReadCSV(list), which:
                    # 3. Append the result to a list and/or raise any error.
                    try:
                        loans_readCSV.append(loanReadCSV(line.strip().replace(' ', '').split(',')))
                    except ValueError as valEx:
                        print(f'Failed to process a line, see log.')
                        logging.error(f'Failed to process line. {valEx}')
                    except Exception as Ex:
                        print(f'Failed to process a line, see log.')
                        logging.error(f'Failed to process line. {Ex}')
                    else:
                        logging.info(f'Successfully imported line.')
                        count += 1

                print(f'Successfully imported {count} lines from {import_loanFile}. See log for details.')
                print()
                logging.info(f'Successfully imported {count} lines from {import_loanFile}.')
                logging.info(f'Imported values are: {loans_readCSV}')
        #######################

        #######################
        # Calculate and display WAR WAM
        # Must run #3 first
        elif master_key == '4':
            logging.debug(f'Grabbing loans from {loans_readCSV}')
            print(f' WAR = {LoanPool(loans_readCSV).WAR()}')  # Instantiate LoanPool object and call WAR
            print(f' WAM = {LoanPool(loans_readCSV).WAM()}')  # Instantiate LoanPool object and call WAM
            print()
        #######################

    ###############################################


#######################
if __name__ == '__main__':
    main()
