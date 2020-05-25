from collections import namedtuple

Score = namedtuple('Score', 'kor eng math')
a = Score(*[1, 2, 3])
b = Score(*[4, 5,6])
print(a)
print(b)