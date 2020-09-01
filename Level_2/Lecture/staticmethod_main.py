'''
class lecture
'''

from shapes.point import Point

class StatisticFunctions(object):
    @staticmethod #staticmethod, treat it like a regular function
    def mean(values):
        return sum(values)/len(values)

    @staticmethod
    def mode(values):
        return 1

    @staticmethod
    def median(values):
        return 2

def main():
    print(StatisticFunctions.mean([1, 2, 3]))
    print(StatisticFunctions.mode([1, 2, 3]))


#######################
if __name__ == '__main__':
    main()