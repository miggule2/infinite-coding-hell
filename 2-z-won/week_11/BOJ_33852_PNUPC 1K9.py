import sys

def char2val(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


def main():
    input = sys.stdin.readline
    s = input().strip()
    k, p = map(int, input().split())
    n = len(s)

    # 36^(n-1-i) mod p 계산
    pow36 = [0] * n
    acc = 1
    for i in range(n-1, -1, -1):
        pow36[i] = acc % p
        acc = (acc * 36) % p

    # 초기 나머지 계산
    rem0 = 0
    v = [char2val(c) for c in s]
    for i in range(n):
        rem0 = (rem0 + v[i] * pow36[i]) % p

    # DP 초기화
    INF = 10**9
    dp = [INF] * p
    dp[rem0] = 0

    # 자리별 DP
    for i in range(n):
        dp_new = dp.copy()
        vi = v[i]
        wi = pow36[i]
        for u in range(36):
            if u == vi:
                continue
            delta = (u - vi) * wi % p
            for r in range(p):
                if dp[r] == INF:
                    continue
                r2 = r + delta
                if r2 >= p:
                    r2 %= p
                # 수정 횟수 +1
                dp_new[r2] = min(dp_new[r2], dp[r] + 1)
        dp = dp_new

    # 결과 출력
    ans = dp[k]
    print(ans if ans < INF else -1)

if __name__ == '__main__':
    main()
