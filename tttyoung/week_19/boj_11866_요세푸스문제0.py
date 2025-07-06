from collections import deque
def yo(dq, k):
    result = []
    while(dq): #dq에 값이 남아있는동안 rotate를 통해 k번째값을 맨 앞으로 위치시키고 popleft를 통해 제거
        dq.rotate(-k+1)
        result.append(dq[0])
        dq.popleft()
    return result

n, k = map(int, input().split())
dq = deque()
for i in range(n):
    dq.append(i + 1)

print(f"<{', '.join(map(str, yo(dq, k)))}>") #f-string을 사용하여 출력, join을 사용하여 리스트내부값만 출력할 수 있도록 함

