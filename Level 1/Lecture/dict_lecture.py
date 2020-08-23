'''
dict  lecture
'''

def freqMap(values): #map of frequencies of values in the list
    map = {}
    for v in values: #for each value in the map
        if not map.get(v): #if value does not yet exist in the map, add it to map and set it to be 1
            map[v] = 1
        else:
            map[v] += 1 #if value already exist, add 1 to the counter

    return map

def main():
    #Code goes here
    print(freqMap([2,3,5,4,5,7,8,4,4,3,2,4,4,5,7,8]))


#######################
if __name__ == '__main__':
    main()