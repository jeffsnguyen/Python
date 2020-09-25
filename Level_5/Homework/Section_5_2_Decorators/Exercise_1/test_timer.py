# Type: Homework
# Level: 5
# Section: 5.2: Decorators
# Exercise: 1
# Description: This contains tests for Timer classes
#   Modify the Timer class to work as a decorator (feel free to use the provided sample code). Its
#       usage should look like this:
#       @Timer
#       def myFunc(arg1, arg2):
#           print('Do Work Here')
#   An example output would look like: <function myFunc at 0x34173DF0>: 1.5467 seconds
#
#   How does this compare to the previous approach to using the context manager? When is this
#       more useful and when are context managers more useful?

# Importing necessary packages
import logging
from utils.timer import Timer
from time import time, sleep
#######################
# To enable PyCharm to create log file
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Setting log file config
logging.basicConfig(filename='log.txt', filemode='a',
                    format="{levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
#######################


@Timer  # decorating the function with the Timer function
def intenseFunction(input):
    sleep(input)  # cause program to wait and do nothing for 5 seconds
    return 'Done'

def main():

    logging.getLogger().setLevel(logging.DEBUG)  # Set logging level
    ###############################################

    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the modified Timer class as a decorator

    #######################
    # Test 1
    testNum = 'Test 1'
    logging.info(f'{testNum}')
    print('1. Test the modified Timer class as a decorator')
    logging.info('1. Test the modified Timer class as a decorator')

    print(intenseFunction(5))

    ## Decorator in this Timer case syntactically provide cleaner code than context manager.
    ## Decorators are useful if you need to augment the function/ class when it's defined.
    ## Context manager is useful for cleanup because it enables clean up after the function while the decorator
    ## doesn't do any clean up at all.
    ## The two, otherwise, are generally unrelated concepts.

    logging.info(f'#######################{testNum} Completed.')
    #######################



    ###############################################


#######################
if __name__ == '__main__':
    main()
