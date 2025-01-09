import sys
from collections import deque #큐에서는 pop을 하면 맨 앞의 요소가 나오게 되고 나머지 요소들이 한칸씩 왼쪽으로 이동해야하므로 리스트를 사용하면 비효율적임
#deque를 사용하면 원래 큐를 사용할대의 시간복잡도인 O(n)에서 O(1)이 됨

num = int(sys.stdin.readline())
dq = deque()
for i in range(num):
    cmlistqu = sys.stdin.readline().split()

    if cmlistqu[0] == "push":
        dq.append(int(cmlistqu[1]))

    elif cmlistqu[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft()) #가장 왼쪽 요소가 나옴

    elif cmlistqu[0] == "size":
        print(len(dq))

    elif cmlistqu[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif cmlistqu[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif cmlistqu[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])