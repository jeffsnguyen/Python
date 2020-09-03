# mortgage main

from loan.mortgage import VariableMortgage, FixedMortgage


def main():
    vm = VariableMortgage(100000, {0:.025, 50:.065}, 360)
    print(type(vm))

    print(vm.rate(0))

    # fm = FixedMortgage(100000, .025, 180)
    # print(fm.rate(0))

#######################
if __name__ == '__main__':
    main()