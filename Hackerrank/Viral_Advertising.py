import sys
import math
n=input().strip()
n=int(n)
g=5
x=[]
c=0
for i in range(0,n):
    g=math.floor(g/2)
    c=c+g
    g=g*3
print (c)