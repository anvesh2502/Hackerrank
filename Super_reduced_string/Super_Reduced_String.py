# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

s=sys.stdin.readline().strip()
st=[]

for i in range(0,len(s)) :

    if len(st)==0 :
        st.append(s[i])
    else :
        top=st[-1]
        if top==s[i] :
          st.pop()
        else :
            st.append(s[i])

res=''.join(st)
if len(res)==0 :
    print 'Empty String'
else :
    print res
