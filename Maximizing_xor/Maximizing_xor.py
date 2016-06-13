#!/bin/python

# Complete the function below.


def  maxXor( l,  r):

   m=0
   for i in range(l,r+1) :
    for j in range(l,r+1) :
      res=i^j
      if res>m :
            m=res
   return  m



_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)
