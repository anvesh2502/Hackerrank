# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here
  answer = 0
  prices=sorted(prices)
  for price in prices :
        if rupees>price :
            answer+=1
            rupees-=price
  return answer

  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
