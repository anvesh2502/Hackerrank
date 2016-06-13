# Enter your code here. Read input from STDIN. Print output to STDOUT

def mid_point_sum(l) :
    if len(l)<=1 :
        return 'YES'
    s=sum(l)
    l_sum=0
    r_sum=s-l[0]
    for i in range(1,len(l)) :
        if l_sum==r_sum :
            return 'YES'
        l_sum+=l[i-1]
        r_sum-=l[i]
    return 'NO'

import sys
sys.stdin.readline()
i=0
for line in sys.stdin :
    if (i%2)==0 :
        i+=1
        continue
    l=map(int,line.strip().split())
    print mid_point_sum(l)
    i+=1
