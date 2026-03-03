import sys

def solve():
    n = int(sys.stdin.readline())
    
    memo = {}
    
    i = 1
    while i * i <= n:
        memo[i * i] = 1
        i += 1
        
    for i in range(1, n + 1):
        if i in memo:
            continue
            
        min_val = i
        
        j = 1
        while j * j < i:
            count = 1 + memo[i - j * j]
            if count < min_val:
                min_val = count
            j += 1
            
        memo[i] = min_val

    print(memo[n])

solve()