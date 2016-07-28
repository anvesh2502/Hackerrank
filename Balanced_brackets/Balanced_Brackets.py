#!/bin/python

import sys

def is_balanced(s) :

    d=dict()
    d['{']='}'
    d['(']=')'
    d['[']=']'

    l=[]

    for c in s :

        if len(l)==0 :
            l.append(c)
        else :
            top=l[-1]
            if top in d and d[top]==c :
                l.pop()
            else :
                l.append(c)

    if len(l)==0 : return 'YES'
    return 'NO'












t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    print is_balanced(s)
