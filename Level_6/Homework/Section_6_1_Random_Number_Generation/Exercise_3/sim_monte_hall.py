# Type: Homework
# Level: 6
# Section: 6.1: Random Number Generation
# Exercise: 3
# Description: Contains the code to simulate the Monte Hall problem
#   The following is a famous problem in probability based on a game show. It has generated much
#       controversy due to the non-intuitive nature of the solution. The objective of this exercise is to write
#       a simulation of the game that empirically demonstrates the accepted solution is indeed the correct
#       solution. The game/problem is as follows:
#
#   You are presented with three doors. Behind one of the doors is a brand-new Lamborghini. Behind the
#       other two doors are goats. You do not know which door contains the Lamborghini.
#   The game show host asks you to choose one door; you choose a door. The host then opens one of the
#       two doors that you did not choose and behind that door is a goat. The host then gives you the
#       following options: Either stay with your originally chosen door or switch doors to the remaining,
#       closed door.
#
#   Should you stay, switch, or it makes no difference?
#
#   To solve this problem, do the following:
#       a) Note down your hypothesis (you may have heard the solution to this famous problem
#           already – no problem!).
#       b) Model the game/player using Python OOP. The player should be a class that defines the
#           switch strategy and has functions to choose a door and whether or not to switch. The game
#           class should consist of a player object and the game logic.
#       c) The game class should have a playGame function which does the following:
#           a. Randomly places the prize behind one of three doors.
#           b. Asks its player object to choose a door.
#           c. Figure out which door to ‘open’ (it should be one of the two non-selected doors, but
#               it must not have the prize behind it). Query the player object whether or not to
#               switch to the remaining door (the player object should either always switch or
#               always not switch).
#           d. Check if the final chosen door is a winner or loser and return the Boolean result.
#       d) Play the game one time from main to verify that it works.
#       e) Play the game in a loop of 10,000,000 times from main and store the results of each play in
#           a list. The average of this list should be the approximate probability of winning with your
#           chosen strategy (stay or switch). Time this function (it may take some time).
#       f) Was your hypothesis correct?

#######################
# Importing necessary packages
from utils.timer import Timer
import logging
from montehall.player import Player
from montehall.game import Game
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


###############################################
def main():
    # Hypothesis:
    # H_0 (null): Probability of winning by staying is equal probability of winning by switching.
    # H_a (alternative): Probability of winning by staying is not equal probability of winning by switching.

    # Set logging level
    # Change logging level to info to see the one time game progress.
    logging.getLogger().setLevel(logging.WARNING)

    ###############################################
    # Play game 1 time in main
    logging.info(f'###############################################')
    logging.info(f'Begin Monte Hall game.')

    # Initiate class variables
    player1 = Player()
    game1 = Game(player1)

    # Call playGame() from Game() and get result. See log for details.
    with Timer('Monte_Hall_1_sim') as t:
        result = game1.playGame(False)

    logging.info(f'Did player win? {result}.')
    print(f'Did player win? {result}.')
    print()

    logging.info(f'End game.')

    ###############################################
    numIteration = 10000000
    ###############################################
    # Test 1. Stay Strategy
    # Playing game in a loop
    # Loop set at 10,000,000 iteration
    print('Test 1')
    print('Playing the Monte Hall Game with stay strategy...')

    resultList = []
    with Timer('MonteHall_Stay_10,000,000sims') as t:
        for i in range(numIteration):
            result = game1.playGame(True)  # Play the game
            resultList.append(result)  # Add the result to the list
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print()
    ###############################################

    ###############################################
    # Test 2 Switch Strategy
    # Playing game in a loop
    # Loop set at 10,000,000 iteration
    print('Test 2')
    print('Playing the Monte Hall Game with switch strategy...')
    resultList = []
    with Timer('MonteHall_Switch_10,000,000sims') as t:
        for i in range(numIteration):
            result = game1.playGame(False)  # Play the game
            resultList.append(result)  # Add the result to the list
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print()
    ###############################################

    # Based on the repetition result, reject the null hypothesis: probability of winning by staying is not equal
    # the probability of winning by switching.
    # One should always switch to get a higher chance at winning.
###############################################


#######################
if __name__ == '__main__':
    main()
