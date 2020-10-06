# Type: Homework
# Level: 4
# Section: 4.3: File I/O
# Exercise: 8
# Description: This contains various file input/output operations for Loan/Asset/Mortgage
#   As a follow-up, create a third option: (3) Read loan .csv file. This option should:
#       a. Ask the user to enter a file path of the loan .csv file.
#       b. Load the .csv file into Loan objects.
#       c. Add an additional (fourth) option to display the WAR and WAM of all the loans.

# Importing packages
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
from loan.mortgage import MortgageMixin, FixedMortgage, VariableMortgage
from loan.loans import FixedRateLoan, VariableRateLoan, AutoLoan
import logging


#######################
# Function to handle user prompt to enter loan data
def loanDataEntry():
    # Create dictionary to look up object type.
    loanName = {1: FixedMortgage, 2: AutoLoan}
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
            logging.debug(f'Prompt user to enter Loan type {loanName[loanType].__name__}.')
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
                logging.debug(f'{loanName[loanType].__name__} is a valid class.')
            else:
                logging.debug(f'{loanName[loanType].__name__} is not valid.')
                print(f'Failed. {loanName[loanType].__name__} is not valid. Try again.')
                flag = False

    # Handle asset type input
    logging.debug('Starting a loop to handle value error.')
    flag = False
    while not flag:
        logging.debug(f'Checking {loanName[loanType].__name__} to choose what to display to user.')
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
                    logging.debug(f'{assetName[assetType].__name__} is a valid class.')
                else:
                    logging.debug(f'{assetName[assetType].__name__} is not valid.')
                    print(f'Failed. {assetName[assetType].__name__} is not valid. Try again.')
                    flag = False
        else:  # Else, shows Housebase parent and child options
            logging.debug(f'Checking {loanType} to choose what to display to user.')
            print('Enter type of asset:\n '
                  '5 = HouseBase\n '
                  '6 = PrimaryHome\n '
                  '7 = VacationHome\n')
            try:  # exception block to handle value error
                assetType = int(input('Asset Type = '))
                logging.debug(f'Prompt user to enter Asset type {assetName[assetType].__name__}.')
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
                    logging.debug(f'{assetName[assetType].__name__} is a valid class.')
                else:
                    logging.debug(f'{assetName[assetType].__name__} is not valid.')
                    print(f'Failed. {assetName[assetType].__name__} is not valid. Try again.')
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
        logging.debug(f'{loanName[loanType].__name__}')
        logging.debug(f'{assetName[assetType].__name__}')
        object = loanName[loanType](notionalVal, rateVal, termVal, assetName[assetType](assetVal))
        print(f'{object}')
        return object
    except Exception as Ex:
        print(f'Failed to create loan object. {Ex}')
        logging.exception(f'Failed to instantiate object. {Ex}')
        raise Exception
#######################


#######################
# Function to handle reading CSV and instantiates objects
# Dissect the list of values from the CSV by:
#       i. Go through each value on the stripped list
#       ii. Attempt to match these value with a preset dict that contain necessary classes' names
#       iii. Do error handling on these names as well as validating numerical value
#       iv. Attempt to instantiate the object.
def loanReadCSV(lineItem):
    lookup_dict = {'loanName': {1: FixedMortgage, 2: AutoLoan},
                   'assetName': {1: Car, 2: Lambourghini, 3: Lexus, 4: Civic,
                                 5: HouseBase, 6: PrimaryHome, 7: VacationHome}}

    # Grab loan class and save to loanName
    for key in lookup_dict['loanName']:  # Look up and match the list value with the dict key
        if lineItem[0] == lookup_dict["loanName"].get(key).__name__:
            loanName = lookup_dict["loanName"].get(key)

    # Grab asset class and save to assetName
    for key in lookup_dict['assetName']:  # Look up and match the list value with the dict key
        if lineItem[1] == lookup_dict['assetName'].get(key).__name__:
            assetName = lookup_dict['assetName'].get(key)

    # Grab asset value and save to assetVal
    try:
        assetVal = float(lineItem[2])
    except ValueError as valEx:
        logging.error(f'Invalid value. Expect number. {valEx}')
        raise ValueError('Invalid value. Expect a number.')
        pass

    # Grab loan notional value and save to notionalVal
    try:
        notionalVal = float(lineItem[3])
    except ValueError as valEx:
        logging.error(f'Invalid value. Expect number. {valEx}')
        raise ValueError('Invalid value. Expect a number.')
        pass

    # Grab loan rate value and save to rateVal
    try:
        rateVal = float(lineItem[4])
    except ValueError as valEx:
        logging.error(f'Invalid value. Expect number. {valEx}')
        raise ValueError('Invalid value. Expect a number.')
        pass

    # Grab loan term value and save to termVal
    try:
        termVal = float(lineItem[5])
    except ValueError as valEx:
        logging.error(f'Invalid value. Expect number. {valEx}')
        raise ValueError('Invalid value. Expect a number.')
        pass

    # Attempt to instantiate the object
    try:
        logging.debug('Attempt to instantiate object.')
        object = loanName(notionalVal, rateVal, termVal, assetName(assetVal))
        return object
    except Exception as Ex:
        print(f'Failed to create loan object. {Ex}')
        logging.exception(f'Failed to instantiate object. {Ex}')
        raise Exception