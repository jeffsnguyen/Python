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
from time import time
import logging
from montehall.player import Player
from montehall.game import Game
import random
#######################
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
###############################################
# Add config of log
logging.basicConfig(filename='log.txt', filemode='a', datefmt='%Y-%m-%d %H:%M:%S',
                    format="{asctime} {levelname} {processName:<12} {message} ({filename}:{lineno})", style='{')
###############################################


# Play the Monte Hall game
def playGame(stayStrat):
    player = Player()
    game = Game(player)
    # Start Game
    # Player Turn 1
    player_firstChoice = player.firstPlayerSelect()  # Player select first door to open
    game.get_firstPlayerSelect(player_firstChoice)  # Host save player selection

    # Host Turn
    host_choice = game.open_firstHostSelect()  # Host select first door to open
    player.get_firstHostSelect(host_choice)  # Player save host's selection

    # Player Turn 2 (final)
    # stayStrat is a given boolean parameter
    finalChoice = player.secondPlayerSelect(stayStrat)  # Player select second door to open
    game.get_secondPlayerSelect(finalChoice)  # Host save player selection

    return game.checkResult(finalChoice)


###############################################
def main():
    # Hypothesis:
    # H_0 (null): Probability of winning by staying is equal probability of winning by switching.
    # H_a (alternative): Probability of winning by staying is not equal probability of winning by switching.

    # Set logging level
    logging.getLogger().setLevel(logging.DEBUG)

    ###############################################
    # Play game 1 time in main
    print(f'Demo Monte Hall.')
    random.seed()
    player1 = Player()
    game1 = Game(player1)
    print(f'Here is the preset doors: {game1.getDict()}')
    print(f'Here is the preset wining door choice: {game1.get_prizeLoc()}.')
    print(f'Starting game...')
    player_firstChoice = player1.firstPlayerSelect()
    print(f'Player selected {player_firstChoice} as first door to open.')

    # Host class registering player's choice
    print(f'Host acknowledged Player choice of {game1.get_firstPlayerSelect(player_firstChoice)} '
          f'as first door to open.')
    host_choice = game1.open_firstHostSelect()
    print(f'Host opened door {host_choice}.')

    # Player class registering host's choice
    print(f'Player acknowledge host choice of {player1.get_firstHostSelect(host_choice)} '
          f'as first door to open.')

    finalChoice = player1.secondPlayerSelect(True)  # Save the player's final choice

    if finalChoice == player_firstChoice:
        print(f'Player chose to stay at door {finalChoice}.')
        # Host class registering player's choice
        print(f'Host acknowledge player wants to stay at door {game1.get_secondPlayerSelect(finalChoice)}.')
    else:
        print(f'Player chose to open door: {finalChoice}.')
        # Host class registering player's choice
        print(f'Host acknowledge player wants to open door {game1.get_secondPlayerSelect(finalChoice)}.')

    print(f'Did player win? {game1.checkResult(finalChoice)}')
    print(f'End of game.')
    print()
    ###############################################

    ###############################################
    # Test 1. Stay Strategy
    # Playing game in a loop
    # Loop set at 10,000,000 iteration
    print('Test 1')
    print('Playing the Monte Hall Game with stay strategy.')
    numIteration = 10000000
    resultList = []
    startTime = time()
    for i in range(numIteration):
        result = playGame(True)  # Play the game
        resultList.append(result)  # Add the result to the list
    endTime = time()
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print(f'Took {endTime - startTime} seconds to run.')
    print()
    ###############################################

    ###############################################
    # Test 2 Switch Strategy
    # Playing game in a loop
    # Loop set at 10,000,000 iteration
    print('Test 2')
    print('Playing the Monte Hall Game with switch strategy.')
    numIteration = 10000000
    resultList = []
    startTime = time()
    for i in range(numIteration):
        result = playGame(False)  # Play the game
        resultList.append(result)  # Add the result to the list
    endTime = time()
    print(f'The probability of this strategy is {sum(resultList) / len(resultList)}')
    print(f'Took {endTime - startTime} seconds to run.')
    print()
    ###############################################

    # Based on the repetition result, reject the null hypothesis: probability of winning by staying is not equal
    # the probability of winning by switching.
    # One should always switch to get a higher chance at winning.
###############################################


#######################
if __name__ == '__main__':
    main()
