memo = {} #메모지에이션
def w(a, b, c):
    if (a, b, c) in memo: #이미 메모에 저장된 값이면 메모에서 꺼내서 씀
        return memo[(a, b, c)]

    elif a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b < c:
        memo[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c) #점화식, 나온값 메모에 저장
        return memo[(a, b, c)]

    else:
        memo[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1) #점화식, 나온값 메모에 저장
        return memo[(a, b, c)]
    
while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")