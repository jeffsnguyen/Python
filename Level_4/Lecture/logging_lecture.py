# longging lecture

import logging

def main():
    logging.debug('My debug string')   # Put in code instead of string
    logging.info('My debug string')
    logging.warn('My warning string')
    logging.error('My error string')
    logging.critical('My error string')

    try:
        i = 5/0
    except ZeroDivisionError as ex:
        logging.error('Exception here ' + str(ex))
        pass

    # logging level: can be turn on/off based on level

    logging.getLogger().setLevel(logging.INFO)  #  at the lowest level
    logging.info('My debug string')

    logging.getLogger().setLevel(logging.DEBUG)
    logging.debug('My debug string')
#######################
if __name__ == '__main__':
    main()