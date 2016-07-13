#!/bin/python

import sys

def exists(l,val) :

    if len(l)==0 :
        return False

    if len(l)==1 :
        return l[0]==val

    mid=(0+len(l))/2

    if l[mid]==val : return True

    if l[mid]<val :
        l=l[0:mid]
        return exists(l,val)
    l=l[mid:]
    return exists(l,val)

def get_suffix_sum_list(l) :

    suffix_list=[]

    total=sum(l)
    suffix_list.append(total)

    for i in range(0,len(l)) :
        total=total-l[i]
        suffix_list.append(total)

    return suffix_list




def equal_stacks(h1,h2,h3) :

   l1=get_suffix_sum_list(h1)
   l2=get_suffix_sum_list(h2)
   l3=get_suffix_sum_list(h3)

   index1,index2,index3=[0,0,0]

   while index1<len(l1) and index2<len(l2) and index3<len(l3) :

       if l1[index1]==l2[index2] and l2[index2]==l3[index3] :
           return l1[index1]

       m=max(l1[index1],l2[index2],l3[index3])

       if m==l1[index1] :
            index1+=1

       if m==l2[index2] :
            index2+=1

       if m==l3[index3] :
            index3+=1

   return 0










n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = map(int,raw_input().strip().split(' '))
h2 = map(int,raw_input().strip().split(' '))
h3 = map(int,raw_input().strip().split(' '))
print equal_stacks(h1,h2,h3)
