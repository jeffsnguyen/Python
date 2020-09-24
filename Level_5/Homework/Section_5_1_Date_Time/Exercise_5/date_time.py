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

# Function to convert datetime to extracted total (total days, hours, etc.)
def dateTimeConvert(dT_str, dT):
    # Create a lookup dict
    dT_dict = {'days': 86400000000,
               'hours': 3600000000,
               'minutes': 60000000,
               'seconds': 1000000,
               'microseconds': 1}

    # Calculate total microseconds as the base
    total_microseconds = dT.days * dT_dict['days'] + dT.seconds * dT_dict['seconds'] + dT.microseconds
    logging.debug(f'Total base microseconds = {total_microseconds}')

    return total_microseconds / dT_dict[dT_str]


# Function to subtract 2 datetime
def dateDiff():

    #######################
    # Taking user input dT1
    logging.info('Taking user inputs')
    dT1 = input('Enter date time 2020-09-23 1:6:30:123456 = ')
    try:  # Exception Handling block to handle datetime conversion
        dT1 = datetime.datetime.strptime(dT1, '%Y-%m-%d %H:%M:%S:%f')
    except Exception as Ex:
        print(f'Failed. Incorrect format. See log for more details.')
        logging.error(f'Failed. {Ex}')
        pass
    else:
        print(f'{dT1} Entered.')
        logging.info(f'Input accepted. {dT1}')
        pass

    #######################
    # Taking user input dT2
    logging.info('Taking user inputs')
    dT2 = input('Enter date time 2020-09-23 1:6:30:123456 = ')
    try:  # Exception Handling block to handle datetime conversion
        dT2 = datetime.datetime.strptime(dT2, '%Y-%m-%d %H:%M:%S:%f')
    except Exception as Ex:
        print(f'Failed. Incorrect format. See log for more details.')
        logging.error(f'Failed. {Ex}')
        pass
    else:
        print(f'{dT2} Entered.')
        logging.info(f'Input accepted. {dT2}')
        print()
        pass

    #######################
    # Calculating time delta
    dT1 = datetime.datetime(year=2011, month=9, day=1, hour=1, minute=27, second=12, microsecond=124)
    dT2 = datetime.datetime(year=2015, month=10, day=14, hour=10, minute=30, second=12, microsecond=12354)

    time_delta = abs(dT1 - dT2)

    logging.debug(f'Calculated time_delta = {time_delta}')

    # Displaying total
    print(f'Total days = {dateTimeConvert("days", time_delta)}')
    print(f'Total hours = {dateTimeConvert("hours", time_delta)}')
    print(f'Total minutes = {dateTimeConvert("minutes", time_delta)}')
    print(f'Total seconds = {dateTimeConvert("seconds", time_delta)}')
    print(f'Total microseconds = {dateTimeConvert("microseconds", time_delta)}')
    logging.debug(f'Called {dateTimeConvert} to do the conversion.')

    # Display in broken down format:
    dT_dict = {'days': 1,
               'hours': 24,
               'minutes': 1440,
               'seconds': 86400,
               'microseconds': 1000000}

    # Calculate each parameters broken down
    logging.debug(f'Calculating separate parameters for {time_delta}')
    day = time_delta.days
    hour = int((dateTimeConvert("hours", time_delta) - (day * dT_dict["hours"])) % dT_dict["hours"])
    minute = int((dateTimeConvert("minutes", time_delta) -
                  (day * dT_dict["minutes"]) - (60 * hour)) % dT_dict["minutes"])
    second = int((dateTimeConvert("seconds", time_delta) -
                  (day * dT_dict["seconds"]) - (3600 * hour ) - (60 * minute)) % dT_dict["seconds"])


    print(f'The difference is {day} days, {hour} hours, {minute} minutes, {second} seconds '
          f'and {time_delta.microseconds} microseconds.')
    # print(time_delta)  # For comparison

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

    dateDiff()

    print()

    logging.info(f'#######################{testNum} Completed.')

###############################################


#######################
if __name__ == '__main__':
    main()
