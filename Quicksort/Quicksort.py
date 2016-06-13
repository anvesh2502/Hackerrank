#!/bin/python
def quick_sort(l) :

   if len(l)<=1 :
        return l
   pivot=l[0]
   l=l[1:]
   left=[]
   right=[]

   for val in l :
        if val>pivot :
            right.append(val)
        else :
            left.append(val)
   l=quick_sort(left)+[pivot]+quick_sort(right)
   print_list(l)
   return l





def print_list(l) :

    for val in l :
        print val,
    print

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quick_sort(ar)
