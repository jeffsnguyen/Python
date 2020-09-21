# Type: Homework
# Level: 4
# Section: 4.1 Python Strings
# Exercise: 1
# Description: Contains the tests for various strings operations
#   Use the following string for each of the below exercises:
#       “ The Python course is the best course that I have ever taken. “
# a. Display the length of the string.
# b. Find the index of the first ‘o’ in the string.
# c. Trim off the leading spaces only.
# d. Trim off the trailing spaces only.
# e. Trim off both the leading and trailing spaces (use this trimmed string for all the remaining parts below).
# f. Fully capitalize the string.
# g. Fully lowercase the string.
# h. Display the number of occurrence of the letter ‘d’ and of the word ‘the’.
# i. Display the first 15 characters of the string.
# j. Display the last 10 characters of the string.
# k. Display characters 5-23 of the string.
# l. Find the index of the first occurrence of the word ‘course’.
# m. Find the index of the second occurrence of the word ‘course’.
# n. Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd
# characters in the string.
# o. Replace the period (.) with an exclamation point (!).
# p. Replace all occurrences of the word ‘course’ with ‘class’.
#######################
# Importing necessary packages

#######################

###############################################

###############################################
def main():

    s = ' The Python course is the best course that I have ever taken. '

    # a. Display the length of the string
    print('a. Display the length of the string')
    print(len(s))
    print()

    # b. Find the index of the first ‘o’ in the string.
    print('b. Find the index of the first ‘o’ in the string.')
    print(s.index('o'))
    print()

    # c. Trim off the leading spaces only.
    print('c. Trim off the leading spaces only.')
    print(s.lstrip(' '))
    print()

    # d. Trim off the trailing spaces only.
    print('d. Trim off the trailing spaces only.')
    print(s.rstrip(' '))
    print()

    # e. Trim off both the leading and trailing spaces
    print('d. Trim off the trailing spaces only.')
    s1 = s.strip(' ')
    print(s1)
    print()

    # f. Fully capitalize the string.
    print('f. Fully capitalize the string.')
    print(s1.upper())
    print()

    # g. Fully lowercase the string.
    print('g. Fully lowercase the string.')
    print(s1.lower())
    print()

    # h. Display the number of occurrence of the letter ‘d’ and of the word ‘the’.
    print('h. Display the number of occurrence of the letter d and of the word the')
    print('d count = ', s1.count('d'))
    print('the count = ', s1.count('the'))
    print()

    # i. Display the first 15 characters of the string.
    print('i. Display the first 15 characters of the string.')
    print(s1[:15])
    print()

    # j. Display the last 10 characters of the string.
    print('j. Display the last 10 characters of the string.')
    print(s1[-10:])
    print()

    # k. Display characters 5-23 of the string.
    print('k. Display characters 5-23 of the string.')
    print(s1[5:23])
    print()

    # l. Find the index of the first occurrence of the word course.
    print('l. Find the index of the first occurrence of the word course.')
    print(s1.index('course'))
    print()

    # m. Find the index of the second occurrence of the word course.
    print('m. Find the index of the second occurrence of the word course.')
    print(s1.find('course', 12))  # set the start position after the first one, which is 11th, so set start = 12
    print()

    # n. Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd
    #       characters in the string.
    print('n. Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd '
          'characters in the string.')
    # 1st method, just enumerate the string and save the matching index in a list using list comprehension
    print('1st method: List comprehension and count yourself.')
    index_str = [index for index, char in enumerate(s1) if char == 't']
    print(index_str)
    # then use eyeball power to count
    print('We see the second to last occurence in the range 7:33 is 21.')
    print()

    # 2nd method use recursive rfind
    # although, occurence is only 2 so full recursive isn't needed.
    print('2nd method: recursive rfind')
    last_find = s1.rfind('t', 7, 33)   # find the right most--last--occurrence
    second_to_last = s1.rfind('t', 7, last_find)  # reset the range with the max being the last occurrence and rerun
    print(second_to_last)
    print()

    # o. Replace the period (.) with an exclamation point (!).
    print('o. Replace the period (.) with an exclamation point (!).')
    print(s1.replace('.', '!'))
    print()

    # p. Replace all occurrences of the word ‘course’ with ‘class’.
    print('p. Replace all occurrences of the word ‘course’ with ‘class’.')
    print(s1.replace('course', 'class'))
    print()


###############################################

#######################
if __name__ == '__main__':
    main()
