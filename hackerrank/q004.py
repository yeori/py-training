def solve(N):
  nums = range(N) # [0, 1, .., N-1]
  mapped = map(lambda n: n*n, nums)
  return list(mapped)
  # return list(map(lambda n: n*n, nums))

if __name__ == '__main__':
  N = int(input().strip())
  sqr = solve(N)
  print(*sqr, sep='\n')