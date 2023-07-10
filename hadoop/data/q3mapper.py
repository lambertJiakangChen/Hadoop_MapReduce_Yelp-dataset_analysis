#!/usr/local/bin/python3.9

import sys
import json
# get the sum of UFC and print it with reviewid at first sum of UFC follow
for line in sys.stdin:
    j = json.loads(line.strip())
    UFC = j["useful"] + j["funny"] + j["cool"]
    print(j["review_id"] + "\t" + str(UFC))

