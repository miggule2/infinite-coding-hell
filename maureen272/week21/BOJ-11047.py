# BOJ 11047: 동전 0
import sys 

input = sys.stdin.readline # 입력을 빠르게 받기 위해 sys.stdin.readline 사용

N, K = map(int, input().split()) # N: 동전의 종류, K: 동전의 가치 합
coins = [int(input()) for _ in range(N)] # 동전의 가치는 오름차순으로 주어짐

count = 0 
for coin in reversed(coins): # 동전의 가치를 큰 것부터 사용하기 위해 reversed 사용
    if K == 0: # 가치의 합이 0이 되면 더 이상 동전을 사용할 필요 없음
        break
    count += K // coin # 현재 동전으로 만들 수 있는 최대 개수 추가
    K %= coin # 남은 가치의 합 업데이트

print(count)
