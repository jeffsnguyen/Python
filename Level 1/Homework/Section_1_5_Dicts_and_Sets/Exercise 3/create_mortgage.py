'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 3
Description: Create a list of unique mortgage amounts.
'''

import random
import pprint

def main():
    # Generate the list  of 100 mortgages from 100000 to 1000000 using random sample to ensure uniqueness
    mortgage = list(random.sample(range(100000, 1000000), 100))
    # Display the list
    print('Mortgage pool:\n')
    pprint.pprint(mortgage)

#######################
if __name__ == '__main__':
    main()