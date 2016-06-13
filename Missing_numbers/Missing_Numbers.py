# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_missing_numbers(l1,l2) :

    d1=dict()
    d2=dict()
    res=[]
    h,l=max(l2),min(l2)
    for i in range(l,h+1) :
        d2[i]=0
    for val in l2 :
        d2[val]+=1
    for v in l1 :
        if v not in d1 :
            d1[v]=1
        else :
            d1[v]+=1
    for key in d2 :
        if key not in d1 :
            res.append(key)
        else :
            if d1[key]!=d2[key] :
                res.append(key)
    for r in res :
        print r,
    print

import sys
sys.stdin.readline()
l1=map(int,sys.stdin.readline().strip().split())
sys.stdin.readline()
l2=map(int,sys.stdin.readline().strip().split())
get_missing_numbers(l1,l2)
