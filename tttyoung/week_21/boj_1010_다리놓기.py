def factorial(x): #팩토리얼 계산함수
    f = 1
    for i in range(x):
        f *= i+1
    return f

def bridge(n, m): #점화실 계산함수
    return factorial(m) // (factorial(n) * factorial(m-n))

t = int(input())
for i in range(t):
    n, m = map(int, input().split())   
    print(bridge(n, m))
