import sys
import bisect

def count_subsets_leq(cap, weights):
    """
    weights 리스트를 반으로 나누어 부분합을 구한 뒤,
    두 절반의 합을 이분 탐색으로 조합하여 cap 이하인 경우의 수를 센다.
    """
    n = len(weights)
    mid = n // 2
    left = weights[:mid]
    right = weights[mid:]

    sumL = []
    def dfs_left(i, acc):
        if i == len(left):
            sumL.append(acc)
            return

        dfs_left(i+1, acc)

        dfs_left(i+1, acc + left[i])
    dfs_left(0, 0)
    sumR = []
    def dfs_right(i, acc):
        if i == len(right):
            sumR.append(acc)
            return
        dfs_right(i+1, acc)
        dfs_right(i+1, acc + right[i])
    dfs_right(0, 0)
    sumR.sort()
    total = 0
    for s in sumL:
        remain = cap - s
        cnt = bisect.bisect_right(sumR, remain)
        total += cnt

    return total

def main():
    input = sys.stdin.readline
    N, C = map(int, input().split())
    W = list(map(int, input().split()))
    print(count_subsets_leq(C, W))

if __name__ == "__main__":
    main()
