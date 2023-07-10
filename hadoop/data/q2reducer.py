#!/usr/local/bin/python3.9

import sys
previous = None
mysum = 0

mdict = {
    '01': 0, 
    '02': 0,
    '03': 0,
    '04': 0,
    '05': 0, 
    '06': 0, 
    '07': 0, 
    '08': 0, 
    '09': 0, 
    '10': 0, 
    '11': 0, 
    '12': 0
}
# compress the month number and save it into dictionary with key month and value numbers of months appear
for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            mdict[previous] = mysum

        previous = key
        mysum = 0

    mysum = mysum + int( value )
    mdict[previous] = mysum
# print into proportion format
total = sum(mdict.values())
for months in mdict:
    print(months + '\t' + str(round(100 * (mdict[months])/total,2)) + '%' )

