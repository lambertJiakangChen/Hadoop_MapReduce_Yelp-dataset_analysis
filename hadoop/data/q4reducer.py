#!/usr/local/bin/python3.9

import sys

n_dict = {}
t_dict = {}
rand_list = []
g = 0
# put value into correspond dictionary put uid in list
for line in sys.stdin:
    line = line.strip()
    b_id, time, bname, rand= line.split("\t") 
    if rand != '-':
        rand_list.append(rand)
    if time == "-":
        n_dict[b_id] = bname
    elif b_id not in t_dict.keys():
        time_list = []
        time_list.append(time)
        t_dict[b_id] = time_list
    else:
        t_dict.setdefault(b_id,[]).append(time)
# replace the business id key to business name drop the key not in business json
for k in list(t_dict):
    if k in n_dict.keys():
        t_dict[n_dict[k]] = t_dict.pop(k)
    else:
        del t_dict[k]
# print the result in uid, time and business name format
for k, v in t_dict.items():
    for i in v:
        print( rand_list[g] + "\t"+ i + "\t" + k)
        g = g + 1
        


        
        

       

  

