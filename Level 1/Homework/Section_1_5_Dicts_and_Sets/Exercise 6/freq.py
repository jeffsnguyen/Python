'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 6
Description: Create the mode function, building off the frequency function
                that was demonstrated in the lecture.
             The function should return a tuple, containing a list of mode values
                (containing one or more items) and their frequency. Be sure to fully test it.
'''

def mode(list): # Return mode of unique values in the list
    map = {} # Initialize an empty dictionary
    for v in list: # Lookup each value in the list
        if not map.get(v): # If lookup value does not yet exist in the map, add it to map and set it to be 1
            map[v] = 1
        else:
            map[v] += 1 # If value already exist, add 1 to the value of the key

    return map

def main():
    # Initialize list
    l = [2, 3, 5, 4, 5, 7, 8, 4, 4, 3, 2, 4, 4, 5, 7, 8]

    # Display mode of list
    print(mode(l))


#######################
if __name__ == '__main__':
    main()