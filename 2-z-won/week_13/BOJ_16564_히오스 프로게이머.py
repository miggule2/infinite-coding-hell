import sys
import threading
import bisect

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    if N == 1:
        print(A[0] + K)
        return
    A.sort()
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + A[i]
    low = A[0]
    high = A[0] + K  # 최대
    ans = low
    while low <= high:
        mid = (low + high) // 2
        # mid로 최소값을 맞추기 위한 비용: A에서 mid보다 작은 것들만 고려
        idx = bisect.bisect_left(A, mid)  # mid보다 작은 것 개수 = idx
        cost = mid * idx - prefix[idx]
        if cost <= K:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == "__main__":
    main()
