# Enter your code here. Read input from STDIN. Print output to STDOUT

def power_game(N) :

    i=0
    while N!=1 :
        if (N&(N-1))==0 :
            N=N/2
        else :
            v=N
            bits=0
            while v!=0 :
                v>>=1
                bits+=1
            N=N-(1<<(bits-1))
        i+=1
    if (i%2)==0 :
        print "Richard"
    else :
        print "Louise"

import sys
sys.stdin.readline()
for line in sys.stdin :
    power_game(int(line.strip()))
