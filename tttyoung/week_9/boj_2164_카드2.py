from collections import deque
n = int(input())
numdeq = deque([i for i in range(1, n+1)])

while len(numdeq) > 1:
    numdeq.popleft()
    numdeq.rotate(-1)

print(numdeq.popleft())