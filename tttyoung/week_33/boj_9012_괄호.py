
num = int(input())
def ps(l):
    s = []
    for j in l:
        if j == "(": #괄호 열리면 스택에 추가
            s.append(j)
        else:
            if not s: #닫힘괄호 나오는데 스택이 비어있으면 NO출력
                return("NO")
            else: s.pop() #스택 pop
    if not s: #끝난 후에는 스택이 비어있어야함
        return("YES")
    else:
        return("NO")

for i in range(num):
    l = list(input())
    print(ps(l))
