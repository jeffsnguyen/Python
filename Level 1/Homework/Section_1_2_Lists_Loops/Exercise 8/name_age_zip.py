'''
Type: Homework
Level: 1
Section: 1.2 Lists/ Loops
Exercise: 8
Description: Create a list of names, and a second list of ages
             which correspond to a name in the first list:

             a. Zip them together and print the result.

             b. Using a list comprehension,
             create a list that contains all the names for which the corresponding age
             is greater than or equals to 18.
             (Hint: Use zip as necessary. Can you also do this without zip? Which is better?).
'''
import pprint

def main():

    # Initialize lists
    names = ['Captain America', 'Winter Soldier', 'Black Widow', 'Iron Man', 'The Hulk', 'Dr. Strange',
                'Spiderman', 'Thor', 'Loki', 'Black Panther', 'Odin']
    ages = [12, 14, 7, 7, 9, 12, 12, 56, 14, 56, 89]

    # Zip names with ages
    names_with_ages = zip(names, ages)
    # Print result as a list
    print('List of names with ages:\n')
    pprint.pprint(list(names_with_ages))
    print()

    #Filter age-over-18 names
    names_18plus = [name for name, age in zip(names, ages) if age >= 18]
    print('List of names over 18:\n')
    print(names_18plus)
    print()

    print('Zip is not necessary. A for loop can be used, however zip is better and cleaner.')

#######################
if __name__ == '__main__':
    main()