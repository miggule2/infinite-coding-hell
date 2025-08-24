n = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

least_price = cost[0] #최소가격을 처음값으로 설정
result = 0
for i in range(n-1):
    if cost[i]<least_price: #해당구역 가격이 최소가격보다 작으면 
        least_price = cost[i] #최소가격 갱신
    result += (least_price*road[i]) #결과값 누적, 위 if문에 해당안해도 결과값 계산
print(result)


