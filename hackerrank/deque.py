'''
# 문서
https://docs.python.org/3.6/library/collections.html#collections.deque


## 수정 메소드
* .append(obj) - 오른쪽(뒤)에 붙임
* .appendLeft(obj) - 왼쪽(앞)에 붙임
* .pop() - 오른쪽(뒤)에서 하나 꺼냄
* .popLeft() - 왼쪽(앞)에서 하나 꺼냄
* .clear() - 다 지움
* .insert(index, obj) - index 위치에 obj 추가함
* 

## 조회 메소드
* .maxlen(field임) - 최대 용량
* .copy() - element들 얕은 복사본 반환



'''
from collections import deque

q = deque()
q.append('a')
q.append('b')
print(q)
q.appendleft('c')
print(q)