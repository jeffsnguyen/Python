'''
Type: Homework
Level: 1
Section: 1.5 Dicts and Sets
Exercise: 2
Description: Create two sets:
             Set 1 should contain the twenty most common male first names in the United States and
             Set 2 should contain the twenty most common male first names in Britain (Google it).

             Perform the following:
                a. Find the first names that appear in both sets.
                b. Find the first names that appear in the United States set, but not Britain.
                c. Find the first names that appear in the Britain set, but not United States.
                d. Use a set comprehension to create a subset of names that have more than five letters.
'''

def main():
    # Set 1 contain the twenty most common male first names in the United States
    name_set_us = set(['James', 'John', 'Robert', 'Michael', 'William',
                      'David', 'Richard', 'Charles', 'Joseph', 'Thomas',
                      'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald',
                      'George', 'Kenneth', 'Steven', 'Edward', 'Brian'])

    # Set 1 contain the twenty most common male first names in the United Kingdom
    name_set_uk = set(['Noah', 'Oliver', 'Leo', 'Archie', 'Alfie',
                      'Logan', 'Oscar', 'George', 'Freddie', 'Charlie',
                      'Harry', 'Arthur', 'Jacob', 'Muhammad', 'Jack',
                      'Thomas', 'Henry', 'James', 'William', 'Joshua'])

    # Find first names that appear in both sets using intersection
    name_usuk = name_set_us.intersection(name_set_uk)
    print('First names that appear in both US and UK:\n', name_usuk)

    # Find the first names that appear in the United States set, but not UK using difference
    name_us_notuk = name_set_us.difference(name_set_uk)
    print('First names that appear in US but not UK:\n', name_us_notuk)

    # Find the first names that appear in the Britain set, but not United States.
    name_uk_notus = name_set_uk.difference(name_set_us)
    print('First names that appear in UK but not US:\n', name_uk_notus)

    # Use a set comprehension to create a subset of names that have more than five letters.
    # Create a set of unique names from US and UK using union
    name_us_plus_uk = name_set_us.union(name_set_uk)
    # Set comprehension to filter only names that have more than five letters
    name_fiveletters = {name for name in name_us_plus_uk if len(name) > 5}
    print('Names that have more than five letters from US and UK:\n', name_fiveletters)

#######################
if __name__ == '__main__':
    main()