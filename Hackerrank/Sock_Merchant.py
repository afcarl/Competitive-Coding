#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
d={}
m=0
for i in range(len(c)):
    if c[i] in d:
        del d[c[i]]
        m=m+1
    else:
        d[c[i]]=c[i]
print(m)    
    
