import sys
t = int(input().strip())
a = []
for a_i in range(t):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
#print(a)
for i in range(int(t)):
    if a[i][0]>a[i][1]:
        s=a[i][2]%a[i][0]
        d=a[i][1]%a[i][0]

        print ((a[i][2]+d-1)%a[i][0])
        continue
    elif (a[i][1])%(a[i][0])==0 and a[i][1]==a[i][0]:
        print ((a[i][2]+a[i][0])-1)
    else:
        d=a[i][1]%a[i][0]
        s=a[i][2]%a[i][0]
        print ((a[i][2]+d-1)%(a[i][0]))
 