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
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
from loan.mortgage import MortgageMixin, FixedMortgage, VariableMortgage
from loan.loan_base import Loan
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
import logging
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode = 'a',
                        format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################

# function to handle user prompt to enter loan data
def loanDataEntry():
    # Create dictionary to look up object type.
    loanName = {1: FixedMortgage, 2: AutoLoan }
    assetName = {1: Car, 2: Lambourghini, 3: Lexus, 4: Civic,
                 5: HouseBase, 6: PrimaryHome, 7: VacationHome}
    car_assetName = {1: Car, 2: Lambourghini, 3: Lexus, 4: Civic}
    house_assetName= {5: HouseBase, 6: PrimaryHome, 7: VacationHome}

    # Handle loan type input
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        print('Enter type of loan:\n '
              '1 = FixedMortgage\n '
              '2 = AutoLoan\n')
        try:  # exception block to handle value error
            loanType = int(input('Loan Type = '))
            logging.debug(f'Prompt user to enter Loan type {loanType}.')
        except ValueError as valEx:
            print(f'Failed. Expecting an integer. {valEx}')
            logging.error(f'Failed. {valEx}')
            pass
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            logging.exception(f'Failed. {Ex}')
            pass
        else:  # If int conversion of key is successful
            logging.debug('Conversion of key succeed. Checking if key is in dict.')
            if loanType in loanName:  # if dict lookup succeed, set flag = True to end loop, otherwise, continue
                flag = True
            else:
                logging.debug(f'{loanType} is not valid.')
                print(f'Failed. {loanType} is not valid. Try again.')
                flag = False


    # Handle asset type input
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        logging.debug(f'Checking {loanType} to choose what to display to user.')
        if loanType == 2:  # If loanType is AutoLoan, only shows Car parent and child options
            print('Enter type of asset:\n '
                  '1 = Car\n '
                  '2 = Lambourghini\n '
                  '3 = Lexus\n '
                  '4 = Civic\n ')
            try:  # exception block to handle value error
                assetType = int(input('Asset Type = '))
                logging.debug(f'Prompt user to enter Asset type {assetType}.')
            except ValueError as valEx:
                print(f'Failed. Expecting an integer. {valEx}')
                logging.error(f'Failed. {valEx}')
                pass
            except Exception as Ex:
                print(f'Failed. Unknown error. {Ex}')
                logging.exception(f'Failed. {Ex}')
                pass
            else:  # If int conversion of key is successful
                logging.debug('Conversion of key succeed. Checking if key is in dict.')
                if assetType in car_assetName:  # if dict lookup succeed, set flag = True to end loop, otherwise, continue
                    flag = True
                else:
                    logging.debug(f'{assetType} is not valid.')
                    print(f'Failed. {assetType} is not valid. Try again.')
                    flag = False
        else:  # Else, shows Housebase parent and child options
            logging.debug(f'Checking {loanType} to choose what to display to user.')
            print('Enter type of asset:\n '
                  '5 = HouseBase\n '
                  '6 = PrimaryHome\n '
                  '7 = VacationHome\n')
            try:  # exception block to handle value error
                assetType = int(input('Asset Type = '))
                logging.debug(f'Prompt user to enter Asset type {assetType}.')
            except ValueError as valEx:
                print(f'Failed. Expecting an integer. {valEx}')
                logging.error(f'Failed. {valEx}')
                pass
            except Exception as Ex:
                print(f'Failed. Unknown error. {Ex}')
                logging.exception(f'Failed. {Ex}')
                pass
            else:  # If int conversion of key is successful
                logging.debug('Conversion of key succeed. Checking if key is in dict.')
                if assetType in house_assetName:  # if dict lookup succeed, set flag = True to end loop, otherwise, continue
                    flag = True
                else:
                    logging.debug(f'{assetType} is not valid.')
                    print(f'Failed. {assetType} is not valid. Try again.')
                    flag = False


    # Handle asset value
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        try:  # try-except block to handle value error
            assetVal = float(input('Asset Value (Must be a valid number) = '))
            logging.debug(f'Prompt user to enter asset value {assetVal}.')
        except ValueError as valEx:
            print(f'Failed. Must be a number. {valEx}')
            logging.error(f'Failed. {valEx}')
            pass
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            flag = True

    # Handle notional value
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        try:  # try-except block to handle value error
            notionalVal = float(input('Loan Notional Value (Must be a valid number) = '))
            logging.debug(f'Prompt user to enter loan notional value {notionalVal}.')
        except ValueError as valEx:
            print(f'Failed. Must be a number. {valEx}')
            logging.error(f'Failed. {valEx}')
            pass
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            flag = True

    # Handle rate value
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        try:  # try-except block to handle value error
            rateVal = float(input('Loan Rate Value (Must be a valid number) = '))
            logging.debug(f'Prompt user to enter loan rate value {rateVal}.')
        except ValueError as valEx:
            print(f'Failed. Must be a number. {valEx}')
            logging.error(f'Failed. {valEx}')
            pass
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            flag = True

    # Handle term value
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        try:  # try-except block to handle value error
            termVal = float(input('Loan Term Value (Must be a valid number) = '))
            logging.debug(f'Prompt user to enter loan term value {termVal}.')
        except ValueError as valEx:
            print(f'Failed. Must be a number. {valEx}')
            logging.error(f'Failed. {valEx}')
            pass
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            logging.error(f'Failed. {Ex}')
            pass
        else:
            flag = True

    # Attempt to instantiate the object
    try:
        logging.debug('Attempt to instantiate object.')
        object = loanName[loanType](notionalVal, rateVal, termVal, assetName[assetType](assetVal))
        print(f'{object}')
        return object
    except Exception as Ex:
        print(f'Failed to create loan object. {Ex}')
        logging.exception(f'Failed to instantiate object. {Ex}')
        raise Exception

def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Initiate variable to receive user keyboard input
    master_key = ''
    logging.debug(f'Initiate {master_key} to take user input.')

    # Initiate empty list to save loans
    loans = []
    logging.debug(f'Initiate {loans} to save loan info.')

    loanFile = 'loansRecord.csv' # Initiate a file name variable

    # Master key is the 2 options user are given
    # 1 prompt for data entry
    # 2 save data to CSV file


    master_key = input('Press 1 to enter loan info. Press 2 to write them to CSV. = ')
    # 1 Execute prompt for data entry
    if master_key == '1':
        logging.debug(f'Calling {loanDataEntry} to take user prompt.')
        try:
            loan1 = loanDataEntry()  # Call the module to enter data
            loans.append(loan1)  # add the data entry to a list
        except Exception as Ex:
            print(f'Failed. Unknown error. {Ex}')
            pass
        else:
            logging.debug(f'Data entry successful at {loan1}')
            print(f'Loan entry successfully recorded under: {loan1}.')  # Display record to user
            print(f'Current loans are: {loans}')
            print()
    # 2 Execute prompt for CSV export
    elif master_key == '2':
        try:  # block to catch if file doesn't exist
            with open(loanFile, 'a') as file1:   # open the csv file
                logging.debug(f'Open CSV for append at {loanFile}')
                for loan in loans:  # loop through the list to write to csv
                    logging.debug(f'Writing {loan} to CSV')
                    file1.write(f'{loan.__class__.__name__}, {loan.asset.__class__.__name__}, {loan.asset.initialValue}, {loan.notional}, {loan.rate}, {loan.term}\n')
        except FileNotFoundError as fnfEx:
            logging.error(f'Failed. {fnfEx}')
        else:
            logging.info(f'Success.')

    ###############################################

#######################
if __name__ == '__main__':
    main()
