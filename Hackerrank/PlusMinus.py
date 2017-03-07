#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
x=len(arr)
pos=0
neg=0
zero=0
for i in range(0,x):
    if arr[i]>0:
        pos=pos+1
    elif arr[i]<0:
        neg=neg+1
    else:
        zero=zero+1
pos_prop=round((pos/x),6)
neg_prop= round((neg/x),6)
zero_prop= round((zero/x),6)
print (pos_prop)
print (neg_prop)
print (zero_prop)