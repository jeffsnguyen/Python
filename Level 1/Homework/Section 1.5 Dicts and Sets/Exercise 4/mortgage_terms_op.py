'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 4
Description: Create a set of mortgage terms, in years (10, 15, 30):
                a. Add a 5-year term to the set.
                b. Remove the 15-year term from the set.
                c. Remove a 45-year term from the set. What happens? How can you prevent that?
'''

import sys

def main():
    # Create mortgage term set
    mortgage_terms = set([10, 15, 30])
    print('Mortgage terms: \n', mortgage_terms)

    # Add 5-year term to the set
    mortgage_terms.add(5)
    print('Mortgage terms (add 5): \n', mortgage_terms)

    # Remove the 15-year term from the set.
    mortgage_terms.remove(15)
    print('Mortgage terms (remove 15): \n', mortgage_terms)

    # Remove the 45-year term from the set.
    try:
        mortgage_terms.remove(45)
        print('Mortgage terms (remove 15): \n', mortgage_terms)
    except:
        sys.exit('There is no 45-year term to be removed. The code will throw an error,'
                 'to prevent this in the future, use discard instead of remove.')

#######################
if __name__ == '__main__':
    main()