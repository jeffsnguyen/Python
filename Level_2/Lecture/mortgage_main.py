# mortgage main

from loan.mortgage import VariableMortgage, FixedMortgage

def main():
    vm = VariableMortgage(100000, {0: .025, 50: .065}, 360)
    type(vm)

#######################
if __name__ == '__main__':
    main()