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

# Return variance of a list
def variance(list):
    mean_list = mean(list) # Calculate mean
    l_temp = [(i - mean_list)**2 for i in list] # Initialize list of (x - mean)**2
    return sum(l_temp) / len(list)

def main():
    l = [1, 2, 3, 8, 9, 10]

    print('Variance = ' + str(variance(l)))

#######################
if __name__ == '__main__':
    main()