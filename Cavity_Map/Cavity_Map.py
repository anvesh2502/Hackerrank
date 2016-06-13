#!/bin/python

import sys
f=sys.stdin
n=int(f.readline())
big_list=[None]*n
j=0
for line in f :
    l=map(int,list(line.strip()))
    big_list[j]=(l)
    j+=1
for i in range(1,len(big_list)-1) :
    sl=big_list[i]
    for j in range(1,len(sl)-1) :
        val=sl[j]
        if val>sl[j-1] and val>big_list[i+1][j] and val>big_list[i-1][j] and val>sl[j+1] :
            sl[j]='X'
for l in big_list :
    print ''.join(map(str,l))
