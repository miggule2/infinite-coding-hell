num = int(input())
st = []
for i in range(num):
    cmlist = input().split()

    if cmlist[0] == "push":
        st.append(int(cmlist[1]))
    elif cmlist[0] == "pop":
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
            st.pop()
    elif cmlist[0] == "size":
        print(len(st))
    elif cmlist[0] == "empty":
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif cmlist[0] == "top":
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
