'''
Type: Homework
Level: 1
Section: 1.3: Functions
Exercise: 4
Description: Create a function that calculates the variance of a passed-in list.
             This function should delegate to the mean function
             (this means that it calls the mean function instead of containing logic
             to calculate the mean itself, since mean is one of the steps to calculating variance).
'''
from mean_passedin_list import mean

# Return variance of a list, with degree of freedom
def variance(list, degOfFreedom = 1):
    mean_list = mean(list) # Calculate mean
    l_temp = [(i - mean_list)**2 for i in list] # Initialize list of (x - mean)**2
    return sum(l_temp) / (len(list) - degOfFreedom)

def main():
    # Initialize a list
    l = [1, 2, 3, 8, 9, 10]

    # Population Variance
    dof = 0
    print('Variance = ' + str(variance(l, dof)))

    # Sample Variance
    dof = 1
    print('Variance = ' + str(variance(l, dof)))

#######################
if __name__ == '__main__':
    main()