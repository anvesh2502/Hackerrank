# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def greater(l1,l2) :

    if l1[1]>l2[1] :
        return 1
    if l1[1]==l2[1] :

      if l1[0][1]>=l2[0][1] :
            return 1
      return -1
    return -1



def sorted_orders(l) :

    d=dict()
    for i in range(0,len(l)) :

        d[i+1]=(l[i],sum(l[i]))

    #print d

    res=sorted(d,key=lambda x : d[x],cmp=greater)
    for val in res :
        print val,
    print








sys.stdin.readline();
l=[]
for line in sys.stdin :
    (a,b)=map(int,line.strip().split())
    l.append((a,b))
sorted_orders(l)
    
