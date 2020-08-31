'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 1
Description: Port Exercise 1.2.8 to use sets instead of lists. What’s the benefit?
'''

def main():
    # Creating set of names and ages to store values
    names = set(['Captain America', 'Winter Soldier', 'Black Widow', 'Iron Man', 'The Hulk', 'Dr. Strange',
                'Spiderman', 'Thor', 'Loki', 'Black Panther', 'Odin'])
    ages = set([12, 14, 7, 17, 9, 121, 212, 556, 144, 56, 89]) # Note that set only accept unique values

    # Zip the above sets together
    names_with_ages = set(zip(names, ages)) # Zip operation on set
    print('Set of names and ages \n',names_with_ages) # Display results

    # Filter ages over 18
    names_18plus = {name for name, age in names_with_ages if age >= 18} # Set comprehension
    print('Set of names with ages 18 or more \n',names_18plus) # Display results

    # Print text answer to the question
    print('The benefits Set is better in this case as name and age are mostly unique so storing data using sets '
          'is much more efficient')

#######################
if __name__ == '__main__':
    main()