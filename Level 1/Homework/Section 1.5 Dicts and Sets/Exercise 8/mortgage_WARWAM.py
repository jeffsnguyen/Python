'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 8
Description: This exercise will build off the mortgage function created in Exercise 1.4.1.

             Modify the dict from 7) to be a dict of address keys and the following tuple as value:
             (amount, rate, term in months).
             Amount should now be between 100,000 and 1,000,000.
             Once you have done this, do the following:

             a. Extract a list of tuple values from the dict, and sort the list by amount (descending).

             b. Create a function that calculates the Weighted Average Rate of the mortgage pool.
             The input parameter should be a list of mortgage tuples (amount,rate,term).
             Print the rate percentage, rounded to the nearest hundredths.

             c. Create a function that calculates the Weighted Average Maturity (term) of the mortgage pool.
             The input parameter should be a list of mortgage tuples (amount,rate,term).

             d. Create a new dict (by processing the original dict) with Term
             as the key and a list of (amount, rate) tuples for each Term key.
'''
import random
import pprint

# Return a dict of entries in the form address:(amount, rate, terms in months)
def create_dict_mortgage():
    # Initialize dict of mortgage address, for simplicity purpose this is hardcoded
    mortgage_dict = {'T57QN1': (523000,.030,360), 'HBB56R': (700000,.025,302), 'PDFI4X': (388000,.050,240),
                     'HWOYO7': (270000,.030,200), 'ZODTXB': (288000,.020,260), '5ZUZWN': (916000,.030,318),
                     'OKW3N7': (932000,.045,350), 'QPGUF5': (356000,.040,312), 'NUTSPN': (571000,.015,355),
                     'V44QSJ': (831000,.010,123), 'P4P97U': (204000,.035,341), '6E8LVM': (131000,.025,272),
                     'LHKCD1': (765000,.020,201), 'X29TBZ': (979000,.350,207), 'ODPVS0': (865000,.070,364),
                     'M1J839': (191000,.015,205), 'VW9MBM': (357000,.030,187), 'C11Z2V': (731000,.060,129)}
    return mortgage_dict

# Return the Weighted Average Rate of the mortgage pool
def WAR_mortgage(pool):
    # Calculate the sum amount of the pool
    # Use list comprehension to access the amount value
    sum_amount = sum(i[0] for i in pool)

    # Loop to calculate weighted rate of each mortgage and add them together
    WAR_rate = 0 # Initialize WAR rate to be 0
    for i in pool:
        WAR_rate += i[0]*i[1]/sum_amount

    return WAR_rate

# Return the Weighted Average Maturity of the mortgage pool
def WAM_mortgage(pool):
    # Calculate the sum amount of the pool
    # Use list comprehension to access the amount value
    sum_amount = sum(i[0] for i in pool)

    # Loop to calculate weighted rate of each mortgage and add them together
    WAM_rate = 0 # Initialize WAR rate to be 0
    for i in pool:
        WAM_rate += i[0]*i[2]/sum_amount

    return WAM_rate

# Main
def main():
    mortgage_ledger = create_dict_mortgage()  # Initalize mortgage dictionary
    print('Mortgage original ledger:\n')
    pprint.pprint(mortgage_ledger)

    # Extract list of values from the dict and sorted by descending amount
    mortgage_val_list = list(mortgage_ledger.values()) # Extract list
    mortgage_val_list.sort(key = lambda x:x[0], reverse = True) # Sort by amount, descending
    pprint.pprint(mortgage_val_list)

    # Call function WAR_mortgage to calculate Weighted Average Rate
    WAR_rate = WAR_mortgage(mortgage_val_list)
    print(f'The Weighted Average Rate of mortgages in the pool is {100*WAR_rate:.2f}%.')

    # Call function WAM_mortgage to calculate Weighted Average Maturity
    WAM_rate = WAM_mortgage(mortgage_val_list)
    print(f'The Weighted Average Maturity of mortgages in the pool is {WAM_rate:.2f} months.')

    # Create a new dict with the form:
    # term: (amount, rate)
    # Comment: This exercise is particularly strange because python dict key are unique??
    # So it was not possible to have similar term mortgage. I had to change the original dict
    term_mortgage_dict = {i[2]: (i[0],i[1]) for j,i in mortgage_ledger.items()} # Dict comprehension
    print('New dict with term as key and (amount, rate) as values:')
    pprint.pprint(term_mortgage_dict)
'''
    # Dict comprehension to filter

    # Mini mortgages have value <200
    miniMortgages = {address: value for (address, value) in mortgage_ledger.items() if value < 200}
    print('Mini mortgages (0,200):')
    pprint.pprint(miniMortgages)

    # Standard mortgages have value between 200 and 467
    standardMortgages = {address: value for (address, value) in mortgage_ledger.items()
                         if ((value >= 200) and(value <= 467))}
    print('Standard mortgages [200,467]:')
    pprint.pprint(standardMortgages)

    # Jumbo mortgages have value >467
    jumboMortgages = {address: value for (address, value) in mortgage_ledger.items() if value > 467}
    print('Jumbo mortgages (467,1000]:')
    pprint.pprint(jumboMortgages)

    # Modify one key value in the jumboMortgages dict and check against the original's
    jumboMortgages['X29TBZ'] = 100
    print('The value of mortgage X29TBZ in jumboMortgage is: ', jumboMortgages['X29TBZ'])
    print('The value of mortgage X29TBZ in original ledger is: ', mortgage_ledger['X29TBZ'])
    print('Modifying the sub-dictionaries value does not modify the value in the original dictionary'
          'because they are different dictionaries')

    # c. Extract the lists of amounts from each separate dict.
    # Modify one value in the miniMortgages list.
    # Does the miniMortgages dict change? How about the original dict? Why?
    # Extract values from each sub dicts

    miniMortgages_val = list(miniMortgages.values())
    print('List of mini mortgage values without address:\n', miniMortgages_val)

    standardMortgages_val = list(standardMortgages.values())
    print('List of standard mortgage values without address:\n', standardMortgages_val)

    jumboMortgages_val = list(jumboMortgages.values())
    print('List of mini mortgage values without address:\n', jumboMortgages_val)

    # Modify 1 value in the mini mortgages list:
    miniMortgages_val[0] -= 1
    print('Subtract 1 from the 6E8LVM address of miniMortgages list. Value is now: ',miniMortgages_val[0])
    print('Double check the miniMortgage dictionary value of 6E8LVM: ', miniMortgages['6E8LVM'])
    print('Double check the original dictionary value of 6E8LVM: ', mortgage_ledger['6E8LVM'])
    print('Changes in the pulled list has no effect on both the subdict and the original dict'
          'because they are separated objects.')

'''
#######################
if __name__ == '__main__':
    main()