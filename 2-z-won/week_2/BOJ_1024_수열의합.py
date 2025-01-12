def solve():
    import sys
    input = sys.stdin.readline
    
    N, L = map(int, input().split())
    
    # k = L, L+1, ..., 100
    for k in range(L, 101):
        # sum(x + x+1 + ... + x+(k-1)) = k*x + k(k-1)/2 = N
        # => k*x = N - k(k-1)/2
        # => x = [N - k(k-1)/2] / k
        
        # 먼저 N - k(k-1)/2 가 음수가 되면 x가 음수가 될 수밖에 없으므로 중단
        temp = N - k * (k - 1) // 2
        if temp < 0:
            break
        
        # 나누어 떨어지는지 확인
        if temp % k == 0:
            x = temp // k
            # x가 음이 아닌 정수인지 확인
            if x >= 0:
                # 조건 만족 -> k개의 수 출력
                sequence = [x + i for i in range(k)]
                
                # 길이 100 이하인지 확인
                if k <= 100:
                    print(" ".join(map(str, sequence)))
                    return
                else:
                    # 길이가 100 초과 시 -1
                    print(-1)
                    return
    
    # 여기까지 왔다면 조건을 만족하는 수열을 못 찾은 것
    print(-1)
