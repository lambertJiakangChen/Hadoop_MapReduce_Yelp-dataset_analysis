#!/usr/local/bin/python3.9

import json
import sys
import re
import random
import string

for line in sys.stdin:

    b_id = ''
    mtime = '-'
    b_name = '-'
    # seperate two json file by their column number print in format bussiness id, time, bussiness name and uid the value that doesn't exist in certain json file print with '-'
    line = line.strip()
    j = json.loads(line.strip())
    if len(j) == 14:
        b_id = list(j.values())[0]
        b_name1 = list(j.values())[1]
        regex = re.compile(r'[\n\r\t]')
        b_name = regex.sub(' ', b_name1).strip()
        print(b_id + "\t" + mtime + "\t" + b_name + "\t" + "-")
    else:
        times = list(j.values())[1].split(', ')
        for time in times:
            b_id = list(j.values())[0]
            mtime = time
            print(b_id + "\t" + mtime + "\t" + b_name + "\t" + ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_')for _ in range(22)))
