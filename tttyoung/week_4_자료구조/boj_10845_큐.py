num = int(input())
qu = []
for i in range(num):
    cmlistqu = input().split()

    if cmlistqu[0] == "push":
        qu.append(int(cmlistqu[1]))
    elif cmlistqu[0] == "pop":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu.pop(0))
    elif cmlistqu[0] == "size":
        print(len(qu))
    elif cmlistqu[0] == "empty":
        if len(qu) == 0:
            print(1)
        else:
            print(0)
    elif cmlistqu[0] == "front":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[0])
    elif cmlistqu[0] == "back":
        if len(qu) == 0:
            print(-1)
        else:
            print(qu[-1])