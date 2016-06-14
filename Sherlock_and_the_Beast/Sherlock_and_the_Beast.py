#!/bin/python

import sys




def get_max_number(n) :

    if n<3 :
        return -1


    q=n/3
    if (n%3)==0 :
        return '5'*n
    while q>=0 :
        rem=n-3*q
        if (rem%5)==0 :
            return '5'*(3*q)+'3'*rem
        q-=1

    return -1

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    print get_max_number(n)
