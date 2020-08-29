'''
Type: Homework
Level: 1
Section: 1.4: Built-in Functions
Exercise: 5
Description: Create any code that demonstrates usage of the abs function.
'''

import sys

def main():
    try: # If input is invalid, exit with an error message
        num = float(input('Enter a valid real number: ')) # Take input and convert
        print('The absolute value of ' + str(num) + ' is ' + str(abs(num))) # Display result
    except:
        sys.exit('Must be a valid real number.')

#######################
if __name__ == '__main__':
    main()