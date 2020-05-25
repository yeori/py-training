"""
# defaultdict problem
* https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
* https://docs.python.org/3.6/library/collections.html#collections.defaultdict

# plain dictionary
* https://www.w3schools.com/python/python_dictionaries.asp

"""
from collections import defaultdict

if __name__ == '__main__':
  n, m = input().strip().split()
  dic = defaultdict(lambda: [])
  for i in range(int(n)): 
    word = input().strip()
    dic[word].append(i+1)
  
  for i in range(int(m)):
    word = input().strip()
    pos = dic[word]
    print(*pos, sep=' ') if pos else print('-1')

