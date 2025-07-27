import heapq as hq #heap 모듈사용
import sys
input = sys.stdin.readline

n = int(input())
heap = [] 

for i in range(n): 
    x = int(input())
    if x == 0: #x==0일때 heappop을 하여 출력
        if len(heap) == 0:
            print(0)
        else:
            print(hq.heappop(heap)[1]) #[1]을 통해 절댓값이 아닌 원본 숫자 출력
    else:
        hq.heappush(heap, (abs(x), x)) #heap에 저장할때 (절댓값, 원본숫자)를 튜플로 저장