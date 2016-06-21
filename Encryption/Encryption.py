#!/bin/python

import sys
import math

s = raw_input().strip()
sq=math.sqrt(len(s))
r=int(math.floor(sq))
c=int(math.ceil(sq))
strings=[]
for i in range(0,c) :
  strings.append(s[i])
j=c
i=0
while j<len(s) :
   strings[i]+=s[j]
   j+=1
   if i==len(strings)-1 :
     i=0
   else :
     i+=1
for string in strings :
    print string,
print
    
