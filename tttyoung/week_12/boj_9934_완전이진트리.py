def recursive_city(citylist, floor, result):
    mid = len(citylist) // 2 #중앙값이 부모노드이므로 
    result[floor].append(citylist[mid]) #그 중앙값을 첫층에 추가

    if len(citylist) == 1: #재귀 반복하다가 숫자가 한개가 남을때 재귀 종료
        return 
    
    #재귀 반복할수록 층수는 하나씩 내려감
    recursive_city(citylist[:mid], floor + 1, result) #mid기준으로 왼쪽값 재귀반복
    recursive_city(citylist[(mid+1):], floor + 1, result) #mid기준으로 오른쪽값 재귀 반복

k = int(input())
searchlist = list(map(int, input().split()))
result = [[] for i in range(k)] #층수에 맞는 빈 리스트 생성

recursive_city(searchlist, 0, result) #0층부터 시작하여 
for i in range(k):
    print(" ".join(map(str, result[i])))
