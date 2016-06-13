# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
f=sys.stdin
chapters,max_problems=map(int,f.readline().strip().split())
problems=map(int,f.readline().strip().split())
book=[None]*(chapters+1)
chapter_number=1
page_num=1
for i in range(0,chapters+1) :
    book[i]=[]
for problem_set in problems :

  num_dict=(problem_set/max_problems)+(int((problem_set%max_problems)!=0))
  if num_dict==1 :
   d=dict()
   d[page_num]=range(1,problem_set+1)
   book[chapter_number].append(d)
   page_num+=1
  else :
    prob_range=range(1,problem_set+1)
    st=0
    for i in range(0,num_dict) :
        d=dict()
        if i==num_dict-1 :
         d[page_num]=prob_range[st:]
        else :
         d[page_num]=prob_range[st:st+max_problems]
        st=st+max_problems
        book[chapter_number].append(d)
        page_num+=1
  chapter_number+=1
c=0
for ch in book :
    dicts=ch
    for d in dicts :
       k=d.keys()[0]
       if k in d[k] :
            c+=1
print c
