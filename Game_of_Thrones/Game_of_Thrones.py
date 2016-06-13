
def has_pallindrome_permutation(s) :
    d=dict()
    for c in s :
        if c not in d :
            d[c]=1
        else :
            d[c]+=1
    mid_key=''
    count=0
    for k in d :
        if (d[k]%2)!=0 :
            count+=1
            mid_key=k
        if count==2 :
            return 'NO'
    try :
     d.pop(mid_key,None)
    except KeyError :
     pass
    for key in d :
        if (d[key]%2)!=0 :
            return 'NO'
    return 'YES'
s=raw_input()
print has_pallindrome_permutation(s.strip())
