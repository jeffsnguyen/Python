# Type: Homework
# Level: 3
# Section: 3.2: Generators 101
# Exercise: 9
# Description: Create a list of ten names. Loop through the list and output each name in the following format:
#               Name 1: Henry
#               Name 2: Jake

#######################
# Importing necessary packages

#######################

###############################################
# Generate to lazy evaluate adding index to list of name
def nameloop(names):
    nameloop = ['Name ' + str(names.index(name) + 1) + ': ' + str(name) for name in names]
    for name in nameloop:
        yield name

###############################################
def main():

    # Testing block 1
    # Scenario:
    #   This block will:
    #       1. Test Test name list iteration

    ###############################################

    # Test 1
    # 1. Test name list iteration
    print('Test 1: Test name list iteration')

    # Generate name list
    names = ['Kawhi', 'PG13%', 'MontrezL', 'Chihuahua Bev', 'Lose Williams',
            'Dirty Morris', 'Jungle Noah', 'Zubac', 'WhoDis 9', 'WhoDis 10']

    # Iterate through the list and print out entries
    print_name = nameloop(names)
    while True:
        print(next(print_name))

###############################################

#######################
if __name__ == '__main__':
    main()