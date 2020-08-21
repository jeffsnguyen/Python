'''
if statement
'''

def main():
    age = input('What is your age?: ')
    age = int(age)
    ###check age code
    if age > 25:
        print('Older than 25')
    elif age < 100:
        print('Less than 100')
    else:
        print('Younger than 25')


#######################
if __name__ == '__main__':
    main()