import sys
from collections import deque 

num = int(sys.stdin.readline())
dq = deque()
for i in range(num):
    cmlistqu = sys.stdin.readline().split()

    if cmlistqu[0] == "push_front":
        dq.appendleft(int(cmlistqu[1])) #왼쪽에 요소를 추가

    elif cmlistqu[0] == "push_back":
        dq.append(int(cmlistqu[1]))

    elif cmlistqu[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft()) #가장 왼쪽 요소가 나옴

    elif cmlistqu[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop()) #가장 오른쪽쪽 요소가 나옴

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