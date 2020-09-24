# Type: Homework
# Level: 5
# Section: 5.1 Date/Time
# Exercise: 2
# Description: Contains the tests for various Date/Time operations
#   Modify the above program to request the user enter the date in the following format (for example):
#       2016-09-25 18:23:14:12342
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
    #       ab. Handle datetime input in the format: 2016-09-25 18:23:14:12342
    #       cde. Handle extraction of parameters: year, month, day, hour, minute, second, microseconds.
    #           d. Print out in 2016-09-25 18:23:14:12342
    #           e. Print out in 2016 September 25 06:24:14:12342 PM
    #       f. Do d e with current local time
    #       g. Do d e with current UTC time

    #######################
    # Test ab
    testNum = 'Test ab'
    logging.info(f'{testNum}')
    print('ab. Handle datetime input in the format: 2016-09-25 18:23:14:12342')
    logging.info('ab. Handle datetime input in the format: 2016-09-25 18:23:14:12342')
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
        print(f'{date_time}')
        logging.info(f'Input accepted. {date_time}')
        pass
    print()

    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test cde
    testNum = 'Test cde'
    logging.info(f'{testNum}')
    print('cde. Handle extraction of parameters: year, month, day, hour, minute, second, microseconds.')
    logging.info('cde. Handle extraction of parameters: year, month, day, hour, minute, second, microseconds.')
    # 2020/09/23 1:6:30:123456

    # Parameters extractions
    logging.debug('Start parameter extraction.')

    year = date_time.year
    month = date_time.month
    day = date_time.day
    hour = date_time.hour
    minute = date_time.minute
    second = date_time.second
    microsecond = date_time.microsecond

    # d. Display the entered datetime with the following format: 2016-09-25 18:23:14:12342
    print(date_time.strftime('%y-%m-%d %H:%M:%S:%f'))

    # d. Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM
    print(date_time.strftime('%Y %B %d %I:%M:%S:%f'))

    print()
    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test f
    testNum = 'Test f.de'
    logging.info(f'{testNum}')
    print('f.de. Do d e with current local time')
    logging.info('f.de. Do d e with current local time')
    # 2020/09/23 1:6:30:123456

    # f.d. Display the entered current datetime with the following format: 2016-09-25 18:23:14:12342
    print(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S:%f'))

    # f.ed. Display the entered current datetime with the following format: 2016 September 25 06:24:14:12342 PM
    print(date_time.now().strftime('%Y %B %d %I:%M:%S:%f'))

    print()
    logging.info(f'#######################{testNum} Completed.')
    #######################

    #######################
    # Test g
    testNum = 'Test g.de'
    logging.info(f'{testNum}')
    print('g.de. Do d e with current UTC time')
    logging.info('g.de. Do d e with current UTC time')
    # 2020/09/23 1:6:30:123456

    # f.d. Display the entered current datetime with the following format: 2016-09-25 18:23:14:12342
    print(datetime.datetime.utcnow().strftime('%y-%m-%d %H:%M:%S:%f'))

    # f.ed. Display the entered current datetime with the following format: 2016 September 25 06:24:14:12342 PM
    print(datetime.datetime.utcnow().strftime('%Y %B %d %I:%M:%S:%f'))

    print()
    logging.info(f'#######################{testNum} Completed.')
    #######################

###############################################


#######################
if __name__ == '__main__':
    main()
