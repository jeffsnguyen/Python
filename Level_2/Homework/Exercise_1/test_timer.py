# Type: Homework
# Level: 1
# Section: 2.1: Classes
# Exercise: 1
# Description: This contains the test function for the class Timer
#   We’ve been using time.time before and after code blocks to report the difference as the ‘time taken’.
#   This exercise is to generalize and encapsulate this into a class, to make things cleaner and reusable.
#   The steps are as follows:
#       a. Create a class called Timer.
#       b. Add a start method and end method. They should work as follows:
#               t = Timer()
#               t.start()
#               # Lots of code here
#               t.end() # This should stop the timer and print the time taken
#       c. Note that start should give an error if the Timer is already started and end should give an error
#           if the Timer is not currently running.
#       d. Add a method to retrieve the last timer result.
#       e. Add the ability to configure the Timer to display either seconds, minutes, or hours.
#           The timer result (i.e. from end and retrieveLastResult) should use whatever the current configuration is.
#       f. Test your class thoroughly.
#   This is obviously cleaner than the previous approach of subtracting times everywhere.
#   The remaining downside to this class is that one must still explicitly invoke t.start() and t.end()
#   around the code one wishes to time. We will remedy this when we extend this class using
#   context managers and decorators (see Levels 3 and 5) to make things even cleaner syntactically.

# Importing necessary packages
from utils.timer import Timer


#######################
# Create a testing function to run a meaningless loop to take up some time
# so that the Timer class can be tested
def testing_loop(x):
    print('Running a meaningless count from 1 to ' + str(x) + ' to test the Timer class...')

    # Run the meaningless loop to test
    count = 0
    for i in range(1, x):
        count += i

    # Signal completion of loop
    print('Loop completed.')


#######################


def main():
    # Initialize t with Timer class
    t = Timer(12, 45, 476)

    # Testing block
    ###############################################
    # Scenario: This test tests the basic base case scenario of timing a loop running 10,000,000
    #   and increment a number by 1 each time.
    # Desired Result: Timer will be displayed in seconds, i.e. timer_config = 1
    # Note: In this test, it is not possible to change the timer config.
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - Start ####
    testing_loop(10000000)
    #### Your test function goes here -  ####
    t.end()  # Stop counter and print result
    ###############################################

    # Testing block
    ###############################################
    # Scenario: This test tests the timing of a loop running 20,000,000 times and increment a number by 1 each time.
    # Desired Result: Timer will be displayed in seconds, i.e. timer_config = 1
    # Note: In this test, user can change the timer config.
    t.timerConfig(60)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - Start ####
    testing_loop(20000000)
    #### Your test function goes here -  ####
    t.end()  # Stop counter and print result
    ###############################################

    # Testing block
    ###############################################
    # Scenario: This test test an exception when the timer configuration is not set in neither hours (3600),
    #   minutes(60) or seconds(1). User is able to configure display time in this test. The testing task is
    #   timing a loop running 30,000,000 times and increment a number by 1 each time.
    # Desired Result:
    #   1. Display a warning message to user that said timer configuration is not implemented and result
    #       will be calculated using default time config, which 1.
    #   2. Timer will be displayed in default time config, which is = 1.
    t.timerConfig(360)  # Set timer display configuration
    t.start()  # Start the counter
    # Run the testing loop to test Timer functionalities
    # Alternative, paste in your own code to test your own function
    #### Your test function goes here - START ####
    testing_loop(30000000)
    #### Your test function goes here - END ####
    t.end()  # Stop counter and print result
    ###############################################

    # Testing block
    ###############################################
    # Scenario: This test demonstrates the functionality that enables user to change time config and retrieve
    #   the last timer result
    # Desired Result:
    #   1. User can call timerConfig with different argument value to set the time config. The only available value
    #       is: hours (3600), minutes(60) or seconds(1). If the timer config value is not in this selection,
    #       display a warning message and display the result by default in seconds.
    #   2. Display the last timer result.
    #### Your test function goes here - START ####
    t.timerConfig(3600)  # Set timer display configuration
    t.retrieveLastResult()  # Retrieve and print last timer result
    #### Your test function goes here - END ####
    ###############################################


#######################
if __name__ == '__main__':
    main()
