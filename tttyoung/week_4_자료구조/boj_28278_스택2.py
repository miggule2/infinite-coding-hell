import sys
num = int(sys.stdin.readline()) 
st = []
for i in range(num):
    cmlist = list(map(int, sys.stdin.readline().split())) 

    if cmlist[0] == 1:
        st.append(int(cmlist[1]))
    elif cmlist[0] == 2:
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
            st.pop()
    elif cmlist[0] == 3:
        print(len(st))
    elif cmlist[0] == 4:
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif cmlist[0] == 5:
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])
