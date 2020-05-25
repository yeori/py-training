'''
# 큐브 쌓기
* https://www.hackerrank.com/challenges/piling-up/problem
* 가장 큰 큐브부터 작은 큐브 순으로 차곡차곡 쌓음
* 단, 주어진 큐브 리스트에서 좌우에서만 빼낼 수 있음(안쪽에서는 빼면 안됨)

# algo
* 왼쪽에서부터 단조증가할때까지 index ++
* 오른쪽에서부터 단조감소할때까지 index --
* 둘이 한곳에서 만나면 yes, 그렇지 않으면 no
'''
def solve(cubes):
  lo = 0
  hi = len(cubes) - 1
  while lo < hi and cubes[lo] >= cubes[lo+1]:
    lo += 1
  while lo < hi and cubes[hi-1] <= cubes[hi]:
    hi -= 1
  return 'Yes' if lo == hi else 'No' 

if __name__ == '__main__':
  T = int(input().strip())
  for tc in range(T):
    int(input().strip()) # just comsume
    cubes = map(lambda str: int(str), input().strip().split(' '))
    print(solve(list(cubes)))
