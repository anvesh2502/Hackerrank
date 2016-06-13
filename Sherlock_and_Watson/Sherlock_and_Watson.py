# Enter your code here. Read input from STDIN. Print output to STDOUT




import sys
n,k,q=map(int,sys.stdin.readline().strip().split())
l=map(int,sys.stdin.readline().strip().split())
num=k%len(l)
low=len(l)-num
l=l[low:]+l[0:low]
for line in sys.stdin :
    print l[int(line.strip())]



    
