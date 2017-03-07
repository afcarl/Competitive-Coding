
import sys


t = int(input().strip())
c=[]
d=[]
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    d.append(k)
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    c.append(a)

k1=0

for i in range(t):
    k1=0
    for j in range(n):
        if c[i][j]<=0:
            k1=k1+1
        else:
            continue
    
    if k1>=d[i]:
        print ("NO")
    else:
        print("YES")
