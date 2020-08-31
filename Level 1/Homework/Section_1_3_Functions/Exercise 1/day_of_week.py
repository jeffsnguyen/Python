'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 1
Description: Write a function that can print out the day of the week for a given number.
             I.e. Sunday is 1, Monday is 2, etc.
             It should return a tuple of the original number and the corresponding name of the day.
'''

import sys

# Look up the day number and return matching tuple of weekday name and the day number
def day_of_week(x):
    # Set up week and day reference list
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday']
    day = [1, 2, 3, 4, 5, 6, 7]

    # Return the tuple of (week, day) in the zip object if day match the lookup variable
    return [(week, day) for week, day in zip(week, day) if day == x]

def main():
    print('This program takes an integer value and return a matching tuple of weekday, day number')

    try: # Exception handling if user enter anything that is not an integer from 1 -> 7
        lookup_day = int(input('Enter an integer from 1 -> 7: '))
        if lookup_day not in range(1,8):
            sys.exit('Must be a integer from 1 -> 7')
    except:
        sys.exit('Must be a integer from 1 -> 7')

    # Display the matching tuple
    print(day_of_week(lookup_day))


#######################
if __name__ == '__main__':
    main()