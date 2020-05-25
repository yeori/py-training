"""
# OrderedDict
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

# str.rsplit(sep, cnt:int)
주어진 문자열을 sep를 구분자로 cnt번 split 함

* https://docs.python.org/3.6/library/stdtypes.html#str.rsplit


"""
from collections import OrderedDict

def add(dic, key, val):
  if key in dic:
    dic[key] += val
  else:
    dic[key] = val

if __name__ == '__main__':
  # 1. number of lines and columns
  N = int(input().strip())
  # row = input().strip().rsplit(' ', 1)
  # print(row)
  odict = OrderedDict()
  for i in range(N):
    row = input().strip().rsplit(' ', 1)
    add(odict, row[0], int(row[1]))
  for k in odict:
    print('{0} {1}'.format(k, odict[k]))