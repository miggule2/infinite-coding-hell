def fibonacci_sum(a, b):
    MOD = 1_000_000_000  # 10^9
    
    if b == 1:
        return 1  # F(1) = 1
    if b == 2:
        return 2 if a == 1 else 1  # F(1) + F(2) = 1 + 1 = 2
    
    fib = [0] * (b + 1)  # 피보나치 수열을 저장할 리스트
    fib[1], fib[2] = 1, 1
    
    for i in range(3, b + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD  # 10^9로 나머지 연산 적용
        
    result = sum(fib[a:b+1]) % MOD  # 범위 내 합을 구하고 MOD 연산 적용
    return result

# 입력 받기
a, b = map(int, input().split())

# 결과 출력
print(fibonacci_sum(a, b))
