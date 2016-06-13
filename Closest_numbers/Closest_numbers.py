# Enter your code here. Read input from STDIN. Print output to STDOUT

def exists(l,val) :

    if len(l)==0 :
        return False
    if len(l)==1 :
        if l[0]==val :
            return True
        return False
    if len(l)==2 :
        if l[0]==val or l[1]==val :
            return True
        return False
    mid=(0+len(l))/2
    if l[mid]==val :
        return True
    if l[mid]>val :
        return exists(l[0:mid],val)
    return exists(l[mid+1:],val)




import sys
n=raw_input()
l=map(int,sys.stdin.readline().strip().split())
l=sorted(l)
min_diff=max(l)
for i in range(0,len(l)-1) :
    if abs(l[i]-l[i+1])<min_diff :
        min_diff=abs(l[i]-l[i+1])

s=set(l)

for val in l :
    if val+min_diff in s :
        print val,val+min_diff,
