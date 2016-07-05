# Enter your code here. Read input from STDIN. Print output to STDOUT

def anagram_count(s) :

  d=dict()
  val=0

  for i in range(0,len(s)+1) :

      j=0
      while j<i :
            sub=s[j:i]
            sub=''.join(sorted(sub))
            if sub in d :
                d[sub]+=1
            else :
                d[sub]=1
            j+=1

  for k in d :
    ans=d[k]*(d[k]-1)
    ans=ans/2
    val+=ans

  return val




import sys

sys.stdin.readline()
for line in sys.stdin :
    print anagram_count(line.strip())
