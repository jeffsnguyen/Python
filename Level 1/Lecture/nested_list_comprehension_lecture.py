'''
nested list comprehension lecture
'''

import time

def main():
    #Demo a nested list comprehension
    nestedList = [[1,2,3,4,5], [3,4,5], [7,5,3,7], [6,4,3,7]] #original list
    flattenedList = [item for sublist in nestedList for item in sublist] #for each sublist and each item in the sublist
    print(flattenedList)

    loopFlattenedList = []
    for sublist in nestedList:
        for item in sublist:
            loopFlattenedList.append(item)

    print(loopFlattenedList)

#######################
if __name__ == '__main__':
    main()