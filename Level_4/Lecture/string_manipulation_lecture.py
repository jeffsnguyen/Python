# string manipulation lecture


def main():
    s = 'This is my sample string'
    # indexing
    print(s[0])
    print(s[-1])
    print()

    # slicing
    print(s[0:2:3])
    print(s[:3])
    print()

    # upper: create a new string, all uppercase
    print(s.upper())
    print()

    # lower: create a new string, all lowercase
    print(s.lower())
    print()

    # count the letter in the string, case sensitive
    print(s.count('t'))
    print(s.count('is'))
    print(s.count('x')) # if none found, return 0
    print()

    # s.index() return the index of the sub string inside the string, first occurence only
    print(s.index('is'))
    #print(s.index('x'))  # get value error
    print()

    print(s.find('x'))  # similar to index but return -1 if not found

    s = '     This is my spaced string    '
    print(s)
    print(s.strip())   # strip the spaces inside the string
    print()

    s = '     This is my spaced string....'
    print(s)
    print(s.strip('.'))  # strip the specified value from the string

    # Dealing with file path
    f = 'C:\\Users\\username\\desktop\\filename.txt'
    print(f)
    f.split('\\')   # split each directory in the path
    print(f.split('\\'))


    l = f.split('\\')
    print(l)
    print('\\'.join(l))   # join each directory in the list with the \\

    g = f.rsplit('\\', 1)   # split the file name from the rest of the directory
    print(g)
    print()

    # Replace
    print(s)
    print(s.replace(' ', ''))
    print(s.replace('T', 'l'))
    print()

    s = 'My new string'
    print(s.startswith(('My')))    # check starting portion of string
    print(s.startswith(('The')))
    print(s.endswith(('ng')))
    print(s.endswith(('ng1')))


#######################
if __name__ == '__main__':
    main()