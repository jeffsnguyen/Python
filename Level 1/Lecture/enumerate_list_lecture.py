'''
list enumerate lecture
'''

def main():
    names = ['Jeff', "Ngoc", "Son", "Nguyen"]
    for i, name in enumerate(names):
        print(str(i+1) + ' : ' + name)

#######################
if __name__ == '__main__':
    main()