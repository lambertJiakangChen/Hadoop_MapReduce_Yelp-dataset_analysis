#!/usr/local/bin/python3.9

import sys

previous = None
id_list = []
# compress the bussiness id correspond to category
for line in sys.stdin:
    key, value = line.split( '\t' )

    if key != previous:
        if previous is not None:
            print(previous + '\t',  id_list)

        previous = key
        id_list = []

    id_list.append(value.replace("\n", ""))

print(previous + '\t',  id_list)