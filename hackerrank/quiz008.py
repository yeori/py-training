"""
https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

# handling string
```
print({0:.3f}.format(12.34567)) # 12.345
```

# Named Tuple
* https://docs.python.org/3.6/library/collections.html#collections.namedtuple

"""
from collections import namedtuple


if __name__ == '__main__':
  skip_empty_val = lambda s: s
  # 1. number of lines and columns
  N = int(input().strip())
  cols = filter(skip_empty_val, input().split(' '))
  Score = namedtuple('Score', cols)
  
  # 2. fill scores
  total = 0
  for i in range(N):
    row = filter(skip_empty_val, input().split(' '))
    # value = list(row)
    # print('>> ', value)
    s = Score(*row)
    total += int(s.MARKS)

  print('{0:.2f}'.format(total/N))