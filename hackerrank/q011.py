"""
# Deque
* https://www.hackerrank.com/challenges/py-collections-deque/problem

# Reflection
메소드 호출

* https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string

"""
from collections import deque
from inspect import signature

if __name__ == '__main__':
  N = int(input().strip())
  queue = deque()
  for i in range(N):
    cmd = input().strip().split(' ')
    method = getattr(queue, cmd[0])
    if len(cmd) > 1:
      method(cmd[1])
    else:
      method()
  print(*queue, sep=' ')