#!/usr/local/bin/python3.9

import sys
import json
# get the month from yelping_since print in format month first follow by 1
for line in sys.stdin:
    j = json.loads(line.strip())
    if j['yelping_since'] is not None:
        print(j['yelping_since'][5:7] + "\t1" )
