#동전 단위 리스트가 주어지고 k원을 만드는데 드는 동전 최솟값 구하기
#큰 단위부터 for문을 돌리며 k보다 작은 단위가 나온순간부터 계산 시작 -> 순간의 최선의 선택으로 최솟값을 구하기 (그리디)

def min_coin(n, k, coinlist):
    count = 0
    for i in range(n-1, -1, -1): #큰단위부터 비교하기 위해 for문 거꾸로 실행
        if k == 0: #금액 충족시 for문 탈출출
            break
        if coinlist[i]<=k: #단위가 금액보다 작은경우 몫을 count에 더해주고 금액을 나머지 금액으로 대체함.
            count += k//coinlist[i]
            k %= coinlist[i]
    return count

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
print(min_coin(N, K, coin_list))

