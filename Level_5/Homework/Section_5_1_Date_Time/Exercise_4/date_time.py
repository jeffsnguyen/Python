# Type: Homework
# Level: 5
# Section: 5.1 Date/Time
# Exercise: 4
# Description: Contains the tests for various Date/Time operations
#   Create a ‘date calculator’ program. It should do the following:
#       a. Prompt the user to enter any date and time.
#       b. Prompt the user to enter a delta time that is used to add or subtract from the original. For
#           example, if the user enters -00:25:13:0 then subtract 25 minutes and 13 seconds (and zero
#           microseconds). Another example: 72:12:00:154 means to add 72 hours, 12 minutes, and 154 microseconds.
#       c. Display the calculated resulting date and time, in an easily-readable format.
#######################
# Importing necessary packages
import logging
import datetime
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')


###############################################
def main():
    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    # Testing block
    # Scenario:
    #   This block will:
    #       a. Handle datetime input in the format: 2016-09-25 18:23:14:12342
    #       bc. Handle timedelta addition and subtraction.

    #######################
    # Test a
    testNum = 'Test a'
    logging.info(f'{testNum}')
    print('a. Handle datetime input in the format: 2016-09-25 18:23:14:12342')
    logging.info('a. Handle datetime input in the format: 2016-09-25 18:23:14:12342')
    # 2020-09-23 1:6:30:123456
    # Taking user inputs
    logging.info('Taking user inputs')
    date_time = input('Enter date time 2020-09-23 1:6:30:123456 = ')
    try:  # Exception Handling block to handle datetime conversion
        date_time = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S:%f')
    except Exception as Ex:
        print(f'Failed. Incorrect format. See log for more details.')
        logging.error(f'Failed. {Ex}')
        pass
    else:
        print(f'{date_time} Entered.')
        logging.info(f'Input accepted. {date_time}')
        pass
    print()

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test bc
    testNum = 'Test bc'
    logging.info(f'{testNum}')
    print('bc. Handle timedelta addition and subtraction')
    logging.info('b. Handle timedelta addition and subtraction')
    # 2020-09-23 1:6:30:123456
    # Taking user inputs
    logging.info('Taking user inputs')
    time_delta = input('Enter time delta 1:6:30:123456 = ')
    negFlag = False
    if time_delta[0] == '-':  # If see minus sign, set flag true and split '-', grab the index 1 which is the time
        negFlag = True
        time_delta = time_delta.split('-')[1]

    try:  # Exception Handling block to handle datetime conversion
        time_delta = datetime.datetime.strptime(time_delta, '%H:%M:%S:%f')
    except Exception as Ex:
        print(f'Failed. Incorrect format. See log for more details.')
        logging.error(f'Failed. {Ex}')
        pass
    else:
        print(f'-{time_delta} Entered.') if negFlag else print(f'{time_delta} Entered.')

        # Extract parameters from time_delta
        hour = time_delta.hour
        minute = time_delta.minute
        second = time_delta.second
        microsecond = time_delta.microsecond

        # Handle addition and subtraction
        if negFlag:
            date_timeR = date_time - datetime.timedelta\
                        (hours=hour, minutes=minute, seconds=second, microseconds=microsecond)
            print(f'{date_time} - {time_delta} = {date_timeR}')
        else:
            date_timeR = date_time + datetime.timedelta\
                        (hours=hour, minutes=minute, seconds=second, microseconds=microsecond)
            print(f'{date_time} + {time_delta} = {date_timeR}')

        logging.debug(f'Successfully calculated {date_timeR}')
    print()

    logging.info(f'#######################{testNum} Completed.')

###############################################


#######################
if __name__ == '__main__':
    main()
