'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 7
Description: Create two lists: The first list should be called ‘players’,
             and contain at least ten unique names.
             The second list should be called ‘injured_players’,
             and contain a few names of players from the first list.

             Create a list comprehension which results in a list
             containing all active (non-injured) players.
'''

def main():

    # Initialize lists
    players = ['Captain America', 'Winter Soldier', 'Black Widow', 'Iron Man', 'The Hulk', 'Dr. Strange',
                'Spiderman', 'Thor', 'Loki', 'Black Panther', 'Odin']
    injured_players = ['Winter Soldier', 'Thor', 'Iron Man']

    # Filter active players, i.e. non-injured players
    active_players = [item for item in players if item not in injured_players]


#######################
if __name__ == '__main__':
    main()