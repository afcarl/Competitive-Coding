#!/bin/python3

import sys


t = int(input().strip())
c=[]
d=[1,1]
for a0 in range(t):
    n = int(input().strip())
    c.append(n)
x=len(c)
h={}
g=[30,36,34,31,35,32,33,29]
s=max(c)
def cycle(q):
    if q==0:
        print (1)
        d.append(1)
    else:
        
        for i in range(2,q+2):
            if i%2==0:
                d.append(d[i-1]*2)
            else:
                d.append(d[i-1]+1)
#        print(d[len(d)-1])     
    
cycle(s)
#print(d)
for i in range(0,len(c)):
#    print (c[i])
    print(d[c[i]+1])