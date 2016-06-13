# Enter your code here. Read input from STDIN. Print output to STDOUT

def factorial(n) :

    if n==0 :
        return 1
    return n*factorial(n-1)



def count_same_pairs(l) :

    freq=dict()
    for val in l :
        if val not in freq :
            freq[val]=1
        else :
            freq[val]+=1

    res=0

    for k in freq :
        if freq[k]>1 :
          res+=freq[k]*(freq[k]-1)
    return res



import sys
N=int(sys.stdin.readline().strip())
i=0
while i<N :
    sys.stdin.readline()
    l=map(int,sys.stdin.readline().strip().split())
    print count_same_pairs(l)
    i+=1
