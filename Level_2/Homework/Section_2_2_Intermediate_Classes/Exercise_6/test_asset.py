# Type: Homework
# Level: 2
# Section: 2.2: Intermediate
# Exercise: 6
# Description: This contains the Asset class and its methods
#   This exercise focuses on creating the individual Asset derived classes. Do the following:
#       a. Modify the annualDeprRate method of the Asset class to trigger a not-implemented error.
#           This ensures that no one can directly instantiate an Asset object (makes it abstract).
#       b. Create a Car class, derived from Asset. Derive multiple car types from Car (i.e. Civic, Lexus,
#           Lamborghini, etc.). Give each one a different depreciation rate.
#       c. Create a HouseBase class, derived from Asset. Derive PrimaryHome and VacationHome
#           from House. Give each one a different depreciation rate (note, a vacation home will
#           depreciate slower than a primary home since it is often vacant).

# Importing necessary packages
from asset.asset import Asset, Car, HouseBase, Lambourghini, Lexus, Civic, PrimaryHome, VacationHome
#######################


def main():
    # Testing block
    # Scenario:
    #   This block will:
    #       1. Test the Asset.annualDeprRate(period) method to print the annual depreciation rate.
    #       2. Test the Car.annualDeprRate(period) method to print the annual depreciation rate.
    #       3. Test the Lambourghini.annualDeprRate(period) method to print the annual depreciation rate.
    #       4. Test the Lexus.annualDeprRate(period) method to print the annual depreciation rate.
    #       5. Test the Civic.annualDeprRate(period) method to print the annual depreciation rate.
    #       6. Test the HouseBase.annualDeprRate(period) method to print the annual depreciation rate.
    #       7. Test the PrimaryHome.annualDeprRate(period) method to print the annual depreciation rate.
    #       8. Test the VacationHome.annualDeprRate(period) method to print the annual depreciation rate.
    ###############################################
    # Test 1.1
    # Scenario: Test the Asset.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.1')
    asset1 = Asset(1000000)
    # Uncomment to run
    #print('The asset annual depreciation rate is:', asset1.annualDeprRate(12))
    print()

    # Test 1.2
    # Scenario: Test the Car.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.2')
    car1 = Car(1000000)
    print('The car annual depreciation rate is:', car1.annualDeprRate(12))
    print()

    # Test 1.3
    # Scenario: Test the Lambourghini.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.3')
    lambo1 = Lambourghini(1000000)
    print('The car annual depreciation rate is:', lambo1.annualDeprRate(12))
    print()

    # Test 1.4
    # Scenario: Test the Lexus.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.4')
    lexus1 = Lexus(1000000)
    print('The car annual depreciation rate is:', lexus1.annualDeprRate(12))
    print()

    # Test 1.5
    # Scenario: Test the Civic.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.5')
    civic1 = Civic(1000000)
    print('The car annual depreciation rate is:', civic1.annualDeprRate(12))
    print()

    # Test 1.6
    # Scenario: Test the HouseBase.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.6')
    house1 = HouseBase(1000000)
    print('The house annual depreciation rate is:', house1.annualDeprRate(12))
    print()

    # Test 1.7
    # Scenario: Test the PrimaryHome.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.7')
    primaryhouse1 = PrimaryHome(1000000)
    print('The house annual depreciation rate is:', primaryhouse1.annualDeprRate(12))
    print()

    # Test 1.8
    # Scenario: Test the PrimaryHome.annualDeprRate(period) method to print the annual depreciation rate.
    print('Test 1.8')
    vacayhouse1 = VacationHome(1000000)
    print('The house annual depreciation rate is:', vacayhouse1.annualDeprRate(12))
    print()
    ###############################################


#######################
if __name__ == '__main__':
    main()
