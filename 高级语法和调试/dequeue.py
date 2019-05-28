from collections import deque

q = deque(['a', 'b', 'c'])
print(q)

q.append("d")
print(q)

q.appendleft('x')
print(q)