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