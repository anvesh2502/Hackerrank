# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def exists(l,val) :
    mid=(0+len(l))/2
    if len(l)==1 :
        if l[0]==val :
            return True
        return False
    if l[mid]==val :
        return True
    if l[mid]>val :
        return exists(l[0:mid],val)
    else :
        return exists(l[mid:],val)



def ice_cream_positions(amt,flavours) :

    s_fl=sorted(flavours)
    j=len(s_fl)-1
    f1=0
    f2=0
    i1=0
    i2=0
    for i in range(0,len(s_fl)) :
       if exists(s_fl,amt-s_fl[i]) :
         f1=s_fl[i]
         f2=amt-s_fl[i]
         break
    for j in range(0,len(flavours)) :
        if flavours[j]==f1 :
            i1=j
            break
    for j in range(0,len(flavours)) :
        if flavours[j]==f2 :
            i2=j

    if i1>i2 :
        print i2+1,i1+1
    else :
        print i1+1,i2+1


N=int(sys.stdin.readline().strip())
for i in range(0,N) :
    M=int(sys.stdin.readline().strip())
    sys.stdin.readline()
    l=map(int,sys.stdin.readline().strip().split())
    ice_cream_positions(M,l)




            
