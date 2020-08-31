'''
Type: Homework
Level: 1
Section: 1.4: Built-in Functions
Exercise: 1
Description: You are a lender, holding onto a large number of mortgages. Create code that does the following:
                a. A function that returns an unsorted list of mortgage amounts, in thousands.
                    Numbers should range from 100 to 1,000 and do not need to all be unique.
                b. Filter the result of a) into three lists: Amounts below 200, amounts between 200 and 467,
                    and amounts greater than 467. Call these ‘miniMortgages’, ‘standardMortgages’,
                    and ‘jumboMortgages’ respectively.
                c. Use the all function with an if statement to verify that the resulting lists of
                    b) indeed contain only numbers within the specified ranges.
                d. Use the any function with an if statement to verify that the resulting lists of
                    b) indeed contain only numbers within the specified ranges.
'''

import random

# Return a list of assorted mortgage amount (in thousands) from 100, 1000
def create_mortgage():
    mortgage_list = [] # Initialize empty list
    for i in range(0,30): # Limit list entries at 30
        mortgage_list.append(random.randint(100, 1001)) # Add random int number in the range to the list
    return mortgage_list

# Check if all entry of list is within given range
def check_range_mortgage_all(list,min,max):
    return all((x >= min) and (x <= max) for x in list)

# Check if any entry of list is within given range
def check_range_mortgage_any(list,min,max):
    return all((x >= min) and (x <= max) for x in list)


def main():
    l = create_mortgage() # Create mortgage list

    # List comprehension to filter
    miniMortgages = [i for i in l if i < 200]
    standardMortgages = [i for i in l if (i >= 200) and (i <= 467)]
    jumboMortgages = [i for i in l if i > 467]

    # Create mortgage check list
    mortgage_group = ["miniMortgages", "standardMortgages", "jumboMortgages"] # Create list contain mortgage group

    # List to check if all value is within range
    mortgage_check_all = []
    mortgage_check_all.append(check_range_mortgage_all(miniMortgages, 0, 199))
    mortgage_check_all.append(check_range_mortgage_all(standardMortgages, 200, 467))
    mortgage_check_all.append(check_range_mortgage_all(jumboMortgages, 468, 1000))
    mortgage_range_all = list(zip(mortgage_group, mortgage_check_all))

    # List to check if any value is within range
    mortgage_check_any = []
    mortgage_check_any.append(check_range_mortgage_any(miniMortgages, 0, 199))
    mortgage_check_any.append(check_range_mortgage_any(standardMortgages, 200, 467))
    mortgage_check_any.append(check_range_mortgage_any(jumboMortgages, 468, 1000))
    mortgage_range_any = list(zip(mortgage_group, mortgage_check_any))

    # Print results
    # Print generated list
    print('Mortgage list:\n', l)

    # Print sorted list based on range value
    print('Mini Mortgage:\n', miniMortgages)
    print('Standard Mortgage:\n', standardMortgages)
    print('Jumbo Mortgage:\n', jumboMortgages)

    # Print check result based on range
    print('If ALL value in group is correct:\n', mortgage_range_all)
    print('If ANY value in group is correct:\n', mortgage_range_any)



#######################
if __name__ == '__main__':
    main()