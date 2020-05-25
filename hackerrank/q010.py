"""
# Word Order
* https://www.hackerrank.com/challenges/word-order/problem

# Dict 구현체
기본 dictionary 구현체와 입력 순서를 기억하는 OrderedDict 구현체

## OrderedDict
* https://docs.python.org/3.6/library/collections.html#collections.OrderedDict

## dict()
* https://docs.python.org/3.6/library/stdtypes.html#dict

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```
"""
from collections import OrderedDict

def acc(dic, key, v):
  if key in dic:
    dic[key] += v
  else:
    dic[key] = 1

if __name__ == '__main__':
  N = int(input().strip())
  odict = OrderedDict()
  for i in range(N):
    acc(odict, input().strip(), 1)
  
  print(len(odict))
  print(*odict.values(), sep= ' ')