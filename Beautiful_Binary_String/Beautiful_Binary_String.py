#!/bin/python

import sys

def beautiful_string_count(s) :

    l=[]

    for i in range(0,len(s)-2) :

        if s[i:i+3]=='010' :
            l.append(i)

    c=len(l)

    j=1
    while j<len(l) :

        if (l[j]-l[j-1])<3 :
            c-=1
            j+=2
        else :
            j+=1
    return c



n = int(raw_input().strip())
B = raw_input().strip()
print beautiful_string_count(B)
