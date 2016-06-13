# Enter your code here. Read input from STDIN. Print output to STDOUT

from bisect import bisect_left

def exists(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def k_sum_arrays(l1,l2,K) :

    l1=sorted(l1)
    l2=sorted(l2)

    for val in l1 :

        for i in reversed(range(0,len(l2))) :
            if (val+l2[i])>=K :
                l2.pop(i)
                break
        else :
            return 'NO'
    return 'YES'


import sys
N=int(sys.stdin.readline().strip())
i=0
while i<N :
    s,K=map(int,sys.stdin.readline().strip().split())
    l1=map(int,sys.stdin.readline().strip().split())
    l2=map(int,sys.stdin.readline().strip().split())
    print k_sum_arrays(l1,l2,K)
    i+=1





    
