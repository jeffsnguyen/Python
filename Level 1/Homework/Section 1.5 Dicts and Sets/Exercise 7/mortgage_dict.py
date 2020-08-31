'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 7
Description: This exercise will build off the mortgage function created in Exercise 1.4.1.

             Extend the mortgage function to return a dict of address:mortgage.
             For simplicity, address should be a unique six-character string.
             For example {‘867E23’ : 120}.
             Once you have done this, modify the filtering code from 1.4.1 to do the following:

             a. Provide three separate dicts, filtered the same way as problem 1).

             b. Modify one value in the jumboMortgages dict.
             Check the original dict; did it remain intact or change? Why?

             c. Extract the lists of amounts from each separate dict.
             Modify one value in the miniMortgages list.
             Does the miniMortgages dict change? How about the original dict? Why?
'''
import random
import pprint

# Return a dict of assorted mortgage amount (in thousands) from 100, 1000
# in the form address::mortgage
def create_dict_mortgage():
    # Initialize dict of mortgage address, for simplicity purpose this is hardcoded
    mortgage_dict = {'T57QN1': 523, 'HBB56R': 700, 'PDFI4X': 388, 'HWOYO7': 270, 'ZODTXB': 288,
                     '5ZUZWN': 916, 'OKW3N7': 932, 'QPGUF5': 356, 'NUTSPN': 571, 'V44QSJ': 831,
                     'P4P97U': 204, '6E8LVM': 131, 'LHKCD1': 765, 'X29TBZ': 979, 'ODPVS0': 865,
                     'M1J839': 191, 'VW9MBM': 357, 'C11Z2V': 731, '9081AR': 305, '9CZZML': 419,
                     'VH9006': 900, 'TC8KL7': 999, 'GGFQ09': 787, 'W118BK': 727, 'IDM3MQ': 657,
                     '3UC7G8': 130, 'B0EM69': 567, 'S4P6BI': 240, '1JJ8K1': 240, 'JTEV0H': 751}

    return mortgage_dict

def main():
    mortgage_ledger = create_dict_mortgage()  # Initalize mortgage dictionary
    print('Mortgage original ledger:\n')
    pprint.pprint(mortgage_ledger)

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


#######################
if __name__ == '__main__':
    main()