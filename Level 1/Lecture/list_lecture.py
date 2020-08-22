'''
list lecture
'''

def main():
    print('Calculate the Average of a List')
    allNumbers = []

    while True:
        num = ''
        while num == '':
            num = input('Add a number to the list (s to stop)): ')
        if num != 's':
            allNumbers.append(float(num))
        else:
            break

    ttl = 0.0
    for num in allNumbers:
        ttl += num

    avg = ttl / len(allNumbers)

    print('Average is: ' + str(avg))

#######################
if __name__ == '__main__':
    main()