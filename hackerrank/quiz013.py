'''
# 정렬 문제
https://www.hackerrank.com/challenges/most-commons/problem
* 알파벳 갯수의 내림차순, 갯수가 같으면 알파벳의 오름차순으로 정렬

# sort howto

아래 문서 참고함
* https://docs.python.org/3.6/howto/sorting.html#sortinghowto

python 2.x 에서는 comparerator(a,b) 가 있었으나 3에서 없어짐(왜 없앤거냐...)
* https://docs.python.org/3.6/howto/sorting.html#the-old-way-using-the-cmp-parameter

대안으로 functools.cmp_to_key 함수를 이용하는 방법이 있다고 함
```
from functools import cmp_to_key

def compare(a, b):
  ...

list = [ ... ]
result = sorted(list, key=cmp_to_key(compare))
```
* 이럴거면 대체 왜 없앤거나... (-_-a)


'''
if __name__ == '__main__':
  dic = dict()
  for c in input().strip():
    cnt = dic[c] if c in dic else 0
    dic[c] = cnt + 1

  entries = sorted(dic.items(), key=lambda e: (-e[1], e[0]))
  for e in entries[:3]:
    print('{} {}'.format(e[0], e[1]))