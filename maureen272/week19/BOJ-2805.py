# BOJ - 2805 - 나무 자르기
import sys
input = sys.stdin.readline # 빠른 입력을 위해(이거 안했을 경우 시간초과 발생)

N, M = map(int, input().split()) # 나무의 개수 N과 필요한 나무의 길이 M
trees = list(map(int, input().split())) # 나무의 길이 리스트

start = 0 # 이진 탐색의 시작점
end = max(trees) # 이진 탐색의 끝점
result = 0

while start <= end: 
    mid = (start + end) // 2 # 중간값 계산
    total = sum(tree - mid for tree in trees if tree > mid) # 현재 중간값으로 잘랐을 때 얻는 나무의 총 길이

    if total >= M: # 필요한 나무의 길이 M 이상이면
        result = mid  # 조건을 만족했으므로 기록하고 더 높게 자를 수 있는지 탐색
        start = mid + 1 # 더 높은 중간값 탐색
    else: # 필요한 나무의 길이 M 미만이면
        end = mid - 1 # 중간값을 낮춰서 탐색

print(result)
