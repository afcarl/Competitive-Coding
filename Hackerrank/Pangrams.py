#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
z=[]
for a0 in range(q):
    m = int(input().strip())
   
    z.append(m)
   
def shift(nelements, k):       
    result = []
    length = len(nelements)
    start = (length - k) % length
    for i in range(length):
        result.append(nelements[(start + i) % length])
    return result
result1=[]
result1=shift(a,k)
for i in range(len(z)):
    print (result1[z[i]])

