import sys
n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
reverse=[]
x=0
c=0
def reverse_int(n):
    return int(str(n)[::-1])
for i in range(n,k+1):
   
    g=reverse_int(i)
    reverse.append(g)
    
for i in range(n,k+1):
    f=abs((i-reverse[x]))
#    print (f)
    if f%q==0:
        c=c+1
    
    x=x+1
print(c)