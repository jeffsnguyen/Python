# date and time  lecture

import datetime

def main():
    dateTime = datetime.datetime.today()  # Current date and time today
    print(dateTime)
    print(type(dateTime))
    print()

    dateTime = datetime.datetime.now()  # Current date and time today
    print(dateTime)
    print(type(dateTime))
    print()

    dateTime = datetime.datetime.utcnow()  # Current date and time today in UTC
    print(dateTime)
    print(type(dateTime))
    print()

    dateTime = datetime.datetime.min  # Earliest support datetime
    print(dateTime)
    print(type(dateTime))
    print()

    dateTime = datetime.datetime.max  # Latest support datetime
    print(dateTime)
    print(type(dateTime))
    print()

    date = datetime.date.today()  # Without time
    print(date)
    print(type(date))  # also different type
    print()

    # Create your own object
    d = datetime.date(2020, 12, 31)  # Without time
    print(d)
    print(type(d))  # also different type
    print()

    # Create your own object
    d = datetime.datetime(2020, 12, 31)  # With time, time is assumed to be midnight
    print(d)
    print(type(d))  # also different type
    print()

    # Create your own object
    d = datetime.datetime(2020, 12, 31, 11, 31, 15)  # With time, time is assumed to be midnight
    print(d)
    print(type(d))  # also different type
    print()

    # adding and subtract date & time
    d = datetime.datetime(2016, 12, 14, 10, 31)
    d1 = d + datetime.timedelta(days=1)
    print(f'{d1}')

    d2 = d - datetime.timedelta(days=1)
    print(d2)

    d3 = d - datetime.timedelta(days=1, minutes=15, hours=15)
    print(d3)

    d4 = datetime.datetime(2016, 12, 14, 10, 31)
    d5 = datetime.datetime(2016, 12, 10, 10, 11)
    z = abs(d5 - d4)
    print(d4 - d5)
    print(f'{z.days} days')
    print(z.microseconds)
    print(z.seconds)
    print()

    print(d4)
    print(str(d4))  # no formatting choice
    print(d.strftime('%d/%m/%y : %H:%M:%S:%ms'))
    print(d.strftime('%d--%m--%y : %H:::%M:::%S'))
    print(d.strftime('%d/%m/%Y : %H:%M:%S'))
    print()

    d6 = datetime.datetime(year=2016, month=12, day=14, hour=10, minute=31, second=12, microsecond=12354)
    print(d6)
    #d = input('Enter date: ')
    #d1 = datetime.datetime.strptime(d, '%Y-%m-%d')
    #print(d1)
    #print(type(d1))

#######################
if __name__ == '__main__':
    main()