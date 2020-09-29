# Type: Homework
# Level: 6
# Section: 6.1: Random Number Generation
# Exercise: 3
# Description: Contains the code for Player class of Monte Hall simulation
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
import logging
import random

#######################


###############################################
class Player(object):

    # Initialize Player object
    def __init__(self):
        self._firstPlayerSelect = None
        self._secondPlayerSelect = None
        self._firstHostSelect = None

    # Instance method to select 1st door
    # This is the first selection (cannot stay/do nothing), must pick a number 1,2 or 3
    # Returning a choice
    def firstPlayerSelect(self):
        self._firstPlayerSelect = random.randint(1, 3)
        return self._firstPlayerSelect

    # Instance method to get host first door choice
    def get_firstHostSelect(self, selection):
        self._firstHostSelect = selection
        return self._firstHostSelect

    # Instance method to select second door
    # This is the first selection (cannot stay/do nothing), must pick a number 1,2 or 3
    #   {1: 'choose door 1', 2: 'choose door 2', 3: 'choose door 3'}
    # Returning a choice
    def secondPlayerSelect(self, stay_strat):
        self._secondPlayerSelect = self._firstPlayerSelect if stay_strat else \
            random.choice([i for i in range(1, 4) if i not in (self._firstHostSelect, self._firstPlayerSelect)])
        return self._secondPlayerSelect
