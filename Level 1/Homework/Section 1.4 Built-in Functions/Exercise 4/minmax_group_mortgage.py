'''
Type: Homework
Level: 1
Section: 1.4: Built-in Functions
Exercise: 4
Description: Find the minimum and maximum mortgage amount owed, for each mortgage sub-list.
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

    # Create a list to house high, low mortgage value for each sub group
    mortgage_hilo_group = []
    mortgage_hilo_group.append([min(miniMortgages), max(miniMortgages)])
    mortgage_hilo_group.append([min(standardMortgages), max(standardMortgages)])
    mortgage_hilo_group.append([min(jumboMortgages), max(jumboMortgages)])

    mortgage_hilo_group = dict(zip(mortgage_group, mortgage_hilo_group)) # Merge name and hi lo value

    # Print results
    # Print generated list
    print('Mortgage list:\n', l)

    # Print sorted list based on range value
    print('Mini Mortgage:\n', miniMortgages)
    print('Standard Mortgage:\n', standardMortgages)
    print('Jumbo Mortgage:\n', jumboMortgages)

    # Print high low value of each sub mortgage group
    print('High low value of each sub mortgage group:\n', mortgage_hilo_group)



#######################
if __name__ == '__main__':
    main()