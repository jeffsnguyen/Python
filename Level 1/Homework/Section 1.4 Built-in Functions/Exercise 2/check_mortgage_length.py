'''
Type: Homework
Level: 1
Section: 1.4: Built-in Functions
Exercise: 2
Description: Find the length of each list in part b of the previous exercise.
             Then, verify that the lengths of all three lists indeed add up to the length of the full list in part a.
'''

import random
from mortgage import create_mortgage

def main():
    l = create_mortgage() # Create mortgage list

    # List comprehension to filter
    miniMortgages = [i for i in l if i < 200]
    standardMortgages = [i for i in l if (i >= 200) and (i <= 467)]
    jumboMortgages = [i for i in l if i > 467]

    # Create mortgage check list
    mortgage_group = ["miniMortgages", "standardMortgages", "jumboMortgages"] # Create list contain mortgage group

    # Count entry of each sorted list
    mortgage_group_count = []
    l1 = len(miniMortgages)
    mortgage_group_count.append(len(miniMortgages))
    l2 = len(standardMortgages)
    mortgage_group_count.append(len(standardMortgages))
    l3 = len(jumboMortgages)
    mortgage_group_count.append(len(jumboMortgages))

    mortgage_group_count = dict(zip(mortgage_group, mortgage_group_count)) # Merge name and count value of each group

    # Print results
    # Print generated list
    print('Mortgage list:\n', l)

    # Print sorted list based on range value
    print('Mini Mortgage:\n', miniMortgages)
    print('Standard Mortgage:\n', standardMortgages)
    print('Jumbo Mortgage:\n', jumboMortgages)

    # Display count of each group and whether the total match the original list
    print('Count of mortgages within each group:\n', mortgage_group_count)

    if sum([l1,l2,l3]) == len(l):
        print('The total mortgage of each list add up to the original? (True/False) ',sum([l1,l2,l3]) == len(l))


#######################
if __name__ == '__main__':
    main()