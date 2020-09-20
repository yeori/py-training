'''
# Introduction to Set
* https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# API
* enumerate() - https://docs.python.org/3.8/library/functions.html#enumerate
* class set([iterable]) - https://docs.python.org/3.8/library/stdtypes.html#set

# sample
```
10
161 182 161 154 176 170 167 171 170 174

```
'''
def average(array):
  # your code goes here
  distint_h = set(array)
  total = sum(distint_h)
  cnt = len(distint_h)
  return total/cnt

if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  result = average(arr)
  print(result)