#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
r=[a,b,c,d,e]
l=[a,b,c,d,e]
g=[a,b,c,d,e]
min1= min(l)
max1= max(l)
minsum=0
maxsum=0
c=1
d=1
e=[]
z=[]
for i in range(len(r)):
    if min1==r[i] and c==1:
        del l[i]
        k=l
        c=2
    elif max1==r[i] and d==1:
        del g[i]
        z=g
        d=2
        

minsum=sum(z)
maxsum=sum(k)
print(minsum,end=" ")
print(maxsum)