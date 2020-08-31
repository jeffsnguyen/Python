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

             Extend the program from 7) to display all passed-in keyword arguments, no matter what the key is.
'''

# Return mean value of a variable number of arguments
def name_with_age(**kwargs):
    for item in kwargs.items(): # Lookup each keywords
        print(item) # Print the tuple


def main():
    # Display name, age and state
    name_with_age(name='Robert', age=21, state='CA')

    # Display name, age and state, hairColor
    name_with_age(name = 'Robert', age = 21, state='CA', weight=900, hairColor = 'Black')


#######################
if __name__ == '__main__':
    main()