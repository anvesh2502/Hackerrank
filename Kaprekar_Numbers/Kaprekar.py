# Enter your code here. Read input from STDIN. Print output to STDOUT

def is_kaprekar(num) :

   n=num*num
   if n==1 :
        return True
   if n<10 :
      return False
   s=str(n)
   mid=(0+len(s))/2
   if (int(s[0:mid])+int(s[mid:]))==num :
        return True
   return False


p=int(raw_input().strip())
q=int(raw_input().strip())
l=[]
flag=False
for val in range(p,q+1) :
    if is_kaprekar(val) :
      print val,
      flag=True
if flag is False :
    print 'INVALID RANGE'
