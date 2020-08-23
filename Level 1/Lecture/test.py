'''
demonstrate packages
'''
import myfunctions.mean as mean #implicit import
from myfunctions.mode import mode #explicit import

def main():
    print(mean.mean([1,2,3]))
    print(mode())
#######################3
if __name__ == '__main__':
    main()