# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
arr=map(int,sys.stdin.readline().strip().split())
f=arr[0]
l=arr[1]
N=arr[2]
fib_arr=[0]*(N+1)
fib_arr[0]=f
fib_arr[1]=l
for i in range(2,N+1) :
    fib_arr[i]=fib_arr[i-1]*fib_arr[i-1]+fib_arr[i-2]
print fib_arr[N-1]
