#!/usr/local/bin/python3.9

import sys

rdict={}
# put the sum in dictionary with key reviewid
for line in sys.stdin:
    key, value = line.split( '\t' )
    rdict[key] = int(value)
# sort with descending order
new_rdict = sorted(rdict.items(), key=lambda x:x[1], reverse=True)
# get the top 4415
for k,v in new_rdict[:4415]:
    print(k + '\t' + str(v))


