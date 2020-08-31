'''
Type: Homework
Level: 1
Section: 1.4: Built-in Functions
Exercise: 3
Description: Sum the full list of mortgages, to obtain the total amount owed to your firm.
'''

import random
from mortgage import create_mortgage

def main():
    l = create_mortgage() # Create mortgage list

    # Print results
    # Print generated list
    print('Mortgage list:\n', l)

    # Calculate sum of the mortgage
    print('Total amount owed to the firm = ', sum(l))




#######################
if __name__ == '__main__':
    main()