#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

a= [int(a0),int(a1),int(a2)]
b= [int(b0),int(b1),int(b2)]
c=0
d=0
j=0
for i in a:
   
    if i<b[j]:
        d=d+1
    elif i>b[j]:
        c=c+1
    j=j+1
print (c,end="")
print (" ",end="")
print (d)