from collections import deque

n = int(input())

q = deque(range(1, n + 1))

for _ in range(0, n - 1):
    q.popleft()
    q.append(q.popleft())

print(q[0])
