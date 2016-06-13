# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_valid_string(s) :

    d=dict()

    for c in s :
        if c not in d :
            d[c]=1
        else :
            d[c]+=1

    comm=-1
    diff=0

#    print d

    for k in d :
        if d[k]!=comm :
            if comm==-1 :
                comm=d[k]
            else :
                diff+=1

    if diff==0 :
        return 'YES'


    if diff==1 :
       for k in d :
         if d[k]!=comm :
                if abs(d[k])==1 or abs(d[k]-comm)==1 :
                    return 'YES'
                else :
                    return 'NO'

    else :
        return 'NO'


import sys
s=sys.stdin.readline().strip()
print is_valid_string(s)
