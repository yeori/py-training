'''
# collections.Counter

# link
* https://www.hackerrank.com/challenges/collections-counter/problem

# sample
```
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

```
'''
from collections import Counter

if __name__ == '__main__':
  input().strip()
  shoes = Counter(input().strip().split(' '))
  # print(shoes)
  customers = int(input().strip())
  # print('# of customers ', customers)
  incomes = 0
  for idx in range(customers):
    shoe, price = input().strip().split(' ')
    if shoes[shoe] > 0 :
      incomes += int(price)
      shoes[shoe] -= 1
  
  print(incomes)
  
