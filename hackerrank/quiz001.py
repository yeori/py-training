"""
https://www.hackerrank.com/challenges/py-if-else/problem
"""
def isOdd(n) :
  return n % 2 > 0

def btw(n, lo, hi) :
  return lo <= n and n <= hi

if __name__ == '__main__':
  n = int(input().strip())
  wierd = isOdd(n) or btw(n, 6, 20)
  answer = 'Wierd' if wierd else 'Not Wierd'
  print(answer)
