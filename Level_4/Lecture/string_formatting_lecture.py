# string formatting lecture


def main():
    age = 5
    print('Ying is %i years old'%age) # format flag i = integer
    print('Ying is %f years old'%age)  # format flag f = float
    print('Ying is %.1f years old' % age)  # format flag f = floag, truncate it 1 decimal place
    print('Ying is %e years old' % age)  # format flag e= exponential
    print('%s is 5 years old' %'Ying')  # format flag s = string
    print()

    name = 'Ying'
    age = 5
    print('%s is %i years old'%(name, age))  # multiple format flag
    print()

    print('{0} is {1} years old'.format(name, age))  # better because python figure out the type
    # better because python figure out the type, descriptive and use keyword arg so order doesn't matter
    print('{name} is {age} years old'.format(name = name, age = age))
    print('Same is {:.1f} years old'.format(5.75))   # specify decimal
    print('Same is {:,.1f} years old'.format(100000))  # specify decimal
    print()

    # f string
    name  = 'Julie'
    print(f'Hello {name}')
    height = 61.23
    print(f'{round(height)}')   # evaluate any expression inside the f string
    print()

    heightDict = {'Julie': 65, 'Sam':75, 'Larry':64}
    name = 'Sam'
    print(f'{name} is {heightDict[name]} inches')

    # floating point precision using f string
    print(f'{name} is {heightDict[name]:,.2f} inches')

#######################
if __name__ == '__main__':
    main()