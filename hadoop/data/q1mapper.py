#!/usr/local/bin/python3.9

import sys
import json
# find business open on the weekend, get all categories and print each line with categories at first follow with the response bussiness id
for line in sys.stdin:
    j = json.loads(line.strip())
    if j['hours'] is not None:
        if 'Saturday' in j['hours'] or 'Sunday' in j['hours']:
            if j['categories'] is not None:
                words = j['categories'].split(', ')
                # print(words)
                for word in words:
                    print(word + "\t" + j["business_id"])