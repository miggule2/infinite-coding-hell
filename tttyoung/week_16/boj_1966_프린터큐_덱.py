from collections import deque

def printqu(dq, m):
    target = dq[m][0] #타겟문서의 고정 인덱스, 추적하기위해 고정인 값
    count = 0

    while True:
        if len(dq) == 1:
            count += 1
            break
        elif dq[0][1] < max(dq[i][1] for i in range(1, len(dq))):
            dq.rotate(-1) #맨 앞 문서를 뒤로 보냄
        else:
            if target == dq[0][0]: #타겟문서가 첫값이면 탈출
                count += 1
                break
            else:
                dq.popleft() #아니라면 pop
                count+=1
    return count

t = int(input()) #testcase수
for i in range(t):
    n, m = map(int, input().split()) #문서의개수, 타겟문서의 초기 인덱스
    #문서의 중요도를 리스트로 받고, enumerate를 이용하여 입력받은 문서의 인덱스를 남겨줌.
    #문서의 중요도만 입력 받기때문에 중요도가 같은 경우 문서를 구분하기 위함.
    dq = deque([i, v] for i, v in enumerate(list(map(int, input().split()))))
    print(printqu(dq, m))