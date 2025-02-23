def solve():
    import sys
    
    input = sys.stdin.readline
    
    N = int(input().strip())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 1. A를 오름차순 정렬
    A_sorted = sorted(A)
    
    # 2. B의 인덱스를 B값에 따라 내림차순 정렬
    indices_sorted_by_B = sorted(range(N), key=lambda i: B[i], reverse=True)
    
    # 3. A'를 재배열하기 위한 리스트 준비
    A_rearranged = [0] * N
    
    # 4. B에서 큰 값부터 작은 값 순으로, A에서 작은 값부터 할당
    for i, idx in enumerate(indices_sorted_by_B):
        A_rearranged[idx] = A_sorted[i]
        
    # 5. 최종 S 계산
    S = sum(A_rearranged[i] * B[i] for i in range(N))
    print(S)

solve()