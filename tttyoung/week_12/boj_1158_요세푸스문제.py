from collections import deque
n, k = map(int, input().split())
dq = deque(i for i in range(1, n+1))

def Josephus(dq, k):
    result = []
    while len(dq)>=1: #마지막 한개 숫자 남을때까지
        dq.rotate(1 - k) #(-) 방향으로 돌려야하기때문에 1-k만큼 rotate한 후
        result.append(dq[0]) #첫번째값을 result에 추가
        dq.popleft() #첫번째 값 pop

    return result

print("<", ", ".join(map(str, Josephus(dq, k))), ">", sep = "")

