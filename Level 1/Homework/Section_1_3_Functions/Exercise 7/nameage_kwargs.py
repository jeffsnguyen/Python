'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 6
Description: Write a function that takes name, age as parameters. It should also take **kwargs.
             The function should display the name, age, and any of ‘state’, ‘height’, and ‘weight’
                that happen to exist in the kwargs.
             Call the function with names, ages, and different combinations of keyword arguments
                (state, height, weight, hairColor, etc.).
'''

# Return mean value of a variable number of arguments
def name_with_age(name, age, **kwargs):
    print(name, age) # print name & age
    print(kwargs.get('state'))  # get the value for the key 'state'
    print(kwargs.get('height')) # get the value for the key 'height'
    print(kwargs.get('weight')) # get the value for the key 'weight'


def main():
    # Display name, age and state
    name_with_age('Jake', 12, state = 'CA')

    # Display name, age and state
    name_with_age('Robert', 21, state='CA', weight = 900)

    # Display name, age and state, hairColor
    name_with_age('Robert', 21, state='CA', weight=900, hairColor = 'Black')


#######################
if __name__ == '__main__':
    main()