# Enter your code here. Read input from STDIN. Print output to STDOUT

def anagram_maker_count(s1,s2) :
    d1=dict()
    d2=dict()
    for c in s1 :
        if c not in d1 :
            d1[c]=1
        else :
            d1[c]+=1
    for c in s2 :
       if c not in d2 :
         d2[c]=1
       else :
        d2[c]+=1
    count=0
    for k in d1 :
        if k not in d2 :
           count+=d1[k]
        else :
            count+=abs(d1[k]-d2[k])
    for k in d2 :
        if k not in d1 :
            count+=d2[k]
    return count

import sys
s1=sys.stdin.readline().strip()
s2=sys.stdin.readline().strip()
print anagram_maker_count(s1,s2)

            
