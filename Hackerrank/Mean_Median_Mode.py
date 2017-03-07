import sys
from collections import Counter
from scipy.stats import mode

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
c=sorted(c)
#print(c)

d={}
mode1=[]
def median(c):
    if len(c)%2==0:
        
        median=(c[int(len(c)/2)]+c[int(len(c)/2)-1])/2
    else:
        median=c[((len+1)/2)-1]
    print (median)
def mean(c):
    average1=sum(c)/float(len(c))
    print (average1)
def mode1(c):
    d=Counter(sorted(c)).most_common()
    max1=-11111111111111
    
    for i in range(len(d)):
        if max1<d[i][1]:
            max1=d[i][1]
        elif max1==d[i][1]:
            mode1.append(d[i][0])
        t=[]
        t=mode1
        print(t)
        
mean(c)
median(c)
print (mode(c).mode[0])