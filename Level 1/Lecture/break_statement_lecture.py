'''
looping + breakstatement
'''

def main():
    print('Mortgage calculator\n')

    while(True):
        prin = float(input('\nEnter mortgage face value (0 to exit): '))
        if prin == 0:
            break
        rate = float(input('\nEnter mortgage rate: '))
        term = float(input('\nEnter mortgage term(months): '))

        mRate = rate/12.0

        monthlyPayment = (mRate*prin)/(1-(1+mRate)**(-term))

        print(monthlyPayment)

        print('Program Complete')

#######################
if __name__ == '__main__':
    main()